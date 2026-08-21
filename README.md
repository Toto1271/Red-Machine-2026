

# Engineering Document / Red Machine

Este repositorio muestra todos los componentes para construir a "pompo", este robot autonomo pertenece al equipo "Red Machine" y cumple el proposito de participar en la categoria de futuros ingenieros en la WRO 2026.

![Image](https://github.com/user-attachments/assets/1cbe6250-ba27-41c2-bb0b-d5abe1c41ac8)


# INDEX - REDMACHINE 2025

## 📌 MAIN CONTENT
1. [Engineering Document / Red Machine](#Engineering-Document--red-machine)
2. [Red-Machine-Members](https://github.com/Samu4035/REDMACHINE-2025/tree/main?tab=readme-ov-file#Red-Machine-Members)
   - [Juan Diego Cano Barros](#-juan-diego-cano-barros)
   - [Samuel José Galban Franco](#-samuel-josé-galban-franco)
   - [Angel Saúl Rodriguez Guerra](#-angel-saúl-rodriguez-guerra)
3. [Development Stages (Previous robot versions)](https://github.com/Samu4035/REDMACHINE-2025/tree/main?tab=readme-ov-file#Development-stages-Previous-robot-versions)
4. [Robot Photos](#Robot-Photos-All-Angles)
5. [Mechanical desing](#Mechanical-Design)
   - [Mechanical Assembly Guide](#-Mechanical-Assembly-Guide--red-machine)
   - [General Structure](#-General-Structure)
   - [Drive and Steering Module](#-Drive-and-Steering-Module--red-machine)
6. [Electronic Components](#Electronic-Components)
   - [Description of Main System Components](#-Description-of-Main-System-Components)
7. [Robot Power Supply](#Robot-Power-Supply)
   - [Consumption calculation](#-Total-Energy-Consumption-Calculation)
8. [Image Processing](#Image-Processing)
   - [Color Detection](#Color-Detection)
9. [How to Run or Test the Project ](#How-to-Run-or-Test-the-Project)
10. [Second Challenge Code](https://github.com/Samu4035/REDMACHINE-2025/tree/main?tab=readme-ov-file#Second-Challenge-Code)
11. [First Challenge Explination](#First-Challenge-Explination)
12. [Videos](https://github.com/Samu4035/REDMACHINE-2025/tree/main?tab=readme-ov-file#Videos-of-Pompo-Operation--Version-3.0-Contemporary-Videos)
   - [Future Engineers - Challenge 1 Variant 1](https://youtu.be/I5WXGXlZpG4?si=D2IsjQdoafDccQmA)
   - [Future Engineers - Challenge 1 Variant 2](https://youtu.be/rjQujXqtAJU?feature=shared)
   - [Future Engineers - Challenge 1 Variant 3](https://youtu.be/9T3Q66ES2Qw?feature=shared)
   - [Future Engineers - Challenge 1 Variant 4](https://youtu.be/tL3BE26AJaA?feature=shared)
   - [Future Engineers-Reto 2](https://youtu.be/XvPb05R_A2o?si=kEyuvRi_PKU7EDct)
13. [Videos of Past Tests](https://github.com/Samu4035/REDMACHINE-2025/tree/main?tab=readme-ov-file#Videos-of-Past-Tests)
14. [Troubleshooting](#troubleshooting)
15. [History and Timeline](#History-and-Timeline-of-Red-Machine)
    - [2023 Season](#2023-Season)
    - [2024 Season](#2024-Season)
    - [2025 Season](#2025-Season)
    - [Robots Evolution](#julian-luka-and-pompo)

## 📂 REPOSITORY STRUCTURE
- [t-photos/](https://github.com/Samu4035/REDMACHINE-2025/tree/main/t-photos) - Team photos
- [v-photos/](https://github.com/Samu4035/REDMACHINE-2025/tree/main/v-photos) - Vehicle photos
- [schemes/](https://github.com/Samu4035/REDMACHINE-2025/tree/main/schemes) - Eschematic diagrams
- [src/](https://github.com/Samu4035/REDMACHINE-2025/tree/main/src) - Code
- [models/](https://github.com/Samu4035/REDMACHINE-2025/tree/main/models) - 3D Designs
- [otros/](https://github.com/Samu4035/REDMACHINE-2025/tree/main/otros) - Other archives

# Repository contents

This repository contains the following directories to organize our project:

* `t-photos`: Includes team photos, as well as photos of the work done during all competition years and photos of the robots built by the team.
* `v-photos`: Contains 6 photos of the vehicle (from all angles).
* `schemes`: Schematic diagrams (JPEG, PNG or PDF) of the electromechanical components, illustrating the wiring of electronic elements and motors, plus an explanation of the function of each.
* `src`: Control software code for all components programmed for the competition.
* `models`: Files for the vehicle's 3D design.
* `other`: Additional files to understand how to prepare the vehicle for the competition.
     
# Introduction
The team has put their greatest effort into building the best possible robot. Our preparation for these olympiads has been based on extensive learning in construction, design and programming, and the experience from previous competitions has been fundamental. Long hours of track analysis and study have led to the creation of our own strategy, based on the components the team chose to work with, aiming for the best possible performance in the various stages of this competition.
Throughout this document and the entire repository, all the design, programming and construction work of the robot is explained precisely.

# Red Machine Members


## 👤 Juan Diego Cano Barros

### Role in the team
Responsible for the robot programming.

### 🧠 Academic Achievements

- 🥉 **Bronze Medal – Ibero-American Mathematics Olympiad (2023)**
He represented Venezuela in the 29th edition of this international competition organized by the OMA in Argentina, after being selected as one of the top 10 of the second national level by @acmvenojm.

- 🥈 **Runner-up – Argentine Mathematics Olympiad Ñandú (2019)**
Participated in the oral exam in Buenos Aires, standing out as the runner-up in Level 1.

---

### Robotics Background

- 🇻🇪 **Two-time National Champion – Futuros Ingenieros Category (WRO Venezuela)**
Winner of the National Robotics Olympiad in two consecutive editions, representing Zulia state and qualifying for the international finals.

- 🌍 **International Finalist – WRO Panama 2023**
Represented Venezuela at the World Robotics Olympiad, placing 25th out of 40 teams in the Futuros Ingenieros category.

- 🇹🇷 **International Participation – WRO Turkey 2024**
Was part of the Venezuelan delegation that competed at the world edition held in Turkey, consolidating experience in high-level global events.

---

### 💡 Motivation and Focus
Eat, Sleep, Meet People, Enjoy Trips, and Sleep

## 👤 Samuel José Galban Franco

### Role in the team
Responsible for the robot's electronics.

### 🧠 Academic Achievements

- 🥈 **Runner-up – National Chemistry Olympiad (2024)**
Represented Liceo Los Robles in the most recent edition of this competition organized by AVOQUIM.

- 🥈 **Runner-up – VIRTUAL MISSIONS PANAMA 2023 CHALLENGE**
Second place in this international competition, representing Venezuela during the WRO 2023 international final held in Panama.

---

### 🤖 Robotics Background

- 🇻🇪 **Two-time National Champion – Futuros Ingenieros Category (WRO Venezuela)**
Winner of the National Robotics Olympiad in two consecutive editions, representing Zulia state and qualifying for the international finals.

- 🌍 **International Finalist – WRO Panama 2023**
Represented Venezuela at the World Robotics Olympiad, placing 25th out of 40 teams in the Futuros Ingenieros category.

- 🇹🇷 **International Participation – WRO Turkey 2024**
Was part of the Venezuelan delegation that competed at the world edition held in Turkey, gaining technical and cultural experience in high-level competitive environments.

---

### 💡 Motivation and Focus
Meet people, enjoy trips, and look for study opportunities



## 👤 Angel Saúl Rodriguez Guerra

### Role in the team
Responsible for the robot's mechanics.

### 🧠 Academic Achievements
- 🥇 **Qualified for the World – World Youth Mathematics Olympiad (WYMO) (2024)**
He represented Venezuela at the World Youth Mathematics Olympiad, an international competition that brings together young mathematical talents from around the world to tackle highly challenging problems.

- 🔬 **Notable Participant – Chemistry and Mathematics Olympiads in Venezuela**
Competed in various editions of the Venezuelan Olympiads, demonstrating excellence and passion for the exact sciences from an early age.

--- 

### 🤖 Robotics Background
- 🇻🇪 **Two-time National Champion – Futuros Ingenieros Category (WRO Venezuela)**
Winner in two consecutive editions of the National Robotics Olympiad, representing Zulia state and earning selection for international competitions as part of the national delegation.

- 🌍 **International Finalist – WRO Panama 2023**
Participated in the World Robotics Olympiad held in Panama, placing 25th among 40 international teams in the Futuros Ingenieros category.

- 🇹🇷 **International Participation – WRO Turkey 2024**
Member of the Venezuelan delegation that competed in the world edition held in Turkey, accumulating technical and cultural experience in high-level competitive settings.

--- 

### 💡 Motivation and Focus
Passionate about continuous learning, creative problem solving, and collaborating in multidisciplinary teams. His track record in academic and technological competitions reflects a genuine motivation to create impact through knowledge and to keep exploring new frontiers of scientific thought and innovation.

---

![Image](https://github.com/user-attachments/assets/b1555ddb-f7c7-47b6-b690-13382831a981)




# Explicación Detallada de los Componentes

### Raspberry Pi 5
Computadora monoplaca de alto rendimiento equipada con un procesador Broadcom BCM2711 Quad-Core ARM Cortex-A72 a 1.5 GHz. Funciona como la unidad central de cómputo del robot, asumiendo el procesamiento pesado de imágenes capturadas por la webcam y la gestión de la nube de puntos transmitida por el Lidar ST27L. Su arquitectura ARM de 64 bits y su memoria RAM permiten ejecutar la pila del sistema operativo Linux (UBUNTU) e hilos paralelos mediante Python, garantizando que el procesamiento visual intensivo y la construcción del mapa espacial no generen cuellos de botella ni bloqueen las respuestas dinámicas del vehículo en la pista. Fue especificamente utilizada por encima de la raspberry pi 4, ya que completa cada iteracion del codigo un 13% mas rapido, ofreciendo aun mas precision, siendo muy relevante para el uso del lidar.

*(Espacio para foto de la Raspberry Pi 4)*

---

### Arduino Uno
Microcontrolador de 8 bits basado en el chip ATmega328P que opera a una frecuencia de reloj de 16 MHz. Dentro de la arquitectura del robot, se desempeña como el nodo de control en tiempo real dedicado a la ejecución de tareas críticas de bajo nivel. Recibe las directivas de movimiento enviadas desde la Raspberry Pi y genera las señales PWM hacia el driver de motores TB6612FNG y al servomotor. Al delegar la temporización estricta de las salidas lógicas a este microcontrolador, se evita que las interrupciones del sistema operativo de la Raspberry Pi causen fluctuaciones en la velocidad de las ruedas o imperfecciones en la respuesta de los actuadores. El arduino uno fue utilizado principalmente para facilitar la construccion de este chasis, debido a que otro tipo de microcontroladores son mucho mas dificiles de encontrar por lo tanto dificultarian poder replicar el chasis.

*(Espacio para foto del Arduino Uno)*

---

### Lidar LDROBOT ST27L
Sensor óptico de medición de distancia omnidireccional basado en la tecnología dToF (Direct Time-of-Flight), capaz de realizar escaneos de 360° en el plano horizontal a rangos de hasta 25 metros. Emite pulsos de luz láser infrarroja y mide el tiempo exacto que tardan en rebotar contra los obstáculos, generando una matriz de coordenadas espaciales en tiempo real. Esta información es fundamental para los algoritmos de navegación y evasión de paredes, ofreciendo una inmunidad total ante cambios bruscos de iluminación ambiental, sombras sobre la pista o variaciones en el color de la superficie de los muros. Se utiliza el lidar en contraste a los ultrasonidos para obtener una precision ~99.1%, debido a que trabajamos con mayor cantidad de datos, donde somos capaces de trazar una recta que se asemeja a la de las paredes en un 93,4%, lo cual asegura que la raspberry pi no confunda las paredes de la pista con cualquier otro obstaculo de la pista, tales como los conos o los estacionamientos.

*(Espacio para foto del Lidar LDROBOT ST27L)*

---

### Servomotor REV Robotics
Actuador de dirección de grado robótico con piñonería interna metálica de alta resistencia y motor integrado de corriente continua, optimizado para operar a 6.0 V con un torque de hasta 13.5 kg-cm. Su función principal es posicionar el mecanismo del tren delantero para cambiar la trayectoria del vehículo. Su electrónica digital interna ajusta la posición del eje con alta precisión angular, manteniendo el ángulo de dirección fijo sin ceder ante las fuerzas de fricción de las ruedas sobre la pista o las inercias generadas durante cambios de dirección a alta velocidad.

*(Espacio para foto del Servomotor REV Robotics)*

---

### Driver TB6612FNG (Puente H Dual)
Módulo controlador de motores basado en una etapa de potencia MOSFET de baja resistencia interna en estado activo (Rds(on)). Permite manejar dos motores DC en paralelo con una corriente continua de hasta 1.2 A por canal (3.2 A pico). Al utilizar transistores MOSFET en lugar de los antiguos transistores bipolares, ofrece una eficiencia energética superior con una disipación de calor mínima, respondiendo de forma lineal a las señales de ciclo de trabajo PWM de hasta 100 kHz enviadas por el Arduino Uno para regular aceleraciones y frenados. Fue un cambio al antiguo puente h l298n, debido a que este nos ofrece mas eficiencia, en un espacio muchisimo menor, permitiendonos hacer todos los cambios fisicos exigidos.

*(Espacio para foto del Puente H TB6612FNG)*

---

### Cámara Webcam
Sensor de captura de imagen HD conectado vía USB a la Raspberry Pi, dedicado a la adquisición de cuadros de video en tiempo real. Proporciona el flujo de datos visuales necesario para que los algoritmos de visión artificial procesen el entorno, detecten patrones cromáticos, identifiquen señales de tráfico y reconozcan elementos clave del circuito. Su integración directa al bus USB 3.0 de la Raspberry Pi permite la transmisión fluida de imágenes sin sobrecargar el bus de comunicación serie del microcontrolador de bajo nivel.

*(Espacio para foto de la Webcam)*

---

### Banco de Baterías 18650 (Arreglo 2S2P)
Fuente de alimentación principal conformada por cuatro celdas cilíndricas recargables de Ion de Litio (Li-ion) formato 18650, configuradas en dos ramas en paralelo de dos celdas en serie cada una. Entrega una tensión nominal de 7.4 V (8.4 V a plena carga) y una capacidad acumulada de 4000 mAh. Esta química de batería ofrece una resistencia interna extremadamente baja, lo que permite suministrar ráfagas elevadas de corriente sin sufrir caídas parásitas de voltaje (*brownouts*) cuando los motores de tracción y el servo de dirección demandan torque máximo en momentos de alta aceleración.

*(Espacio para foto del paquete de baterías 18650)*

---

### Reductor de Voltaje XL4015 (Step-Down 5 A)
Convertidor conmutado de corriente continua (*Buck Converter*) capaz de transformar el voltaje variable del banco de baterías (7.4 V – 8.4 V) en una línea regulada estable de 5.0 V DC con capacidad de suministro de hasta 5 A. Su frecuencia de conmutación interna y su alto rendimiento energético (hasta el 96%) evitan el desperdicio de energía en forma de calor residual, suministrando una alimentación limpia e inmune a ruidos electromagnéticos a la Raspberry Pi, la cual a su vez energiza la webcam, el Lidar ST27L y el Arduino Uno. Este componente es estrictamente necesario, debido a que la mayoria de reductores de voltaje de bajo costo suministran una cantidad menor a 4A, lo cual es necesario para el correcto funcionamiento de la raspberry pi, y por lo tanto de sus componentes adyacentes

*(Espacio para foto del regulador XL4015)*

---

### Reductor de Voltaje LM2596 (Step-Down 3 A)
Regulador conmutado independiente que opera a una frecuencia de 150 kHz, dedicado a transformar la tensión de las baterías en una salida fija de 6.0 V DC para la etapa de dirección. Al estar aislado de la línea de 5.0 V de la computadora principal, absorbe los picos térmicos y electromagnéticos que genera el servomotor REV Robotics durante sus movimientos bruscos, previniendo que el ruido inductivo del motor o los bajones de tensión repentinos causen reinicios imprevistos en la Raspberry Pi o fallas de sincronía en el Lidar.

*(Espacio para foto del regulador LM2596)*

---

# Alimentación del Robot

El sistema de energía del robot está estructurado mediante dos reguladores *step-down* conectados al paquete principal de baterías:

- **Línea de Cómputo y Percepción:** El regulador XL4015 reduce el voltaje de las baterías a 5 V estables para alimentar la Raspberry Pi. Esta, a su vez, distribuye energía al Arduino Uno, al Lidar LDROBOT ST27L y a la webcam a través de sus puertos USB e interfaces de alimentación.
- **Línea de Actuación (Servo):** El regulador LM2596 ajusta la tensión a 6 V para alimentar de forma dedicada el servomotor REV Robotics, aislando sus picos de corriente del resto del circuito lógico.
- **Línea de Tracción:** Las baterías alimentan directamente la entrada de potencia del puente H TB6612FNG, el cual distribuye la energía a ambos motores de tracción conectados en paralelo.

---

### 🔋 Cálculo del Consumo Total de Energía

| Componente | Cantidad | Consumo estimado (mA) | Total (mA) |
|:---|:---:|:---:|:---:|
| Raspberry Pi (con Webcam) | 1 | 1200 mA | 1200 mA |
| Lidar LDROBOT ST27L | 1 | 350 mA | 350 mA |
| Arduino Uno | 1 | 50 mA | 50 mA |
| Servomotor REV Robotics | 1 | 180 mA (típico) | 180 mA |
| Motores de Tracción (en paralelo) | 2 | 500 mA c/u | 1000 mA |
| **TOTAL** | — | — | **2780 mA** |

---

### ⚡ Distribución de Potencia y Autonomía Estimada

El sistema se alimenta de forma distribuida para optimizar la eficiencia y proteger los componentes sensibles contra ruido inductivo:

- 🔌 **Línea Regulada XL4015 (5V):** Raspberry Pi, Webcam, Lidar ST27L y Arduino Uno.
- 🔌 **Línea Regulada LM2596 (6V):** Servomotor REV Robotics.
- 🔋 **Alimentación Directa a Puente H TB6612FNG:** Motores de tracción conectados en paralelo.

| Fuente de Alimentación | Componentes Alimentados | Consumo Estimado (mA) | Capacidad Aprox. |
|:---|:---|:---:|:---:|
| Regulador XL4015 (Salida 5V) | Raspberry Pi, Webcam, Lidar, Arduino | ~1600 mA | 4000 mAh |
| Regulador LM2596 (Salida 6V) | Servomotor REV Robotics | ~180 mA | 4000 mAh |
| Puente H TB6612FNG (Directo) | Motores de Tracción (en paralelo) | ~1000 mA | 4000 mAh |

> 💡 *Nota:*  Al momento de utilizarlos todos en conjunto tienen una autonomia estimada de 1.2 horas de forma eficiente
> 

# Buenas Prácticas de Cableado, Eficiencia y Seguridad

* **Estandarización de colores por función:** Se utilizó el mismo color de cable para cada tipo de línea en todo el robot (rojo para positivo, negro para tierra, azul para señales PWM, amarillo/verde para comunicación). Esto evita confusiones durante las reparaciones y previene conexiones cruzadas accidentales. En competencias pasadas esto no era un estandar, lo que generaba confusiones al momento de la reparacion

* **Separación física de cables de energía y datos:** Se pasaron los cables gruesos que llevan energía a los motores por un lado del chasis y los cables delgados que llevan información a la Raspberry Pi, Lidar y Arduino por el otro. Mantenerlos alejados evita que la fuerza de los motores cause interferencias en las lecturas de los sensores.

* **Trenzado de cables de alimentación:** Los cables de corriente (positivo y negativo) que van hacia los motores y los reguladores se enrollaron juntos en pares trenzados. Esta forma de enroscarlos ayuda a cancelar de forma natural el ruido magnético que generan sobre el resto de la electrónica. De igualmente facilitan solucionar cualquier error, ya que hay mucho menor volumen de cables

* **Uso de tubos termorretráctiles (Thermoshrink) en las soldaduras:** Cada unión soldada se cubrió con tubo termorretráctil en lugar de usar cinta aislante. Esto garantiza que las soldaduras no queden expuestas, evitando cortocircuitos por contacto accidental con el chasis u otros componentes.

* **Agrupado con precintos y fundas espirales:** Se utilizaron precintos plásticos y fundas para juntar los cables en ramas ordenadas. Esto evita que queden cables sueltos que puedan engancharse con las ruedas, el servomotor o con elementos externos de la pista mientras el robot se desplaza.

* **Alivio de tensión en zonas con movimiento:** En los cables que van conectados a partes móviles, como el servomotor de la dirección, se dejó una ligera curvatura de margen y se sujetó el cable al chasis justo antes del conector. Así, el tirón del movimiento lo absorbe la estructura del robot y no los pines del componente.



# Videos of Past Tests

## Version 1.0 Robot Videos
### First challenge
[<img width="926" height="515" alt="image" src="https://github.com/user-attachments/assets/bcca2144-03be-48d7-a760-bc5364874bd4" />](https://youtu.be/W26b5g69BQQ?si=Y7qg7TaV6iR0McLb)

### Second challenge test
[<img width="453" height="583" alt="image" src="https://github.com/user-attachments/assets/5d6ff46e-4ade-4e43-bef0-940c5f0850ff" />](https://youtube.com/shorts/cc8yKOo6g8U?si=XeC0w1IYvneSmaU0)



## Version 2.0 Robot Videos

### Complete Challenge 1 Video, All Variants
[<img width="336" height="188" alt="image" src="https://github.com/user-attachments/assets/dfae6ff3-cb71-4b5f-9016-ae2efeb6b23f" />
](https://www.youtube.com/watch?v=HS7eLoFSOkU)

### Complete Challenge 2 Video
[<img width="336" height="188" alt="image" src="https://github.com/user-attachments/assets/5868e78c-5e65-40ab-8b85-4ca204db4f23" />
](https://www.youtube.com/watch?v=cjjnRDXaDAU&t=56s)

## Robot videos
### Color Detection Demonstration
[<img width="270" height="480" alt="image" src="https://github.com/user-attachments/assets/b3d6a860-b0d2-4d91-bf3d-b9a8c1924240" />
](https://www.youtube.com/shorts/HLt_O2JlURQ)

### Continuity Test
[<img width="270" height="480" alt="image" src="https://github.com/user-attachments/assets/dd85f7af-9fe4-475b-be93-eda2947dddbc" />](https://www.youtube.com/shorts/jUmZjaQ_be8)

## Videos about Red Machine
### National Presentation 2023
[<img width="336" height="188" alt="image" src="https://github.com/user-attachments/assets/00664584-bacb-41d2-8210-cb014d690640" />](https://www.youtube.com/watch?v=fVg6WCavaBU)
### Red Machine National 2023
[<img width="336" height="188" alt="image" src="https://github.com/user-attachments/assets/525ffe10-d1de-4dda-a9da-bc815b110c35" />](https://www.youtube.com/watch?v=FSo2NadI6ec&pp=0gcJCbIJAYcqIYzv)
### Red Machine Team Presentation
[<img width="320" height="180" alt="image" src="https://github.com/user-attachments/assets/f27d65da-cd69-4e9f-b46f-22959dfdb275" />](https://www.youtube.com/watch?v=EYFYI9Z96V4&t=25s)
### Educational Robotics
[<img width="320" height="180" alt="image" src="https://github.com/user-attachments/assets/2ca73ef3-91ca-4155-91c7-0617813404df" />](https://www.youtube.com/watch?v=Is-765hQCRY)








# History and Timeline of Red Machine

1. 2023 Season
- [Julio 2023](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Julio-2023)
- [Agosto 2023](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Agosto-2023)
- [Septiembre 2023](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Septiembre-2023)
- [Octubre 2023](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Octubre-2023)
2. 2024 Season
- [Febrero 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Febrero-2024)
- [Marzo 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Marzo-2024)
- [Abril 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Abril-2024)
- [Mayo 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Mayo-2024)
- [Junio 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Junio-2024)
- [Octubre 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Octubre-2024)
- [Noviembre 2024](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Noviembre-2024)
3. 2025 Season
- [Febrero 2025](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Febrero-2025)
- [Marzo 2025](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Marzo-2025)
- [Abril 2025](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Abril-2025)
- [Mayo 2025](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#Mayo-2025)
4. Julian, Luka and Pompo
- [JULIAN 1.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#JULIAN-1.0)
- [JULIAN 2.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#JULIAN-2.0)
- [JULIAN 3.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#JULIAN-3.0)
- [JULIAN 4.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#JULIAN-4.0)
- [JULIAN 5.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#JULIAN-5.0)
- [LUKA 1.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#LUKA-1.0)

- [LUKA 2.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md)

- [LUKA 3.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#LUKA-3.0)

- [POMPO 1.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#POMPO-1.0)

- [POMPO 2.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#POMPO-2.0)

- [POMPO 3.0](https://github.com/Samu4035/REDMACHINE-2025/blob/main/t-photos/Historia.md#POMPO-3.0)

    
## 2023 Season

### July 2023

After participating in a regional robotics competition, the team decided to take part in the WRO, specifically in the Future Engineers category. As a first step, the team began studying and analyzing the competition rules.

![1ra julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/66f7c8f1-b10c-4261-86b3-32c87bcd3b81)

In the following days, the team began studying what could be the first version of the chassis and investigated various ways to address the initial challenges, which were how to design the steering system and which motor to use to achieve the required speed and torque.

![2da julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/3c73dc50-b3c4-4f2d-a4ad-92f87ee21a87)

Next, the team began searching for motors that could be used, disassembling toys, printers, and other devices, ultimately obtaining the necessary motor by dismantling a Nikko Dodge T-rex Ram remote-controlled car, which provided the mechanical parts needed to design the steering system.

![3rajulio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/dbdfbd4e-9594-40f0-b34e-6d0528d7b328) 

![4julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/32158385-5185-4d74-b19a-fd5dca851590)

Subsequently, the team proceeded to assemble both systems, along with the various devices the robot would need, onto acrylic bases, completing the first prototype of what would become the chassis and allowing them to move forward with the programming phase.

![5julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/5d1d2414-1c38-4973-b7b8-8c7c55b3b648)

For programming, an Arduino Mega 2560 was used as the controller, a dual H-bridge as a power and speed regulator, and an ultrasonic sensor to measure distance. Subsequently, the team resumed searching for solutions to detect traffic light colors, deciding to use an ESP32-CAM with an OV2640 lens, with the next challenge being how to program it with Arduino.

![6julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/eb1e7891-75de-4a19-87ab-400c2de48bbc)

The team investigated which power source to use for the robot, since after using 9V batteries, they realized these were not ideal as they depleted very quickly. Consequently, two battery packs were connected, each containing eight 1.2V rechargeable cells in series, ultimately providing a total of 9.6V.

Due to space requirements, a second prototype was designed, adding a second level to the robot. The electronics were placed on the upper level, while the first level housed the batteries, the traction system, and the steering system.
![7julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/aa52095a-ea01-412f-901e-da4eb791124c)

Without being able to solve the programming yet, it was decided to use an RGB 34725 sensor so that the robot could detect which direction it should cross.

![8julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/e1047aac-374b-4cdb-8531-4b916cac0f36)

A strategy was proposed: it was decided to cross by detecting the color of the track lines, also using two additional ultrasonic sensors, one on each side of the robot, so that once it detected a wall, it could cross to avoid a collision. However, these two ultrasonic sensors ended up being more of a problem than a help, because when they detected something, the robot lost its trajectory. Consequently, it was ultimately decided not to use these two ultrasonic sensors.

![9julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/c96458f7-a354-4cbc-b139-bbab67d7a71c)

Before the competition, the team found rechargeable batteries with a higher voltage (3.7 V), so it was decided to remove one of the two battery packs and modify the remaining pack to operate with 3 batteries.

![10julio](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/cab0ff29-43a8-4808-9a1b-f93d4ca45027)

### August 2023

After participating in the first regional competition, the team began seeking solutions to the problems encountered. It was decided to change the steering system, creating a new one using parts from a Spike Prime robotics kit, number 45678, since this new steering system would allow a larger turning radius as well as more precise turns.

![1ago](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/2e470dc5-3636-41a1-9733-a62f20ae0db0)

New strategies were proposed, for which it was decided that the ideal way to cross would be with the help of ultrasonic sensors, and that the TCS34725 sensor would only detect the first line to determine whether the robot should cross clockwise or counterclockwise.

Continuing with the second part of the challenge, the team began programming the camera, looking for a way to transfer the camera’s information to the Arduino without using Wi-Fi. After researching several sources, they found a solution: transmitting the data through serial ports.

Then, the motor used during all this time began to fail frequently, preventing the team from progressing in the second challenge. A few days before the competition, the team extracted the motor—and consequently the gearbox—from another remote-controlled car to integrate it into the robot.

![2ago](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/6dbc1ef9-7d96-4ca5-839e-63c8bb6c3e24)

To provide a larger turning radius, the steering system was modified using pieces from a Lego Spike Prime kit.

![3ago](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/528c8a5c-2b6b-4996-9143-c09bb9472b1b)

### September 2023

Practice sessions were conducted on the track to improve the robot’s performance in challenges one and two, aiming for the best results in the 2023 national championship. The report was drafted and updated based on the progress achieved so far, followed by additional track practice to further enhance the robot’s performance in challenges one and two for the 2023 national championship.

![4ago](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/e132722b-7d13-4236-8e9b-7d837b6f065d) ![5 ago](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/eb82c5c2-2d85-4bf3-a0a5-0326dc07f3d5)

The time has come for the national competition, where the team successfully achieved the goal of qualifying for the 2023 WRO World Cup in Panama.

![sep2](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/41c23672-ecf9-4970-a691-882c736f0801)![sep1](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/454f09af-68c2-41fe-842e-51191bca02c3)
 

### October 2023

Work continued on programming the camera for Challenge 2. The wheels of the steering system were changed to improve safety and aesthetics, and the construction of the third prototype of the robot began, focusing on restoring the acrylic parts and organizing the cables through connectors to enhance the robot’s overall appearance.

![sep3](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/38c0d5d6-7739-47c4-ac14-718439dbf9c6)

The time for the World Cup arrives, where the team ranked among the top 25 in the world and within the top 2 among Latin American countries.

![oc1](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/d7f5104d-0fcb-45c1-b448-8e1b9b5449bd)![oct2](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/93173685-2fc5-4110-bf5e-b1adf484abe1)

## 2024 season

### February 2024

The first thing the team did to start this season was study the new rulebook, to identify the differences in the challenge and consider possible strategies for the new year.

![febrero 1](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/543ccce4-e258-4f4d-ab56-94f6a3207c77)

The team began designing the new robot, taking into account everything they had learned at the World Cup. During this design phase, aspects such as size, weight, which components would be used, their placement, and the distance between the traction and steering systems were considered.

![feb2](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/e518fc97-dbcd-4631-86c7-ceff1295411f)

The team continued planning which strategy to use. To avoid revealing the improvements and advancements planned for the new robot, they decided it would be best to compete with Julián (the 2023 robot) during the regional competitions and use the new robot (Luka) in the national competition, which would be the biggest challenge at the time.

![feb3](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/c918252f-6495-4227-b0c1-6020686d0f09)

### March 2024

During this month, the construction of the robot for the 2024 national competition began. In the first week of March, the acrylic bases were cut and the missing components for the robot were purchased.
First, the traction system and the steering system were installed on the robot. At this stage, the steering system was built using three acrylic pieces. Afterward, the Arduino and the Raspberry Pi were installed.

![feb4](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/23bb3e40-7f24-499d-9f17-81d077cd7c80)![feb5](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/bf47b801-3b39-4c64-8e48-dd82d7b7f9e9)

At the end of March, the construction of the robot was completed after installing all the sensors it would use. Additionally, programming for Challenge 1 was started, along with Python programming for Challenge 2.

![feb6](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/ba34c027-6287-45b2-a1b7-981fea57a367)

### April 2024

Since the team decided to participate with Julián in the regional competitions, work began on some improvements to the robot’s performance. One of these improvements was replacing the 34725 RGB sensor with the TCS3200 color sensor.

![feb7](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/48b506e4-a226-4501-9297-ab61940ddbd8)

In preparation for the upcoming regional competition, the report was updated according to the work completed so far. The most important updates included the timeline, the wiring diagram, and the specifications of the color sensor.

![feb8](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/e74d6b44-9a5a-4ff3-aa44-223e3d5b8257)

2024 Regional Competitions:

Colegio Santo Tomás de Aquino 05-04-2024
![feb9](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/0569d301-fa0c-444f-8521-f688f98e4dcd)

### May 2024
Liceo Los Robles 05-18-2024
![feb10](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/da1b210c-ddeb-4e1a-85d9-211e8c0ffc5c)


### June 2024

In preparation for the national competition, the team continued testing both challenges, focusing primarily on the second one; at the same time, they worked on Luka's report.
During the tests, it was decided to remove the color sensor, as it was not functioning optimally, and the side ultrasonic sensors began to be used to determine which path Luka should follow.

![jun1](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/4ec63c83-89a8-4a1b-ab29-952e07b1f754)

The team managed to fully complete the report and finished uploading all the information to GitHub by the end of the month, being fully prepared for the 2024 National WRO competition.

![JUN2](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/ec3a2df2-7dff-4fec-b924-b2d1eb7ead83) ![JUN3](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/cd6712cd-9323-48ea-98b8-636553662499)


### October 2024

After winning the national competition, the team managed to become part of the delegation representing Venezuela in the international finals of the Robotics Olympiad in Izmir, Turkey. This required extensive preparation and practice, so they began working on Luka.

During the first two weeks of preparation, the team started making structural changes to Luka to reduce the size of the robot. To achieve this, both the traction and steering systems were modified. The steering system was rotated 180 degrees so that the wheels were positioned more toward the front, and the traction motor was repositioned vertically to occupy less horizontal space. After this, approximately 5 cm of unused space at the rear of the robot was removed, completing this process with the robot measuring 18 cm in length.

![motor comparation](https://github.com/user-attachments/assets/00b11495-df00-430e-b246-063aeed43f5f)
![Traction comparation](https://github.com/user-attachments/assets/34566443-f982-43b6-9cad-7033e43392aa)


The third week of work marked the start of programming. After encountering issues with powering the Raspberry Pi, the team decided to look for a new method to detect traffic signals. After evaluating solutions, they chose to use a Pixy Cam because it took up less space, weighed less, and could be powered directly by the Arduino. The team also realized that a gyroscope would be necessary, especially for the second challenge, so they began using the HMS5883L magnetometer.

![pixy2 1](https://github.com/user-attachments/assets/0d5ba0ac-d5ba-47c5-957f-c5cc7350b439)
![HMC5883L](https://github.com/user-attachments/assets/fdfc00e6-27a0-4843-81a8-c86973bba489)


The Pixy Cam turned out to be an excellent choice, but the magnetometer was not, so the team started looking for a new one and chose the MPU6050. After extensive practice with the accelerometer, the team was able to use it on full curves, but due to its large margin of error, they could not rely on it to make the car turn exactly 90 degrees.

![prueba pixy](https://github.com/user-attachments/assets/ba0a2a27-5e38-4ecf-aacf-253b168c61ea)
![MPU6050](https://github.com/user-attachments/assets/14ad7f2f-d015-4d14-b35c-de9057ae6749)


Therefore, the team used the fourth week to design a new strategy. With this new strategy, the robot was calibrated with the outer walls. 

### November 2024

The first week of November was devoted entirely to preparation and practice. During this week, the robot managed to complete two consistent laps in the second challenge, but the team remained concerned about the gyroscope issue. 

![ramdom practice](https://github.com/user-attachments/assets/0c77eda4-712e-47df-84f0-b20429e7cd49)



Therefore, in the second week of November, the team began practicing with a new gyroscope, the BNO055. This sensor is a hybrid of a magnetometer and an accelerometer, which allows it to provide almost exact data. 

![BNO055](https://github.com/user-attachments/assets/9bccdb43-f634-4808-92c7-ae4d567bc054)

Finally, on the 28th, 29th, and 30th of this month, the team competed in the international finals in Turkey, achieving 19th place worldwide and second place in Latin America. 

"FOTO"

This competition left the team highly motivated for the upcoming national competitions, with the goal of qualifying and achieving the best results in the international final to be held in Singapore. 

![Image](https://github.com/user-attachments/assets/2f67bc4d-b872-4518-9a7e-bd1731d2f31f)

## 2025 season

### February 2025

As in previous years, Red Machine's first action at the start of a new season was to review the changes in the competition rules and scoring. The team carefully studied the new rules to ensure that everything they did was in accordance with them, and to develop and create the best robot possible. 

Under these rules, in the following weeks of this first month, work began on creating the first prototype of the new robot, “Pompo.”


### March 2025

This month, the team finished the first pompo prototype and began programming, using ROBOTC as the environment to program the ev3 module, which was the brain of this first pompo prototype. 
After long practice sessions, the team completed the first challenge perfectly, so it was time to move on to the second one. At this point, the team encountered a major problem: adapting the Pixycam to this EV3 module. 

### April 2025

After spending time looking for solutions to this problem, the team decided that it would be best to go back to working with Arduino, as the programming is very similar and the current problem could be solved much more quickly. 
Based on this, they worked for a long time to modify the entire robot chassis to adapt it to Arduino and the new sensors and motors that would be used, as those from EV3 are not directly compatible with Arduino.
Once construction was complete, the team returned to programming, but when they tested Pompo on the track, its chassis began to malfunction. 

### May 2025

For this reason, the team began working again on improving the chassis, finally achieving what would be the first definitive pompo chassis.
The scheduling of the first challenge was quick, so work on the second challenge began almost immediately. 

## Julian, luka and pompo

### JULIAN 1.0

![Primer Julian ](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/09cf93c9-366d-4cb8-a5c8-3ff131a1eefd)

### JULIAN 2.0

![segundo julian](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/e478974d-5332-49b8-afac-896d01656986)

### JULIAN 3.0

![Tercer Julian](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/cdd24993-e070-411b-bbf5-a24d7a4b233f)

### JULIAN 4.0

![Cuarto Julian](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/074197a0-749a-46c5-a047-525aad2b035c)

### JULIAN 5.0

![Quinto Julian ](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/0ce756c7-e496-4795-b2be-6cf495847561)

### LUKA 1.0

![Primer Luka](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/72f9fc19-2931-4442-80e8-b228e3491019)

### LUKA 2.0

![Segundo Luka ](https://github.com/RoboticaLLR/redmachine2024/assets/155327813/565f334d-1133-470b-ba16-1d1ea5e7b660)

### LUKA 3.0

![Luka`s right](https://github.com/user-attachments/assets/7adb4b68-6ba3-44b4-b7dc-02d3c609dd1a)


### POMPO 1.0

![Image](https://github.com/user-attachments/assets/02ba46a0-c65a-447c-a863-a571f83f3bbb)

### POMPO 2.0

![Image](https://github.com/user-attachments/assets/36442ffd-411f-4371-bcaa-29c3b6fd4452)


### POMPO 3.0

![Image](https://github.com/user-attachments/assets/40842456-c271-4c38-b15f-77bbeb7e6772)






