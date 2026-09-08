import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy as np
import serial
import time
from collections import Counter

class WroRetoAbierto(Node):
    def __init__(self):
        super().__init__('wro_reto_abierto')

        # --- PARÁMETROS GENERALES Y DE COMPETENCIA ---
        self.giros_completados = 0
        self.MAX_GIROS = 12
        self.declare_parameter('sentido', 0)
        self.declare_parameter('distancia_objetivo', 0.4)
        self.declare_parameter('distancia_frontal_obstaculo', 0.45)
        self.declare_parameter('velocidad_motor', 20)
        self.declare_parameter('limite_angulo_max', 38.0)

        # PID
        self.declare_parameter('Kp_dist', 400.0)
        self.declare_parameter('Kd_dist', 40.0)
        self.declare_parameter('Ki_dist', 0.0)
        self.declare_parameter('Kp_ang', 0.0)
        self.declare_parameter('Kd_ang', 0.0)

        # Servo
        self.rec = 57
        self.izquierda = 30
        self.derecha = 90

        # Variables de distancia
        self.d = 999.0
        self.dd = 999.0
        self.di = 999.0
        self.sentido = self.get_parameter('sentido').value

        # PID memoria
        self.prev_error_dist = 0.0
        self.integral_dist = 0.0
        self.prev_error_ang = 0.0
        self.last_time = self.get_clock().now()

        # Control de giro
        self.girando = False
        self.tiempo_inicio_giro = 0.0
        self.TIEMPO_GIRO = 1.5

        # Finalización
        self.finalizando = False
        self.tiempo_inicio_final = 0.0
        self.TIEMPO_AVANCE_FINAL = 4.0

        # Serial
        self.puerto_serial = '/dev/ttyUSB0'
        self.baudrate = 115200
        try:
            self.arduino = serial.Serial(self.puerto_serial, self.baudrate, timeout=1)
            time.sleep(2)
            self.get_logger().info(f'Conectado al Arduino en {self.puerto_serial}')
        except Exception as e:
            self.get_logger().error(f'No se pudo conectar al Arduino: {e}')
            self.arduino = None

        self.subscription = self.create_subscription(
            LaserScan, '/scan', self.lidar_callback, 10
        )
        self.get_logger().info('Nodo iniciado. Buscando pared frontal para determinar sentido...')

    # =========================================================================
    # FUNCIONES AUXILIARES
    # =========================================================================
    def distancia_moda(self, distancias, bin_width=0.02):
        if not distancias:
            return 999.0
        min_d = min(distancias)
        max_d = max(distancias)
        if max_d - min_d < bin_width:
            return np.mean(distancias)
        bins = np.arange(min_d, max_d + bin_width, bin_width)
        digitized = np.digitize(distancias, bins)
        counts = Counter(digitized)
        moda_bin_idx = max(counts, key=counts.get)
        centro_bin = (bins[moda_bin_idx - 1] + bins[moda_bin_idx]) / 2 if moda_bin_idx > 0 else bins[0]
        return centro_bin

    def detectardistancias(self, msg):
        dist_f, dist_d, dist_i = [], [], []
        for i, rango in enumerate(msg.ranges):
            if msg.range_min < rango < msg.range_max:
                angulo = np.degrees(msg.angle_min + (i * msg.angle_increment)) % 360
                if 75 <= angulo <= 105:
                    dist_f.append(rango)
                elif 165 <= angulo <= 195:
                    dist_d.append(rango)
                elif angulo >= 345 or angulo <= 15:
                    dist_i.append(rango)
        self.d = self.distancia_moda(dist_f)
        self.dd = self.distancia_moda(dist_d)
        self.di = self.distancia_moda(dist_i)

        self.get_logger().info(f'Lecturas (moda) -> Frente(d): {self.d:.2f}m | Izq(di): {self.di:.2f}m | Der(dd): {self.dd:.2f}m')

    def obtener_puntos_sector(self, msg, ang_min, ang_max):
        distancias_raw, angulos_raw = [], []
        for i, rango in enumerate(msg.ranges):
            if msg.range_min < rango < msg.range_max:
                angulo_rad = msg.angle_min + (i * msg.angle_increment)
                angulo_deg = np.degrees(angulo_rad) % 360
                en_rango = (ang_min <= angulo_deg <= ang_max) if ang_min < ang_max else (angulo_deg >= ang_min or angulo_deg <= ang_max)
                if en_rango:
                    distancias_raw.append(rango)
                    angulos_raw.append(angulo_rad)
        if not distancias_raw:
            return [], []
        moda = self.distancia_moda(distancias_raw, bin_width=0.02)
        if moda == 999.0:
            return [], []
        umbral = max(0.1, 0.2 * moda)
        distancias_filtradas, angulos_filtrados = [], []
        for r, a in zip(distancias_raw, angulos_raw):
            if abs(r - moda) <= umbral:
                distancias_filtradas.append(r)
                angulos_filtrados.append(a)
        return distancias_filtradas, angulos_filtrados

    def detectarlado_en_pared(self):
        if self.dd < self.di:
            self.sentido = 1
            self.get_logger().warn(f'Pared derecha más cercana (Der: {self.dd:.2f}m vs Izq: {self.di:.2f}m). Fijando Sentido 1 (Giro Derecha).')
        else:
            self.sentido = 2
            self.get_logger().warn(f'Pared izquierda más cercana (Izq: {self.di:.2f}m vs Der: {self.dd:.2f}m). Fijando Sentido 2 (Giro Izquierda).')

    # =========================================================================
    # BUCLE PRINCIPAL
    # =========================================================================
    def lidar_callback(self, msg):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        if dt <= 0:
            return

        self.detectardistancias(msg)

        dist_frontal_limite = self.get_parameter('distancia_frontal_obstaculo').value
        vel = int(self.get_parameter('velocidad_motor').value)

        if self.giros_completados >= self.MAX_GIROS and not self.finalizando:
            if not self.girando:
                self.finalizando = True
                self.tiempo_inicio_final = current_time.nanoseconds / 1e9
                self.get_logger().info(f'🚀 Iniciando avance final de {self.TIEMPO_AVANCE_FINAL} segundos...')

        if self.finalizando:
            tiempo_transcurrido = (current_time.nanoseconds / 1e9) - self.tiempo_inicio_final
            if tiempo_transcurrido >= self.TIEMPO_AVANCE_FINAL:
                self.get_logger().info('🛑 Avance final completado. Deteniendo robot.')
                self.enviar_a_arduino(velocidad=0, angulo_servo=self.rec)
                self.destroy_node()
                rclpy.shutdown()
                return

        if self.d < dist_frontal_limite and self.d > 0:
            if self.sentido == 0:
                self.detectarlado_en_pared()

            if not self.finalizando:
                if self.sentido == 1 and not self.girando:
                    self.giroizq90(vel)
                    self.girando = True
                    self.tiempo_inicio_giro = current_time.nanoseconds / 1e9
                    self.giros_completados += 1
                    self.get_logger().info(f'🔄 Giro IZQUIERDA #{self.giros_completados} de {self.MAX_GIROS}')
                elif self.sentido == 2 and not self.girando:
                    self.giroder90(vel)
                    self.girando = True
                    self.tiempo_inicio_giro = current_time.nanoseconds / 1e9
                    self.giros_completados += 1
                    self.get_logger().info(f'🔄 Giro DERECHA #{self.giros_completados} de {self.MAX_GIROS}')
        else:
            if self.girando and not self.finalizando:
                tiempo_actual = current_time.nanoseconds / 1e9
                if tiempo_actual - self.tiempo_inicio_giro > self.TIEMPO_GIRO:
                    self.girando = False
                    self.enviar_a_arduino(velocidad=0, angulo_servo=self.rec)
                    self.get_logger().info(f'✅ Giro completado. Continuando navegación...')

            if self.sentido == 0:
                self.get_logger().info('Avanzando recto buscando pared frontal...')
                self.enviar_a_arduino(velocidad=vel, angulo_servo=self.rec)
            elif self.sentido == 1:
                self.detectarderecha(msg, dt, vel)
            elif self.sentido == 2:
                self.detectarizquierda(msg, dt, vel)

    # =========================================================================
    # MANIOBRAS Y SEGUIMIENTO
    # =========================================================================
    def giroizq90(self, vel):
        self.get_logger().warn(f'¡Obstáculo al frente ({self.d:.2f}m)! Girando a la IZQUIERDA.')
        self.enviar_a_arduino(velocidad=vel, angulo_servo=self.izquierda)

    def giroder90(self, vel):
        self.get_logger().warn(f'¡Obstáculo al frente ({self.d:.2f}m)! Girando a la DERECHA.')
        self.enviar_a_arduino(velocidad=vel, angulo_servo=self.derecha)

    def detectarderecha(self, msg, dt, vel):
        dist_obj = self.get_parameter('distancia_objetivo').value
        limite_ang = float(self.get_parameter('limite_angulo_max').value)

        distancias, angulos = self.obtener_puntos_sector(msg, 165, 195)
        if len(distancias) < 5:
            self.enviar_a_arduino(0, self.rec)
            return

        correccion, dist_pared, err_ang = self.calcular_pid_svd(
            distancias, angulos, dist_obj, limite_ang, dt, es_derecha=True
        )

        angulo_servo = self.rec - correccion
        angulo_servo = max(self.izquierda, min(self.derecha, angulo_servo))

        self.get_logger().info(f'[Seguir Der] Dist: {dist_pared:.2f}m | Ang: {err_ang:+.1f}° | Servo: {angulo_servo}°')
        self.enviar_a_arduino(velocidad=vel, angulo_servo=angulo_servo)

    def detectarizquierda(self, msg, dt, vel):
        dist_obj = self.get_parameter('distancia_objetivo').value
        limite_ang = float(self.get_parameter('limite_angulo_max').value)

        distancias, angulos = self.obtener_puntos_sector(msg, 345, 15)
        if len(distancias) < 5:
            self.enviar_a_arduino(0, self.rec)
            return

        correccion, dist_pared, err_ang = self.calcular_pid_svd(
            distancias, angulos, dist_obj, limite_ang, dt, es_derecha=False
        )

        angulo_servo = self.rec + correccion
        angulo_servo = max(self.izquierda, min(self.derecha, angulo_servo))

        self.get_logger().info(f'[Seguir Izq] Dist: {dist_pared:.2f}m | Ang: {err_ang:+.1f}° | Servo: {angulo_servo}°')
        self.enviar_a_arduino(velocidad=vel, angulo_servo=angulo_servo)

    def calcular_pid_svd(self, distancias, angulos, dist_obj, limite_ang, dt, es_derecha):
        Kp_d = self.get_parameter('Kp_dist').value
        Kd_d = self.get_parameter('Kd_dist').value
        Ki_d = self.get_parameter('Ki_dist').value
        Kp_a = self.get_parameter('Kp_ang').value
        Kd_a = self.get_parameter('Kd_ang').value

        X = np.array([r * np.cos(a) for r, a in zip(distancias, angulos)])
        Y = np.array([r * np.sin(a) for r, a in zip(distancias, angulos)])

        X_mean, Y_mean = np.mean(X), np.mean(Y)
        X_c, Y_c = X - X_mean, Y - Y_mean
        _, _, Vh = np.linalg.svd(np.vstack([X_c, Y_c]).T)
        dir_x, dir_y = Vh[0]
        norm_x, norm_y = Vh[1]

        if dir_y < 0:
            dir_x, dir_y = -dir_x, -dir_y

        angulo_vector = np.degrees(np.arctan2(dir_y, dir_x))

        if es_derecha:
            error_angulo_real = 90.0 - angulo_vector
        else:
            error_angulo_real = angulo_vector - 90.0
            error_angulo_real = (error_angulo_real + 180) % 360 - 180

        distancia_pared = abs(X_mean * norm_x + Y_mean * norm_y)
        error_distancia = dist_obj - distancia_pared

        derivada_dist = (error_distancia - self.prev_error_dist) / dt
        self.integral_dist = max(-0.5, min(0.5, self.integral_dist + (error_distancia * dt)))
        salida_distancia = (Kp_d * error_distancia) + (Kd_d * derivada_dist) + (Ki_d * self.integral_dist)

        derivada_ang = (error_angulo_real - self.prev_error_ang) / dt
        salida_angulo = (Kp_a * error_angulo_real) + (Kd_a * derivada_ang)

        self.prev_error_dist = error_distancia
        self.prev_error_ang = error_angulo_real

        correccion_total = int(salida_distancia + salida_angulo)

        if error_angulo_real >= limite_ang and correccion_total < 0:
            correccion_total = 0
        elif error_angulo_real <= -limite_ang and correccion_total > 0:
            correccion_total = 0

        return correccion_total, distancia_pared, error_angulo_real

    def enviar_a_arduino(self, velocidad, angulo_servo):
        if self.arduino and self.arduino.is_open:
            try:
                self.arduino.write(f"M{velocidad}\n".encode('utf-8'))
                self.arduino.write(f"S{angulo_servo}\n".encode('utf-8'))
            except Exception as e:
                self.get_logger().error(f'Error de transmisión serial: {e}')

    def destroy_node(self):
        if self.arduino and self.arduino.is_open:
            self.enviar_a_arduino(0, self.rec)
            time.sleep(0.1)
            self.arduino.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    nodo = WroRetoAbierto()
    try:
        rclpy.spin(nodo)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            nodo.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
