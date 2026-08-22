

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
Responsible for the robot programming and the robot's electronics.

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
Responsible for the robot's repository.

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

# ⚙️ Diseño y Fabricación Mecánica

## 1. Fabricación Digital y Selección de Materiales

* **Diseño CAD en Fusion 360 e Impresión 3D:** El vehículo fue modelado íntegramente en **Autodesk Fusion 360**, lo que nos permitió diseñar un chasis adaptado al 100% a las necesidades geométricas del proyecto. Toda la fabricación física se realizó en una impresora **Creality K1 Max**. Esta combinación nos dio una flexibilidad total durante el desarrollo para realizar modificaciones estructurales rápidas, ajustar tolerancias de ensamble sobre la marcha e iterar el diseño a medida que agregábamos componentes mecánicos sin depender de piezas comerciales rígidas.

* **Elección del PETG frente a otros materiales:** Evaluamos las distintas opciones de filamentos en el mercado (PLA, ABS, ASA y Nylon) y seleccionamos **PETG** como el material definitivo por las siguientes razones:
  * **Frente al PLA:** El PLA es excesivamente rígido y cristalino, lo que lo vuelve quebradizo ante choques, impactos o vibraciones continuas. El PETG ofrece una tenacidad superior con la flexibilidad justa para absorber esfuerzos mecánicos sin fracturarse.
  * **Frente al ABS y ASA:** Aunque el ABS y el ASA ofrecen alta resistencia térmica, sufren de una fuerte contracción al enfriarse (*warping*), lo que dificulta la precisión dimensional en piezas estructurales planas como los pisos del chasis. El PETG ofrece una estabilidad dimensional excelente al imprimirse, sin deformaciones en las esquinas.
  * **Frente al Nylon (PA):** El Nylon es altamente resistente pero requiere condiciones extremas de secado y procesado por su alta higroscopía. El PETG proporciona una rigidez estructural y resistencia al impacto óptimas para las cargas de la competencia sin la complejidad de manipulación del Nylon.
  * **En conclusión:** El PETG representó el equilibrio perfecto entre **tenacidad a impactos, rigidez dimensional, durabilidad mecánica y facilidad de procesamiento**.

* **Parámetros de Impresión Predeterminados (Creality Print):**
  * **Temperatura de Boquilla (Nozzle Temperature):** $240^\circ\text{C} - 245^\circ\text{C}$ (garantiza fusión completa y máxima adhesión intercapa).
  * **Temperatura de la Cama (Bed Temperature):** $70^\circ\text{C} - 80^\circ\text{C}$ (previene desprendimientos o *warping*).
  * **Velocidad de Impresión (Print Speed):** $50\text{ mm/s} - 100\text{ mm/s}$ (mantiene la precisión dimensional en voladizos y orificios).
  * **Relleno (Infill) y Patrón:** $15\% - 20\%$ con patrón Grid / Gyroid (balance entre rigidez y bajo peso).
  * **Enfriamiento de Capa (Fan Speed):** $30\% - 50\%$ (equilibrio entre acabado estético y cohesión estructural).

---

## 2. Evolución del Chasis y Prototipado CAD

* **Prototipo 1 (Boceto Base y Silueta Monocapa):** Diseñamos una placa plana inicial en Fusion 360 para definir las dimensiones generales del robot y evaluar la posición física de los componentes. Incluyó un hueco rectangular posterior para la transmisión y cuatro columnas verticales para proyectar la altura del segundo nivel. Confirmó que la estructura impresa resultaba sumamente ligera, permitiéndonos trabajar con motores estándar sin perder agilidad.

(INSERTA AQUÍ LA FOTO DEL PROTOTIPO 1 CAD - WhatsApp Image 2026-08-22 at 11.13.13 AM.jpeg)

* **Prototipo 2 (Chasis con Caja Inferior Integrada):** Rediseñamos la sección delantera del chasis incorporando una estructura en forma de caja en la parte inferior. Este subchasis encajonado albergó el servomotor de dirección y la transmisión en ranuras a medida, fijando la arquitectura base: **tracción trasera y dirección delantera**.

(INSERTA AQUÍ LA FOTO DEL PROTOTIPO 2 CAD - WhatsApp Image 2026-08-22 at 11.15.01 AM.jpeg)

* **Prototipos Intermedios (Evolución del Segundo Piso y Torre LiDAR):** Se diseñó el plato del piso superior con una elevación tipo escalón/cantiléver en la zona frontal. Este desnivel se concibió específicamente para montar el sensor LiDAR por encima de la dirección pero por delante de la Raspberry Pi 5, logrando una visión hacia el frente y laterales de ~270° totalmente despejada.

(INSERTA AQUÍ LA FOTO DEL CAD PISO 2 Y TORRE LIDAR - image_01017c.png)

* **Prototipo Final Ensamblado (Red Machine):** Consolidamos el ensamble integral uniendo el chasis de PETG con la electrónica y la mecánica de precisión:
  * **Estructura Vertical de Dos Niveles:**
    * **Nivel Inferior:** Encajonado para albergar el Arduino Uno, driver puente H y reguladores de voltaje, aislándolos de interferencias externas y caídas.
    * **Nivel Superior:** Diseñado para alojar la Raspberry Pi 5 con disipador de aluminio y ventilador, asegurando un flujo de aire constante para el procesador.
  * **Rigidez Estructural por Anclaje Dual:** La firmeza del piso superior se logró mediante una combinación estratégica: en los laterales, la estructura propia de los portabaterías actúa como pared portante fija, mientras que en la parte delantera se colocaron dos tornillos de sujeción directa sobre las columnas principales. Este anclaje cancela cualquier flexión o juego del segundo piso, manteniéndolo completamente estático ante vibraciones o movimientos bruscos.
  * **Integración del Portabaterías 18650:** Las baterías Li-Ion de 3.7V se alojaron lateralmente formando una pared estructural entre el primer y segundo piso. Esta disposición ahorra volumen interno y sitúa la masa de las baterías en el centro geométrico del vehículo para equilibrar el peso.
  * **Torre Frontal del LiDAR:** El soporte en escalón fija el LiDAR a una altura estratégica cercana a los 10 cm mediante tornillería M3 y espárragos roscados. Esta elevación sitúa el plano de escaneo justo en la parte superior del tope de las paredes de la pista, asegurando una lectura panorámica despejada hacia el frente y los costados (sin el bloqueo posterior de la Raspberry Pi) y libre de interferencias causadas por los bordes de los muros.
  * **Dirección Híbrida PETG-Lego:** El servomotor acciona directamente un subensambaje de manguetas y brazos de dirección Lego Technic. Esta combinación eliminó las holguras mecánicas de los prototipos impresos previos, proporcionando giros de alta precisión.
  * **Geometría de Trocha Reducida:** Como se aprecia en la estructura frontal del robot real, las ruedas de dirección están sensiblemente más juntas que las ruedas traseras de tracción. Esta configuración acorta el eje transversal de giro, garantizando un agarre óptimo del tren delantero y eliminando los derrapes indeseados (*oversteer*) en las curvas.

(INSERTA AQUÍ LA FOTO DEL ROBOT IMPRESO CON LIDAR/DIRECCIÓN - WhatsApp Image 2026-08-22 at 11.17.11 AM.jpeg)

(INSERTA AQUÍ LA FOTO DEL ROBOT COMPLETO CON RASPBERRY Y BATERÍAS - image_010486.jpg)

---

## 3. Módulo de Tracción y Centro de Masa

* **Tracción Trasera y Distribución de Pesos ($CoG$):** Los motores envían la potencia directamente a las ruedas traseras desde la caja inferior. Al situar los componentes pesados (baterías en los laterales bajos, Arduino, puente H y reguladores) en el primer piso, logramos mantener un **centro de gravedad bajo y centrado**, lo que garantiza estabilidad en curva y una adherencia constante del tren trasero sin riesgo de vuelco.

---

## 4. Módulo de Dirección y Comportamiento Dinámico

* **Optimización de la Trocha Delantera (Ancho de Eje):** Inicialmente las ruedas delanteras tenían la misma separación que las traseras. Sin embargo, al acercar las ruedas delanteras entre sí (trocha estrecha), logramos eliminar el problema de sobreviraje (*coleo/drifting*) en los giros.
* **Explicación Técnica del Agarre:** Al acortar el eje delantero, se reduce el momento de inercia lateral y el brazo de palanca al girar. Esto evita que el tren delantero muerda el suelo de forma violenta, permitiendo que las ruedas traseras mantengan el empuje en línea recta de forma homogénea y el vehículo tome las curvas de manera fluida y precisa.
* **Acoplamiento Servo-Lego:** La integración de componentes Lego en la articulación de la dirección eliminó las holguras mecánicas de la pieza impresa previa, permitiendo un movimiento suave, preciso y de fácil mantenimiento.

---

## 5. Integración de Sensores y Estructura Superior

* **Soporte y Posicionamiento del LiDAR:** La elevación frontal coloca al sensor justo sobre el límite superior de las paredes de la pista (~10 cm), permitiendo captar el entorno sin obstaculizar su rango de visión.
* **Estabilidad de Sensores y Cableado:** Gracias a la fijación con los dos tornillos delanteros y la rigidez lateral de los portabaterías, el segundo piso no flexiona, manteniendo las lecturas del LiDAR y de la Raspberry Pi totalmente estables sin sufrir descalibraciones por movimientos indeseados del chasis. Se incorporaron canales y pasajes entre ambos pisos para mantener el cableado protegido, ordenado y accesible.


# Explicación Detallada de los Componentes

### Raspberry Pi 5
Computadora monoplaca de alto rendimiento equipada con un procesador Broadcom BCM2711 Quad-Core ARM Cortex-A72 a 1.5 GHz. Funciona como la unidad central de cómputo del robot, asumiendo el procesamiento pesado de imágenes capturadas por la webcam y la gestión de la nube de puntos transmitida por el Lidar ST27L. Su arquitectura ARM de 64 bits y su memoria RAM permiten ejecutar la pila del sistema operativo Linux (UBUNTU) e hilos paralelos mediante Python, garantizando que el procesamiento visual intensivo y la construcción del mapa espacial no generen cuellos de botella ni bloqueen las respuestas dinámicas del vehículo en la pista. Fue especificamente utilizada por encima de la raspberry pi 4, ya que completa cada iteracion del codigo un 13% mas rapido, ofreciendo aun mas precision, siendo muy relevante para el uso del lidar.

<img width="547" height="365" alt="Image" src="https://github.com/user-attachments/assets/ee4a2d47-cdb3-4551-9ac5-bdc70aca7ef5" />

---

### Arduino Uno
Microcontrolador de 8 bits basado en el chip ATmega328P que opera a una frecuencia de reloj de 16 MHz. Dentro de la arquitectura del robot, se desempeña como el nodo de control en tiempo real dedicado a la ejecución de tareas críticas de bajo nivel. Recibe las directivas de movimiento enviadas desde la Raspberry Pi y genera las señales PWM hacia el driver de motores TB6612FNG y al servomotor. Al delegar la temporización estricta de las salidas lógicas a este microcontrolador, se evita que las interrupciones del sistema operativo de la Raspberry Pi causen fluctuaciones en la velocidad de las ruedas o imperfecciones en la respuesta de los actuadores. El arduino uno fue utilizado principalmente para facilitar la construccion de este chasis, debido a que otro tipo de microcontroladores son mucho mas dificiles de encontrar por lo tanto dificultarian poder replicar el chasis.

<img width="554" height="554" alt="Image" src="https://github.com/user-attachments/assets/f3303144-e0d6-4a5d-963b-7fc49d130d49" />

---

### Lidar LDROBOT ST27L
Sensor óptico de medición de distancia omnidireccional basado en la tecnología dToF (Direct Time-of-Flight), capaz de realizar escaneos de 360° en el plano horizontal a rangos de hasta 25 metros. Emite pulsos de luz láser infrarroja y mide el tiempo exacto que tardan en rebotar contra los obstáculos, generando una matriz de coordenadas espaciales en tiempo real. Esta información es fundamental para los algoritmos de navegación y evasión de paredes, ofreciendo una inmunidad total ante cambios bruscos de iluminación ambiental, sombras sobre la pista o variaciones en el color de la superficie de los muros. Se utiliza el lidar en contraste a los ultrasonidos para obtener una precision ~99.1%, debido a que trabajamos con mayor cantidad de datos, donde somos capaces de trazar una recta que se asemeja a la de las paredes en un 93,4%, lo cual asegura que la raspberry pi no confunda las paredes de la pista con cualquier otro obstaculo de la pista, tales como los conos o los estacionamientos.

<img width="1560" height="1040" alt="Image" src="https://github.com/user-attachments/assets/46ac07cd-9cbf-48de-8fcb-77f954027434" />

---

### Servomotor REV Robotics
Actuador de dirección de grado robótico con piñonería interna metálica de alta resistencia y motor integrado de corriente continua, optimizado para operar a 6.0 V con un torque de hasta 13.5 kg-cm. Su función principal es posicionar el mecanismo del tren delantero para cambiar la trayectoria del vehículo. Su electrónica digital interna ajusta la posición del eje con alta precisión angular, manteniendo el ángulo de dirección fijo sin ceder ante las fuerzas de fricción de las ruedas sobre la pista o las inercias generadas durante cambios de dirección a alta velocidad.

<img width="447" height="447" alt="Image" src="https://github.com/user-attachments/assets/8abc1899-f602-4f87-bb8d-5500465385a9" />

---

### Driver TB6612FNG (Puente H Dual)
Módulo controlador de motores basado en una etapa de potencia MOSFET de baja resistencia interna en estado activo (Rds(on)). Permite manejar dos motores DC en paralelo con una corriente continua de hasta 1.2 A por canal (3.2 A pico). Al utilizar transistores MOSFET en lugar de los antiguos transistores bipolares, ofrece una eficiencia energética superior con una disipación de calor mínima, respondiendo de forma lineal a las señales de ciclo de trabajo PWM de hasta 100 kHz enviadas por el Arduino Uno para regular aceleraciones y frenados. Fue un cambio al antiguo puente h l298n, debido a que este nos ofrece mas eficiencia, en un espacio muchisimo menor, permitiendonos hacer todos los cambios fisicos exigidos.

<img width="600" height="600" alt="Image" src="https://github.com/user-attachments/assets/c2a01a8a-279a-4ffb-bbfb-bd9812285ecc" />

---

### Cámara Webcam
Sensor de captura de imagen HD conectado vía USB a la Raspberry Pi, dedicado a la adquisición de cuadros de video en tiempo real. Proporciona el flujo de datos visuales necesario para que los algoritmos de visión artificial procesen el entorno, detecten patrones cromáticos, identifiquen señales de tráfico y reconozcan elementos clave del circuito. Su integración directa al bus USB 3.0 de la Raspberry Pi permite la transmisión fluida de imágenes sin sobrecargar el bus de comunicación serie del microcontrolador de bajo nivel.

*(Espacio para foto de la Webcam)*

---

### Banco de Baterías 18650 (Arreglo 2S2P)
Fuente de alimentación principal conformada por cuatro celdas cilíndricas recargables de Ion de Litio (Li-ion) formato 18650, configuradas en dos ramas en paralelo de dos celdas en serie cada una. Entrega una tensión nominal de 7.4 V (8.4 V a plena carga) y una capacidad acumulada de 4000 mAh. Esta química de batería ofrece una resistencia interna extremadamente baja, lo que permite suministrar ráfagas elevadas de corriente sin sufrir caídas parásitas de voltaje (*brownouts*) cuando los motores de tracción y el servo de dirección demandan torque máximo en momentos de alta aceleración.

<img width="447" height="447" alt="Image" src="https://github.com/user-attachments/assets/49806f89-29f1-40ea-af4c-96aacd6fbabc" />

---

### Reductor de Voltaje XL4015 (Step-Down 5 A)
Convertidor conmutado de corriente continua (*Buck Converter*) capaz de transformar el voltaje variable del banco de baterías (7.4 V – 8.4 V) en una línea regulada estable de 5.0 V DC con capacidad de suministro de hasta 5 A. Su frecuencia de conmutación interna y su alto rendimiento energético (hasta el 96%) evitan el desperdicio de energía en forma de calor residual, suministrando una alimentación limpia e inmune a ruidos electromagnéticos a la Raspberry Pi, la cual a su vez energiza la webcam, el Lidar ST27L y el Arduino Uno. Este componente es estrictamente necesario, debido a que la mayoria de reductores de voltaje de bajo costo suministran una cantidad menor a 4A, lo cual es necesario para el correcto funcionamiento de la raspberry pi, y por lo tanto de sus componentes adyacentes


<img width="500" height="314" alt="Image" src="https://github.com/user-attachments/assets/575e3060-acd1-46a1-82d9-acdd8987e7ab" />

---

### Reductor de Voltaje LM2596 (Step-Down 3 A)
Regulador conmutado independiente que opera a una frecuencia de 150 kHz, dedicado a transformar la tensión de las baterías en una salida fija de 6.0 V DC para la etapa de dirección. Al estar aislado de la línea de 5.0 V de la computadora principal, absorbe los picos térmicos y electromagnéticos que genera el servomotor REV Robotics durante sus movimientos bruscos, previniendo que el ruido inductivo del motor o los bajones de tensión repentinos causen reinicios imprevistos en la Raspberry Pi o fallas de sincronía en el Lidar.

<img width="554" height="554" alt="Image" src="https://github.com/user-attachments/assets/fc3d9751-dfd1-4643-af99-ec4f98f1a798" />

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



## Preparación de la Raspberry Pi

### Descarga e instalación de Ubuntu Server en la microSD

En tu ordenador local, descarga e instala **Raspberry Pi Imager** desde [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/). En Ubuntu, puedes instalarlo con:

```bash
sudo snap install rpi-imager
```

Inserta la microSD (mínimo 16 GB, clase 10) en tu lector. Abre Raspberry Pi Imager y sigue estos pasos:
- **Choose OS** → Other specific-purpose OS → Ubuntu → **Ubuntu Server 24.04 LTS (64‑bit)**.
- **Choose Storage** → selecciona tu microSD.

Haz clic en el engranaje (⚙️) para la configuración avanzada:
- Marca **Set hostname** y escribe, por ejemplo, `wro-robot`.
- Marca **Enable SSH** y elige **Use password authentication**.
- Establece el usuario y contraseña que usarás, por ejemplo: Usuario: `wro`, Contraseña: `wro2025`.
- Marca **Configure wireless LAN** e introduce el SSID y la contraseña de tu red Wi‑Fi.
- Marca **Set locale settings**: elige `es_ES.UTF-8` y `Europe/Madrid`.

Haz clic en **Write** y espera a que termine la escritura. Una vez escrita, retira la microSD, insértala en la Raspberry Pi y conecta la alimentación USB‑C.

### Primer arranque y configuración inicial

Al encender, Ubuntu Server arrancará y mostrará un prompt de inicio de sesión. Inicia sesión con el usuario y contraseña que configuraste.

Ejecuta los siguientes comandos para actualizar el sistema e instalar herramientas básicas:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y net-tools git vim curl wget htop
```

Configura la zona horaria y sincroniza la hora (importante para ROS 2 y certificados):

```bash
sudo timedatectl set-timezone Europe/Madrid
sudo apt install -y ntp
sudo timedatectl set-ntp true
```

Reinicia para asegurar que todos los cambios se aplican:

```bash
sudo reboot
```

### Configuración de la red (Wi‑Fi e IP fija)

Si configuraste el Wi‑Fi en el Imager, ya deberías tener conexión. Para verificar:

```bash
ip a
ping -c 4 google.es
```

Para asignar una IP fija (recomendado para SSH), editamos el archivo de configuración de Netplan:

```bash
sudo nano /etc/netplan/50-cloud-init.yaml
```

Sustituye el contenido por el siguiente (ajusta la IP, puerta de enlace y SSID/contraseña a tu red):

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      optional: true
  wifis:
    wlan0:
      dhcp4: false
      addresses:
        - 192.168.1.100/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
      access-points:
        "nombre_de_tu_wifi":
          password: "tu_contraseña"
```

Guarda con `Ctrl+O`, Enter, y sal con `Ctrl+X`. Aplica la configuración:

```bash
sudo netplan apply
```

Verifica que tienes la IP asignada:

```bash
hostname -I
```

Anota la IP (ej. `192.168.1.100`).

### Habilitación y configuración de SSH

SSH ya debería estar activo si lo marcaste en el Imager. Para asegurarte:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Desde tu ordenador local, prueba la conexión:

```bash
ssh wro@192.168.1.100
```

Si todo funciona, ya puedes trabajar sin monitor ni teclado.

---

## Instalación de ROS 2 Jazzy en la Raspberry Pi

Seguimos la [guía oficial de ROS 2 Jazzy para Ubuntu 24.04](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).

### Configuración del locale

```bash
sudo apt update && sudo apt install -y locales
sudo locale-gen es_ES es_ES.UTF-8
sudo update-locale LC_ALL=es_ES.UTF-8 LANG=es_ES.UTF-8
export LANG=es_ES.UTF-8
```

Añade la variable al final de `~/.bashrc` para que persista:

```bash
echo "export LANG=es_ES.UTF-8" >> ~/.bashrc
```

### Adición del repositorio de ROS 2

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install -y curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### Instalación de ROS 2 Humble

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y ros-Jazzy-desktop
sudo apt install -y python3-colcon-common-extensions python3-rosdep python3-pip
```

### Configuración del entorno

Añade el sourcing de ROS 2 a tu `.bashrc`:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
source ~/.bashrc
```

Inicializa `rosdep`:

```bash
sudo rosdep init
rosdep update
```

---

## Configuración del entorno de desarrollo en tu ordenador local

Vamos a usar **Visual Studio Code** con la extensión **Remote‑SSH** para editar y ejecutar código directamente en la Raspberry Pi.

### Instalación de Visual Studio Code

Descarga e instala VS Code desde [https://code.visualstudio.com/](https://code.visualstudio.com/). En Ubuntu:

```bash
sudo snap install --classic code
```

### Instalación de la extensión Remote‑SSH

Abre VS Code, ve a la pestaña de Extensiones (Ctrl+Shift+X) y busca **Remote - SSH**. Instala la extensión de Microsoft.

### Configuración de la clave SSH para la Raspberry Pi (recomendado)

Para no tener que escribir contraseña cada vez, genera un par de claves en tu ordenador local:

```bash
ssh-keygen -t rsa -b 4096 -C "wro-robot"
```

Copia tu clave pública a la Raspberry Pi:

```bash
ssh-copy-id wro@192.168.1.100
```

Prueba que ya no pide contraseña: `ssh wro@192.168.1.100`.

### Conexión remota a la Raspberry Pi desde VS Code

En VS Code, haz clic en el icono de **Remote Explorer**. Elige **"Add New SSH Host..."** y escribe `wro@192.168.1.100`. Una vez añadido, haz clic en el icono de conexión para abrir una sesión remota.

---

## Preparación del código en la Raspberry Pi

### Creación del workspace de ROS 2

```bash
mkdir -p ~/wro_ws/src
cd ~/wro_ws
```

### Creación del paquete y del nodo

```bash
cd ~/wro_ws/src
ros2 pkg create --build-type ament_python wro_reto_abierto
cd wro_reto_abierto
rm -rf wro_reto_abierto/*.py
touch wro_reto_abierto/wro_reto_abierto_node.py
chmod +x wro_reto_abierto/wro_reto_abierto_node.py
```

Edita el `setup.py` para que el punto de entrada apunte a nuestro nodo:

```python
entry_points={
    'console_scripts': [
        'wro_node = wro_reto_abierto.wro_reto_abierto_node:main',
    ],
},
```

### Instalación de dependencias Python

```bash
sudo pip3 install numpy pyserial
```

---

## Configuración del Arduino Uno

### Instalación del Arduino IDE en Ubuntu

```bash
sudo apt install -y arduino arduino-core
```

### Configuración de permisos del puerto serial

```bash
sudo usermod -a -G dialout wro
```

### Conexión física del Arduino Uno a la Raspberry Pi

Conecta el Arduino Uno a la Raspberry Pi mediante un cable USB tipo B.

### Compilación y carga del código en el Arduino

Crea un archivo `sketch.ino`:

```bash
mkdir -p ~/arduino_sketch
nano ~/arduino_sketch/sketch.ino
```

Código completo del Arduino:

```cpp
#include <Servo.h>

const int pinMotor1 = 4;
const int pinMotor2 = 5;
const int pinServo  = 7;

Servo miServo;

void fijarMotor(int velocidad) {
  velocidad = constrain(velocidad, -150, 150);
  if (velocidad > 0) {
    int pwmResta = 150 - velocidad; 
    analogWrite(pinMotor1, 150);
    analogWrite(pinMotor2, pwmResta);
  } else if (velocidad < 0) {
    int pwmResta = 150 - abs(velocidad);
    analogWrite(pinMotor1, pwmResta);
    analogWrite(pinMotor2, 150);
  } else {
    digitalWrite(pinMotor1, LOW);
    digitalWrite(pinMotor2, LOW);
  }
}

void setup() {
  Serial.begin(115200); 
  pinMode(pinMotor1, OUTPUT);
  pinMode(pinMotor2, OUTPUT);
  miServo.attach(pinServo);
  miServo.write(57);
  fijarMotor(0);
}

void loop() {
  if (Serial.available() > 0) {
    String entrada = Serial.readStringUntil('\n');
    entrada.trim();
    if (entrada.length() > 0) {
      char tipoComando = toupper(entrada.charAt(0)); 
      if (tipoComando == 'S') {
        int angulo = entrada.substring(1).toInt();
        angulo = constrain(angulo, 30, 90);
        miServo.write(angulo);
      } else if (tipoComando == 'M') {
        int velocidad = entrada.substring(1).toInt();
        fijarMotor(velocidad);
      } else if (isDigit(tipoComando) || tipoComando == '-') {
        int angulo = entrada.toInt();
        angulo = constrain(angulo, 30, 90);
        miServo.write(angulo);
      }
    }
  }
}
```

**Carga del sketch** con `arduino-cli`:

```bash
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
sudo mv bin/arduino-cli /usr/local/bin/
arduino-cli compile --fqbn arduino:avr:uno ~/arduino_sketch/
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno ~/arduino_sketch/
```

---

## Comunicación Serial entre ROS 2 y Arduino

### Identificación del puerto serial

```bash
ls /dev/ttyACM*
```

Normalmente aparecerá `/dev/ttyACM0`.

### Permisos del puerto serial

```bash
sudo chmod 666 /dev/ttyACM0
sudo usermod -a -G dialout $USER
```

### Creación de una regla udev permanente

```bash
sudo nano /etc/udev/rules.d/99-arduino.rules
```

Contenido:
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0043", MODE="0666"
```

Recarga las reglas:

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

---

## Compilación y ejecución del proyecto

### Compilación del workspace

```bash
cd ~/wro_ws
colcon build --symlink-install
```

### Configuración de variables de entorno

```bash
echo "source ~/wro_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Creación del archivo del nodo Python

```bash
nano ~/wro_ws/src/wro_reto_abierto/wro_reto_abierto/wro_reto_abierto_node.py
```

### Ejecución del nodo

```bash
ros2 run wro_reto_abierto wro_node
```

---

## Explicación Detallada del Código y su Lógica

He diseñado este sistema con una arquitectura cliente-servidor donde la Raspberry Pi (ROS 2) actúa como el cerebro principal que procesa los datos del LiDAR y toma decisiones de alto nivel, mientras que el Arduino Uno se encarga del control en tiempo real de los actuadores.

### Lógica de Navegación Global

El flujo de navegación que he implementado sigue un ciclo continuo basado en la detección del entorno:

```
[INICIO] → [Leer LiDAR] → [¿Pared frontal?]
                              ↓
                          Sí → [¿Sentido definido?] → No → [Comparar laterales] → [Fijar sentido]
                              ↓                                              ↓
                              Sí → [Girar 90° según sentido]                [Girar]
                              ↓
                          No → [¿Sentido definido?] → No → [Avanzar recto buscando pared]
                              ↓
                              Sí → [Seguir pared según sentido]
                              ↓
                         [Volver a leer LiDAR]
```

### Análisis del Código Python (Nodo ROS 2)

He estructurado el nodo en varias capas funcionales para mantener el código limpio y modular.

#### 1. Configuración Inicial y Parámetros

En el método `__init__`, he declarado todos los parámetros ajustables que permiten modificar el comportamiento del robot sin recompilar:

```python
self.declare_parameter('sentido', 0)                    # Dirección de giro (0=desconocido)
self.declare_parameter('distancia_objetivo', 0.4)      # Distancia deseada a la pared (metros)
self.declare_parameter('distancia_frontal_obstaculo', 0.35)  # Umbral para detectar pared frontal
self.declare_parameter('velocidad_motor', 20)          # Velocidad constante
self.declare_parameter('limite_angulo_max', 38.0)      # Límite de corrección angular
```

He incluido un sistema PID completo para controlar tanto la distancia como el ángulo respecto a la pared. Los parámetros Kp, Ki y Kd permiten ajustar la respuesta del robot a diferentes velocidades y superficies.

#### 2. Callback del LiDAR (Función Principal)

He implementado la lógica principal en `lidar_callback`, que se ejecuta cada vez que llega un nuevo escaneo del LiDAR:

```python
def lidar_callback(self, msg):
    # Calculo del tiempo entre frames para los PID
    current_time = self.get_clock().now()
    dt = (current_time - self.last_time).nanoseconds / 1e9
    self.last_time = current_time
    
    # Lectura y filtrado de distancias
    self.detectardistancias(msg)
    
    # Lógica de decisión según obstáculos
    if self.d < dist_frontal_limite and self.d > 0:
        # Obstáculo frontal detectado
        if self.sentido == 0:
            self.detectarlado_en_pared()
        # Ejecución de giro
    else:
        # Navegación normal
```

#### 3. Filtrado de Datos del LiDAR

He creado `detectardistancias()` para extraer únicamente los puntos relevantes del escaneo:

- **Frente**: Ángulos de 75° a 105° (para detección de obstáculos frontales)
- **Derecha**: Ángulos de 165° a 195° (para seguimiento de pared derecha)
- **Izquierda**: Ángulos de 345° a 15° (para seguimiento de pared izquierda)

Utilizo el valor mínimo de cada sector como distancia representativa, lo que asegura que el robot reaccione al obstáculo más cercano.

#### 4. Determinación del Sentido de Navegación

El método `detectarlado_en_pared()` compara las distancias laterales cuando el robot encuentra su primera pared frontal:

```python
def detectarlado_en_pared(self):
    if self.dd < self.di:
        self.sentido = 2  # Girar a la derecha y seguir pared derecha
    else:
        self.sentido = 1  # Girar a la izquierda y seguir pared izquierda
```

Esta decisión se toma UNA SOLA VEZ en toda la ejecución, permitiendo que el robot mantenga una estrategia consistente durante todo el recorrido.

#### 5. Algoritmo de Seguimiento de Pared con SVD (Singular Value Decomposition)

He implementado un método avanzado de seguimiento de pared utilizando SVD, que es más robusto que simplemente usar la distancia mínima:

**Proceso matemático implementado en `calcular_pid_svd()`:**

1. **Transformación de coordenadas polares a cartesianas**: Convierto las lecturas de distancia (r) y ángulo (θ) a coordenadas X,Y:
   ```python
   X = r * cos(θ)
   Y = r * sin(θ)
   ```

2. **Cálculo de la línea de la pared**: Utilizo SVD para encontrar la línea que mejor se ajusta a todos los puntos:
   ```python
   X_c = X - mean(X)
   Y_c = Y - mean(Y)
   _, _, Vh = np.linalg.svd(np.vstack([X_c, Y_c]).T)
   dir_x, dir_y = Vh[0]  # Vector dirección de la pared
   norm_x, norm_y = Vh[1]  # Vector normal a la pared
   ```

3. **Cálculo de errores**:
   - **Error de distancia**: Distancia deseada (0.4m) menos distancia real a la pared
   - **Error de ángulo**: Diferencia entre la orientación de la pared y la dirección deseada (paralela al robot)

4. **Control PID**: Calculo dos salidas PID (una para distancia y otra para ángulo) que se combinan para producir la corrección final del servo:
   ```python
   salida_distancia = Kp_d * error_distancia + Kd_d * derivada_dist + Ki_d * integral_dist
   salida_angulo = Kp_a * error_angulo + Kd_a * derivada_ang
   correccion_total = salida_distancia + salida_angulo
   ```

#### 6. Comunicación con el Arduino

He diseñado el protocolo de comunicación para ser simple y robusto:

```python
def enviar_a_arduino(self, velocidad, angulo_servo):
    self.arduino.write(f"M{velocidad}\n".encode('utf-8'))
    self.arduino.write(f"S{angulo_servo}\n".encode('utf-8'))
```

- **M<velocidad>**: Controla la velocidad del motor (rango -150 a 150)
- **S<ángulo>**: Controla el ángulo del servo (rango 30 a 90 grados)

### Análisis del Código Arduino (Controlador de Bajo Nivel)

El sketch de Arduino actúa como un intérprete de comandos seriales:

#### 1. Control del Motor con PWM

He implementado `fijarMotor()` para controlar un motor DC mediante un puente H (TB6612FNG). La lógica de PWM es:

- **Velocidad positiva (0 a 150)**: PWM variable en pinMotor1, PWM fijo en pinMotor2
- **Velocidad negativa (-150 a 0)**: PWM fijo en pinMotor1, PWM variable en pinMotor2
- **Velocidad 0**: Ambos motores en LOW

```cpp
if (velocidad > 0) {
    int pwmResta = 150 - velocidad; 
    analogWrite(pinMotor1, 150);      // PWM fijo
    analogWrite(pinMotor2, pwmResta); // PWM variable
}
```

Esta técnica permite un control de velocidad suave y mantiene el torque constante.

#### 2. Manejo de Comandos Seriales

El bucle principal escucha constantemente el puerto serial y procesa comandos:

```cpp
if (Serial.available() > 0) {
    String entrada = Serial.readStringUntil('\n');
    char tipoComando = toupper(entrada.charAt(0));
    
    if (tipoComando == 'S') {
        int angulo = entrada.substring(1).toInt();
        miServo.write(constrain(angulo, 30, 90));
    }
    else if (tipoComando == 'M') {
        int velocidad = entrada.substring(1).toInt();
        fijarMotor(velocidad);
    }
}
```

### Diagrama de Flujo del Sistema Completo

```
┌─────────────────────────────────────────────────────────────────┐
│                        RASPBERRY PI (ROS 2)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               NODO WRO_RETO_ABIERTO                    │   │
│  │                                                         │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │            lidar_callback()                    │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  detectardistancias(msg)              │   │   │   │
│  │  │  │  • Frente (75°-105°) → self.d        │   │   │   │
│  │  │  │  • Derecha (165°-195°) → self.dd     │   │   │   │
│  │  │  │  • Izquierda (345°-15°) → self.di    │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  │                  ↓                            │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  ¿self.d < umbral?                    │   │   │   │
│  │  │  │  ↓ Sí              ↓ No               │   │   │   │
│  │  │  │  Obstáculo       Sin obstáculo        │   │   │   │
│  │  │  │  frontal         → Navegación         │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  │                  ↓                            │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  ¿sentido == 0? (primera vez)         │   │   │   │
│  │  │  │  ↓ Sí                                 │   │   │   │
│  │  │  │  detectarlado_en_pared()              │   │   │   │
│  │  │  │  • Si dd < di → sentido = 2          │   │   │   │
│  │  │  │  • Si di < dd → sentido = 1          │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  │                  ↓                            │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  sentido=1 → detectarizquierda()     │   │   │   │
│  │  │  │  sentido=2 → detectarderecha()       │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  │                                                         │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │         detectarizquierda() / derecha()        │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  obtener_puntos_sector()              │   │   │   │
│  │  │  │  • Extrae puntos en rango de ángulos  │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  │                  ↓                            │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  calcular_pid_svd()                   │   │   │   │
│  │  │  │  • SVD: encuentra línea de la pared   │   │   │   │
│  │  │  │  • PID: calcula corrección            │   │   │   │
│  │  │  │  • Retorna: corrección_total          │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  │                  ↓                            │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  angulo_servo = rec ± corrección      │   │   │   │
│  │  │  │  enviar_a_arduino(vel, angulo_servo)  │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              ↓                                  │
│                    ┌──────────────────┐                        │
│                    │  SERIAL / USB   │                        │
│                    │  /dev/ttyACM0   │                        │
│                    └──────────────────┘                        │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                         ARDUINO UNO                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    SKETCH.INO                          │   │
│  │                                                         │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │                 setup()                        │   │   │
│  │  │  • Serial.begin(115200)                       │   │   │
│  │  │  • Configura pines y servo                    │   │   │
│  │  │  • miServo.write(57)  (centro)               │   │   │
│  │  │  • fijarMotor(0)      (reposo)               │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  │                  ↓                                      │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │                 loop()                         │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  ¿Serial.available() > 0?             │   │   │   │
│  │  │  │  ↓ Sí                                 │   │   │   │
│  │  │  │  Lee comando (String)                 │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  │                  ↓                            │   │   │
│  │  │  ┌────────────────────────────────────────┐   │   │   │
│  │  │  │  tipoComando = 'S' → S<ángulo>       │   │   │   │
│  │  │  │  • miServo.write(ángulo)             │   │   │   │
│  │  │  │  • constrain(30, 90)                 │   │   │   │
│  │  │  │                                       │   │   │   │
│  │  │  │  tipoComando = 'M' → M<velocidad>    │   │   │   │
│  │  │  │  • fijarMotor(velocidad)             │   │   │   │
│  │  │  │  • constrain(-150, 150)              │   │   │   │
│  │  │  └────────────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  │                                                         │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │         fijarMotor(int velocidad)              │   │   │
│  │  │  • Velocidad > 0 → PWM en pinMotor1           │   │   │
│  │  │  • Velocidad < 0 → PWM en pinMotor2           │   │   │
│  │  │  • Velocidad = 0 → Motor detenido             │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              ↓                                  │
│                    ┌──────────────────┐                        │
│                    │   ACTUADORES    │                        │
│                    │  • Motor DC     │                        │
│                    │  • Servo        │                        │
│                    └──────────────────┘                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Solución de problemas comunes

### No se conecta al puerto serial /dev/ttyUSB0 o /dev/ttyACM0

Verifica que el Arduino está conectado y reconocido:

```bash
lsusb
ls -l /dev/ttyACM0
```

Si no tienes permisos, ejecuta:

```bash
sudo chmod 666 /dev/ttyACM0
sudo usermod -a -G dialout $USER
```

### ROS 2 no encuentra el paquete o el nodo

Asegúrate de haber hecho source del workspace:

```bash
source ~/wro_ws/install/setup.bash
```

Verifica que el nombre del paquete y del ejecutable coinciden en `setup.py`. Recompila si es necesario:

```bash
colcon build --packages-select wro_reto_abierto
```

### El servo no responde o los motores no giran

Comprueba que el Arduino recibe los comandos. Abre el monitor serial en el Arduino IDE (a 115200 baudios) y envía manualmente `S45` y `M20` para ver si hay respuesta. Verifica la conexión de los cables y que los límites del servo sean correctos (30-90).

### Las lecturas del LiDAR son erróneas

Asegúrate de que el tópico `/scan` se publica correctamente:

```bash
ros2 topic echo /scan
```

Comprueba que los rangos de ángulos en el código coinciden con la orientación del LiDAR. Puedes modificar los límites (75-105, 165-195, 345-15) según la posición del sensor.

### El robot gira en sentido incorrecto

Revisa la lógica de `detectarlado_en_pared()`. Si la pared derecha está más cerca, `sentido=2` (gira a la derecha). Para invertir el comportamiento, intercambia los valores.

---

## Recomendaciones finales

- **Prueba los comandos por separado**: antes de ejecutar el nodo completo, verifica que el Arduino responde a comandos manuales desde el monitor serial y que el LiDAR publica datos correctamente.
- **Ajusta los parámetros PID**: los valores de `Kp_dist`, `Kd_dist`, etc. dependen de la velocidad y características físicas del robot. Puedes modificarlos en tiempo real con `ros2 param set`.
- **Usa `rqt_graph`** para visualizar los nodos y tópicos: `rqt_graph`.
- **Guarda los logs**: redirige la salida a un archivo con `ros2 run wro_reto_abierto wro_node > logs.txt 2>&1`.

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






