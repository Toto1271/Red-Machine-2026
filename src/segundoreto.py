#!/usr/bin/env python3
import os
os.environ["QT_QPA_PLATFORM"] = "offscreen"

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, Image
import numpy as np
import serial
import time
from collections import Counter
import cv2
from cv_bridge import CvBridge

class WroRetoAbiertoConColor(Node):
    def __init__(self):
        super().__init__('wro_reto_abierto_con_color')

        # ============================================================
        # PARÁMETROS DE NAVEGACIÓN
        # ============================================================
        self.declare_parameter('sentido', 0)
        self.declare_parameter('distancia_objetivo_base', 0.4)
        self.declare_parameter('distancia_objetivo_rojo', 0.2)
        self.declare_parameter('distancia_objetivo_verde', 0.6)
        self.declare_parameter('distancia_frontal_obstaculo', 0.45)
        self.declare_parameter('velocidad_motor', 20)
        self.declare_parameter('limite_angulo_max', 38.0)
        self.declare_parameter('umbral_error_color', 5.0)

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

        # Control de giro normal (ya no se usa)
        self.girando = False
        self.tiempo_inicio_giro = 0.0
        self.TIEMPO_GIRO = 1.5

        # Finalización
        self.giros_completados = 0
        self.MAX_GIROS = 12
        self.finalizando = False
        self.tiempo_inicio_final = 0.0
        self.TIEMPO_AVANCE_FINAL = 4.0

        # ============================================================
        # MÁQUINA DE ESTADOS PARA MANIOBRA DE CRUCE
        # ============================================================
        self.cruce_activo = False
        self.cruce_fase = 0
        self.cruce_tiempo_inicio = 0.0
        self.cruce_vel = 0
        self.cruce_distancia_objetivo = self.get_parameter('distancia_objetivo_base').value

        # Último mensaje del LIDAR para usar en el cruce
        self.last_scan_msg = None

        # ============================================================
        # DETECCIÓN DE COLOR + FORMA
        # ============================================================
        self.bridge = CvBridge()
        self.frame_counter = 0
        self.process_every_n = 2

        self.declare_parameter('red_h_low1', 0)
        self.declare_parameter('red_h_high1', 7)
        self.declare_parameter('red_s_low1', 140)
        self.declare_parameter('red_s_high1', 255)
        self.declare_parameter('red_v_low1', 80)
        self.declare_parameter('red_v_high1', 255)

        self.declare_parameter('red_h_low2', 168)
        self.declare_parameter('red_h_high2', 180)
        self.declare_parameter('red_s_low2', 140)
        self.declare_parameter('red_s_high2', 255)
        self.declare_parameter('red_v_low2', 80)
        self.declare_parameter('red_v_high2', 255)

        self.declare_parameter('green_h_low', 40)
        self.declare_parameter('green_h_high', 85)
        self.declare_parameter('green_s_low', 170)
        self.declare_parameter('green_s_high', 255)
        self.declare_parameter('green_v_low', 70)
        self.declare_parameter('green_v_high', 255)

        self.declare_parameter('min_area', 300)
        self.declare_parameter('min_aspect_ratio', 1.2)
        self.declare_parameter('max_aspect_ratio', 4.0)

        self.ultimo_color = None
        self.error_angulo_actual = 0.0
        self.velocidad_actual = 0

        # ============================================================
        # CONEXIÓN CON ARDUINO
        # ============================================================
        self.puerto_serial = '/dev/ttyUSB0'
        self.baudrate = 115200
        try:
            self.arduino = serial.Serial(self.puerto_serial, self.baudrate, timeout=1)
            time.sleep(2)
            self.get_logger().info(f'✅ Conectado al Arduino en {self.puerto_serial}')
        except Exception as e:
            self.get_logger().error(f'❌ No se pudo conectar al Arduino: {e}')
            self.arduino = None

        # ============================================================
        # SUSCRIPCIONES
        # ============================================================
        self.subscription = self.create_subscription(
            LaserScan, '/scan', self.lidar_callback, 10
        )
        self.sub_image = self.create_subscription(
            Image, '/image_raw', self.image_callback, 10
        )

        self.get_logger().info('🚀 Nodo con CRUCE ESPECIAL (usando PID de navegación)')
        self.get_logger().info('📏 Cruce: retroceder 2s → girar 90° → retroceder a 5cm de pared (con PID) → avanzar')
        self.get_logger().info('🔴 ELIMINADO el giro normal a 0.45m')

    # ============================================================
    # REINICIO DE MEMORIA
    # ============================================================
    def reiniciar_memoria_color(self):
        self.ultimo_color = None
        self.get_logger().info('🔄 Memoria reiniciada (vuelve a 40 cm)')

    # ============================================================
    # FILTRO DE FORMA
    # ============================================================
    def filtrar_por_forma(self, mask):
        min_area = self.get_parameter('min_area').value
        min_aspect_ratio = self.get_parameter('min_aspect_ratio').value
        max_aspect_ratio = self.get_parameter('max_aspect_ratio').value

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos_validos = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < min_area:
                continue
            x, y, w, h = cv2.boundingRect(cnt)
            if w == 0:
                continue
            aspect_ratio = h / w
            if min_aspect_ratio <= aspect_ratio <= max_aspect_ratio:
                contornos_validos.append(cnt)
        return contornos_validos

    # ============================================================
    # CALLBACK DE CÁMARA
    # ============================================================
    def image_callback(self, msg):
        self.frame_counter += 1
        if self.frame_counter % self.process_every_n != 0:
            return

        umbral = self.get_parameter('umbral_error_color').value
        if abs(self.error_angulo_actual) > umbral:
            return

        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except Exception as e:
            self.get_logger().error(f'Error al convertir: {e}')
            return

        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        red_h_low1 = self.get_parameter('red_h_low1').value
        red_h_high1 = self.get_parameter('red_h_high1').value
        red_s_low1 = self.get_parameter('red_s_low1').value
        red_s_high1 = self.get_parameter('red_s_high1').value
        red_v_low1 = self.get_parameter('red_v_low1').value
        red_v_high1 = self.get_parameter('red_v_high1').value

        red_h_low2 = self.get_parameter('red_h_low2').value
        red_h_high2 = self.get_parameter('red_h_high2').value
        red_s_low2 = self.get_parameter('red_s_low2').value
        red_s_high2 = self.get_parameter('red_s_high2').value
        red_v_low2 = self.get_parameter('red_v_low2').value
        red_v_high2 = self.get_parameter('red_v_high2').value

        green_h_low = self.get_parameter('green_h_low').value
        green_h_high = self.get_parameter('green_h_high').value
        green_s_low = self.get_parameter('green_s_low').value
        green_s_high = self.get_parameter('green_s_high').value
        green_v_low = self.get_parameter('green_v_low').value
        green_v_high = self.get_parameter('green_v_high').value

        red_lower1 = np.array([red_h_low1, red_s_low1, red_v_low1])
        red_upper1 = np.array([red_h_high1, red_s_high1, red_v_high1])
        red_lower2 = np.array([red_h_low2, red_s_low2, red_v_low2])
        red_upper2 = np.array([red_h_high2, red_s_high2, red_v_high2])
        green_lower = np.array([green_h_low, green_s_low, green_v_low])
        green_upper = np.array([green_h_high, green_s_high, green_v_high])

        mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
        mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)
        mask_green = cv2.inRange(hsv, green_lower, green_upper)

        contornos_rojo = self.filtrar_por_forma(mask_red)
        contornos_verde = self.filtrar_por_forma(mask_green)

        red_pixels = sum(cv2.contourArea(c) for c in contornos_rojo)
        green_pixels = sum(cv2.contourArea(c) for c in contornos_verde)

        if red_pixels > 500 and green_pixels <= 500:
            self.ultimo_color = 'red'
            self.get_logger().info('🔴 ROJO válido → 20 cm')
        elif green_pixels > 500 and red_pixels <= 500:
            self.ultimo_color = 'green'
            self.get_logger().info('🟢 VERDE válido → 60 cm')
        else:
            if self.ultimo_color is not None:
                self.get_logger().info(f'⚪ Sin forma válida → manteniendo {self.ultimo_color.upper()}')

    # ============================================================
    # FUNCIONES DE NAVEGACIÓN (LIDAR + PID)
    # ============================================================
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
        moda = self.distancia_moda(distancias_raw)
        if moda == 999.0:
            return [], []
        umbral = max(0.1, 0.2 * moda)
        distancias_filtradas, angulos_filtrados = [], []
        for r, a in zip(distancias_raw, angulos_raw):
            if abs(r - moda) <= umbral:
                distancias_filtradas.append(r)
                angulos_filtrados.append(a)
        return distancias_filtradas, angulos_filtrados

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

    # ============================================================
    # FUNCIONES DE SEGUIMIENTO DE PARED (con velocidad y distancia personalizables)
    # ============================================================
    def detectarderecha_con_velocidad(self, msg, dt, vel, dist_obj):
        limite_ang = float(self.get_parameter('limite_angulo_max').value)
        distancias, angulos = self.obtener_puntos_sector(msg, 165, 195)
        if len(distancias) < 5:
            self.enviar_a_arduino(velocidad=vel, angulo_servo=self.rec)
            return
        correccion, dist_pared, err_ang = self.calcular_pid_svd(
            distancias, angulos, dist_obj, limite_ang, dt, es_derecha=True
        )
        self.error_angulo_actual = err_ang
        angulo_servo = self.rec - correccion
        angulo_servo = max(self.izquierda, min(self.derecha, angulo_servo))
        self.enviar_a_arduino(velocidad=vel, angulo_servo=angulo_servo)

    def detectarizquierda_con_velocidad(self, msg, dt, vel, dist_obj):
        limite_ang = float(self.get_parameter('limite_angulo_max').value)
        distancias, angulos = self.obtener_puntos_sector(msg, 345, 15)
        if len(distancias) < 5:
            self.enviar_a_arduino(velocidad=vel, angulo_servo=self.rec)
            return
        correccion, dist_pared, err_ang = self.calcular_pid_svd(
            distancias, angulos, dist_obj, limite_ang, dt, es_derecha=False
        )
        self.error_angulo_actual = err_ang
        angulo_servo = self.rec + correccion
        angulo_servo = max(self.izquierda, min(self.derecha, angulo_servo))
        self.enviar_a_arduino(velocidad=vel, angulo_servo=angulo_servo)

    def detectarderecha(self, msg, dt, vel, dist_obj):
        limite_ang = float(self.get_parameter('limite_angulo_max').value)
        distancias, angulos = self.obtener_puntos_sector(msg, 165, 195)
        if len(distancias) < 5:
            self.enviar_a_arduino(velocidad=vel, angulo_servo=self.rec)
            return
        correccion, dist_pared, err_ang = self.calcular_pid_svd(
            distancias, angulos, dist_obj, limite_ang, dt, es_derecha=True
        )
        self.error_angulo_actual = err_ang
        angulo_servo = self.rec - correccion
        angulo_servo = max(self.izquierda, min(self.derecha, angulo_servo))
        self.enviar_a_arduino(velocidad=vel, angulo_servo=angulo_servo)

    def detectarizquierda(self, msg, dt, vel, dist_obj):
        limite_ang = float(self.get_parameter('limite_angulo_max').value)
        distancias, angulos = self.obtener_puntos_sector(msg, 345, 15)
        if len(distancias) < 5:
            self.enviar_a_arduino(velocidad=vel, angulo_servo=self.rec)
            return
        correccion, dist_pared, err_ang = self.calcular_pid_svd(
            distancias, angulos, dist_obj, limite_ang, dt, es_derecha=False
        )
        self.error_angulo_actual = err_ang
        angulo_servo = self.rec + correccion
        angulo_servo = max(self.izquierda, min(self.derecha, angulo_servo))
        self.enviar_a_arduino(velocidad=vel, angulo_servo=angulo_servo)

    # ============================================================
    # ENVIAR COMANDOS AL ARDUINO
    # ============================================================
    def enviar_a_arduino(self, velocidad, angulo_servo):
        if self.arduino and self.arduino.is_open:
            try:
                self.arduino.write(f"M{velocidad}\n".encode('utf-8'))
                self.arduino.write(f"S{angulo_servo}\n".encode('utf-8'))
                self.velocidad_actual = velocidad
            except Exception as e:
                self.get_logger().error(f'Error de transmisión serial: {e}')

    # ============================================================
    # GIROS Y SENTIDO
    # ============================================================
    def giroizq90(self, vel):
        self.enviar_a_arduino(velocidad=vel, angulo_servo=self.izquierda)

    def giroder90(self, vel):
        self.enviar_a_arduino(velocidad=vel, angulo_servo=self.derecha)

    def detectarlado_en_pared(self):
        if self.dd < self.di:
            self.sentido = 2
        else:
            self.sentido = 1

    # ============================================================
    # MANIOBRA DE CRUCE
    # ============================================================
    def iniciar_cruce(self, vel):
        self.cruce_activo = True
        self.cruce_fase = 1
        self.cruce_tiempo_inicio = time.time()
        self.cruce_vel = vel
        self.get_logger().warn('🚦 INICIANDO MANIOBRA DE CRUCE')
        self.get_logger().info('⬅️ Fase 1: Retrocediendo 2 segundos...')
        self.enviar_a_arduino(velocidad=-100, angulo_servo=self.rec)

    def procesar_cruce(self):
        if not self.cruce_activo:
            return

        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.cruce_tiempo_inicio

        if self.cruce_fase == 1:
            if tiempo_transcurrido >= 2.0:
                self.cruce_fase = 2
                self.cruce_tiempo_inicio = tiempo_actual
                self.get_logger().info('🔄 Fase 2: Girando 90°...')
                if self.sentido == 1:
                    self.enviar_a_arduino(velocidad=self.cruce_vel, angulo_servo=self.izquierda)
                else:
                    self.enviar_a_arduino(velocidad=self.cruce_vel, angulo_servo=self.derecha)

        elif self.cruce_fase == 2:
            if tiempo_transcurrido >= self.TIEMPO_GIRO:
                self.cruce_fase = 3
                self.cruce_tiempo_inicio = tiempo_actual
                self.get_logger().info('📏 Fase 3: Retrocediendo con PID (5cm de pared)...')

        elif self.cruce_fase == 3:
            if self.last_scan_msg is None:
                return

            dt = 0.1
            if self.sentido == 1:
                self.detectarizquierda_con_velocidad(self.last_scan_msg, dt, -100, self.cruce_distancia_objetivo)
            else:
                self.detectarderecha_con_velocidad(self.last_scan_msg, dt, -100, self.cruce_distancia_objetivo)

            if int(tiempo_transcurrido) % 1 == 0 and tiempo_transcurrido > 0:
                self.get_logger().info(f'📏 Retrocediendo... ({tiempo_transcurrido:.1f}s)')

            if tiempo_transcurrido >= 5.0 or abs(self.error_angulo_actual) < 2.0:
                self.cruce_fase = 4
                self.cruce_tiempo_inicio = tiempo_actual
                self.get_logger().info('✅ Fase 4: Avanzando y reanudando...')
                self.enviar_a_arduino(velocidad=self.cruce_vel, angulo_servo=self.rec)

        elif self.cruce_fase == 4:
            if tiempo_transcurrido >= 1.0:
                self.cruce_activo = False
                self.cruce_fase = 0
                self.girando = False
                self.giros_completados += 1
                self.reiniciar_memoria_color()
                self.get_logger().info('✅ Maniobra de cruce COMPLETADA')

    # ============================================================
    # LIDAR CALLBACK
    # ============================================================
    def lidar_callback(self, msg):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        if dt <= 0:
            return

        self.last_scan_msg = msg
        self.detectardistancias(msg)

        if self.cruce_activo:
            self.procesar_cruce()
            return

        dist_obj_base = self.get_parameter('distancia_objetivo_base').value
        dist_obj_rojo = self.get_parameter('distancia_objetivo_rojo').value
        dist_obj_verde = self.get_parameter('distancia_objetivo_verde').value

        if self.ultimo_color == 'red':
            dist_obj = dist_obj_rojo
        elif self.ultimo_color == 'green':
            dist_obj = dist_obj_verde
        else:
            dist_obj = dist_obj_base

        dist_frontal_limite = self.get_parameter('distancia_frontal_obstaculo').value
        vel = int(self.get_parameter('velocidad_motor').value)

        if self.giros_completados >= self.MAX_GIROS and not self.finalizando:
            if not self.girando:
                self.finalizando = True
                self.tiempo_inicio_final = current_time.nanoseconds / 1e9
                self.get_logger().info('🚀 Avance final...')

        if self.finalizando:
            tiempo_transcurrido = (current_time.nanoseconds / 1e9) - self.tiempo_inicio_final
            if tiempo_transcurrido >= self.TIEMPO_AVANCE_FINAL:
                self.get_logger().info('🛑 12 vueltas completadas. Deteniendo robot.')
                self.enviar_a_arduino(0, self.rec)
                self.destroy_node()
                rclpy.shutdown()
                return

        if self.d < dist_frontal_limite and self.d > 0:
            if self.sentido == 0:
                self.detectarlado_en_pared()

            if not self.girando and not self.finalizando and not self.cruce_activo:
                self.iniciar_cruce(vel)
                return

        if self.girando and not self.finalizando:
            tiempo_actual = current_time.nanoseconds / 1e9
            if tiempo_actual - self.tiempo_inicio_giro > self.TIEMPO_GIRO:
                self.girando = False
                self.enviar_a_arduino(0, self.rec)
                self.get_logger().info('✅ Giro completado.')
                self.reiniciar_memoria_color()

        if not self.girando:
            if self.sentido == 0:
                self.enviar_a_arduino(vel, self.rec)
            elif self.sentido == 1:
                self.detectarizquierda(msg, dt, vel, dist_obj)
            elif self.sentido == 2:
                self.detectarderecha(msg, dt, vel, dist_obj)

def main(args=None):
    rclpy.init(args=args)
    nodo = WroRetoAbiertoConColor()
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
