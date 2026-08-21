

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


# Development stages (Previous robot versions) 

   
# Mechanical System ⚙
<details> 
<summary> Version 1.0 (Outdated version) </summary>
   
## Steering
The robot's steering subsystem is located at the rear to provide a larger turning radius. It was built with LEGO pieces from a robotics kit called the LEGO Spike Prime Kit, combining these parts with the wheels from a Ford Mustang remote-controlled (RC) car, to which a Rev Robotics servo motor was adapted. It was later programmed via an Arduino Mega 2560, with the servo connected to the Arduino's GND, 5V and pin 4.

## Drive
The robot's drive subsystem was taken from a Ford Mustang remote-controlled car. This system was used because it included a motor and a gearbox, providing the torque and speed needed for the robot. It operates with a set of gears that allow the robot to turn at different speeds without losing traction; this mechanism was placed at the front of the robot. The system is powered through a dual H-bridge L298n using a pack of three 3.7 V batteries.

## Chassis design
The chassis base was built from acrylic, which was cut and drilled according to the wiring and assembly needs of the used parts.

The robot has two tiers, both built from acrylic. On the robot's first deck the traction and steering systems, the ultrasonic sensor, the RGB color sensor TCS34725, two switches (one for power and the other to start), and the dual H-bridge L298n were assembled; while on the second deck are the battery pack, the 9 V battery, the ESP32-CAM camera, the Arduino Mega 2560, and the battery connector.

## Right

<img width="389" height="222" alt="image" src="https://github.com/user-attachments/assets/a2016c58-0b47-4b87-a7a0-eab0ad5f67ca" />


## Left

<img width="342" height="220" alt="image" src="https://github.com/user-attachments/assets/e5089f1b-c0ae-4e4d-b949-2b966f01b291" />


## Front

<img width="192" height="253" alt="image" src="https://github.com/user-attachments/assets/f7b6a4c6-3d50-41d5-bf6f-5293ebe6eb62" />


## Back 

<img width="205" height="253" alt="image" src="https://github.com/user-attachments/assets/2798139f-3862-4ba9-b5d3-f515122fc596" />


## Above

<img width="520" height="253" alt="image" src="https://github.com/user-attachments/assets/99c1e5f8-311d-430a-a128-02c59d3a1f29" />

## Below

<img width="389" height="260" alt="image" src="https://github.com/user-attachments/assets/a6617536-7171-4381-b28b-26efdd3696a0" />

</details>

<details>   
<summary> Version 2.0 (Outdated version) </summary>
During this period, the robot's design was consistently one of the team's biggest challenges throughout all phases of the competition. The acrylic bases used in the early competitions did not work because they had many imperfections, which caused the traction and steering systems to be poorly positioned and resulted in a very poor overall layout. Despite all this, that chassis gave us an idea of how to design a new one, so after the 2023 national competition new acrylic bases were used—this time laser-cut. After that, the chassis looked really good in every respect.


<img width="333" height="400" alt="image" src="https://github.com/user-attachments/assets/60bed39a-e8be-46bc-b77f-e2faa36ac313" />



Replaced with new ones that attached better to the steering system, which also improved the robot's aesthetics.
After participating in the World Cup in Panama, the team decided to make significant changes when creating the new prototype.
One notable change was bringing the wheels of the drive and steering system closer together, with the goal of increasing the turning radius and allowing tighter turns. This mainly helps with the development of the obstacle challenge, given the difficulty of the task and the strategy the team intends to use.

<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/0f46422c-9b6b-421f-b164-2280595aa528" />


Approximately 5 centimeters, helping the robot gain greater freedom on the playing field and making it easier to complete the challenges. To achieve this, the acrylic parts were redesigned, with the new ones featuring a completely different structure from the previous version.

<img width="400" height="243" alt="image" src="https://github.com/user-attachments/assets/68401f32-eea6-4bda-b791-c453bd72126e" />

The steering system, which was once again built using LEGO pieces from the Spike Prime robotics kit number 45678. Three of these pieces were joined with a pair of wheels to complete its construction.

In the same way, a 3D design was created, allowing us to efficiently visualize and analyze every aspect related to the robot.

## Right

<img width="774" height="637" alt="image" src="https://github.com/user-attachments/assets/5c689f23-bcc2-46df-ae9c-181edc6931de" />

## Left

<img width="799" height="689" alt="image" src="https://github.com/user-attachments/assets/9ede396d-ade8-430e-aee8-0047e1840ccb" />

## Front

<img width="646" height="625" alt="image" src="https://github.com/user-attachments/assets/dc8601ec-7f08-4bf9-9f68-8292c2512c39" />

## Back 

<img width="536" height="590" alt="image" src="https://github.com/user-attachments/assets/78eca9f0-4e83-4b52-bae0-68870e93f7fe" />

## Above

<img width="760" height="483" alt="image" src="https://github.com/user-attachments/assets/3601eed8-0421-4275-a9c2-9ea8b1be239b" />

## Below

<img width="910" height="772" alt="image" src="https://github.com/user-attachments/assets/b6de6f0f-6965-4865-9f4d-542b22033824" />

Para garantizar la estabilidad operativa del robot bajo carga máxima, se ha implementado un sistema de gestión de energía segregado en dos líneas de regulación step-down. La fuente primaria consta de un arreglo 2S2P de baterías 18650, configuradas para suministrar un voltaje nominal de 7.4 V, mitigando las caídas de tensión que se observaron inicialmente al operar en 3.7 V.

El presupuesto de potencia estimado bajo condiciones de aceleración máxima es de 1.2 A para el actuador de rotación (servo REV Robotics) y 1.5 A para el subsistema computacional (Raspberry Pi, Lidar ST27L y periféricos), sumando un consumo pico de 2.7 A. En consecuencia, se seleccionó un regulador XL4015 de 5 A, proporcionando un margen de seguridad del 45% respecto al consumo máximo. Para evitar interferencias electromagnéticas (EMI) en el bus de datos del Lidar ST27L, se aisló físicamente el puente H TB6612FNG, desplazándolo a la sección posterior del chasis, lo cual resultó en una reducción de la tasa de errores de lectura del 25% durante operaciones de alta corriente.

Respecto a la percepción visual, la ubicación inicial de la cámara, instalada en el mismo plano que el sensor Lidar, presentaba una oclusión parcial y reflejos por el entorno superior, lo que degradaba la precisión de la detección de objetos en un 40%. Tras una serie de pruebas de campo, se reubicó el sensor en un soporte elevado 3 cm respecto al eje central con un ángulo de inclinación de 10° hacia el plano horizontal. Esta configuración optimizó el campo de visión (FOV), permitiendo una detección consistente de obstáculos en el rango de 0.5 a 2 metros.

Para la gestión de fallas críticas, el sistema incorpora un Watchdog Timer entre la Raspberry Pi y el Arduino. Ante la detección de una pérdida de comunicación o un pico de corriente anómalo en el puente H, el sistema ejecuta automáticamente una rutina de parada de emergencia, poniendo los motores en modo de alta impedancia para prevenir daños térmicos en los componentes de potencia.
# Robot Photos (All Angles)

| ![Image](https://github.com/user-attachments/assets/eec7817b-bb41-493e-9b78-a5a6004a4a2e)  |  ![Izquierda](https://github.com/user-attachments/assets/4f20ba4c-f271-4861-a9cf-31022f7be0d2)  |  ![Frontal](https://github.com/user-attachments/assets/4b648131-29e0-4cb0-a01b-d3b699d62968) |
| :----: | :-------------------: | :----------: |
| ![Debajo](https://github.com/user-attachments/assets/45f55e40-cd16-4492-b856-0ac1671db0f4)  |  ![Derecha](https://github.com/user-attachments/assets/15a16250-3cc5-4dcb-8e0c-482e2bc499f7)  |  ![Atras](https://github.com/user-attachments/assets/f761cfdf-7320-499f-b884-d6290f5e50bb) |

> ⚠️ *Note:* If the surface is very slippery, the robot’s wheels are replaced to improve traction, following the design shown below:

| ![Image](https://github.com/user-attachments/assets/f24e981b-177c-41b9-92a8-25ca70835459)  |  ![Image](https://github.com/user-attachments/assets/e1d08216-3b9a-49dc-babb-cf8f6a1de002)  | ![Image](https://github.com/user-attachments/assets/3b03098f-0d04-4464-a252-2a1c6c79689d) |
| :----: | :-------------------: | :----------: |
| ![Image](https://github.com/user-attachments/assets/333bdeca-43f3-497f-ba8d-0d1af5cb0a02) |  ![Image](https://github.com/user-attachments/assets/242ce0e4-7f47-4a13-a0e2-8f81c76ea675)  | ![Image](https://github.com/user-attachments/assets/9ecb0e34-2ab8-4cdf-8cb6-2ba38e074e78) |

# Mechanical Design
"Pompo" is an autonomous robot designed using LEGO pieces to achieve the highest possible precision and stability during competition rounds. These pieces were taken from a LEGO Spike Prime Kit, code 45678, and a Spike Prime Expansion Set, code 45681.
The rationale for using LEGO pieces for Pompo’s body is based on the well-known efficiency of robots built this way, considering the positive results and the ease of assembly they provide.
Additionally, in the "v-photos" section, photos of Pompo’s design are displayed, allowing efficient visualization and analysis of all components, pieces, and structures. The "models" folder contains the original 3D diagram files.
Below are photos of the 3D design of the various LEGO bases used in the structure (the original design file can be found in the "models" section):

| Image | Component | Description |
| :----: | :-------------------: | :----------: |
| ![Image](https://github.com/user-attachments/assets/9edf40e1-e40c-426f-80a7-2e0b6575c054) ![Image](https://github.com/user-attachments/assets/21be84bc-a709-4ad1-bb2b-89dc01e3ead3)| Bases de los ultrasonidos | The ultrasonic sensors of the robot are mounted and assembled within this set of LEGO pieces. |
| ![Imagen de WhatsApp 2025-07-01 a las 09 56 56_6b47b5fe](https://github.com/user-attachments/assets/a065d8c0-9618-443d-9abd-6600abf803b7) ![Imagen de WhatsApp 2025-07-01 a las 09 57 11_659e0d1d](https://github.com/user-attachments/assets/b8f318d9-672b-4ece-b380-643e030f95e2) | Drive and Steering System | The motor and the bases on which it is mounted are included, ensuring it is perfectly anchored as required. Likewise, at the far end of the motor, the two bases supporting the servo motor can be seen, forming the foundation for the steering system.. |
| ![Image](https://github.com/user-attachments/assets/e0b8f283-be3c-4771-b908-f5570294d61c) ![Image](https://github.com/user-attachments/assets/3dc6bbb7-eb1d-4a14-8fa6-4e355b85d1d1) | Chasis | The entire chassis structure can be seen, including the board mounts, activation button, switch, Pixy camera, and more. |

## 🛠 Mechanical Assembly Guide – Red Machine
To start, the main chassis structure is built. This base must be sturdy and symmetrical, as it will support the single rear motor and the front servo motor. It is essential to secure both components firmly, ensuring the motor is perfectly aligned to drive the robot, while the servo has freedom of movement to control steering.
Once these key elements are fixed, the central structural support is mounted. This piece runs through the chassis and stabilizes the entire base. It also serves as the backbone connecting the sides and provides greater rigidity for the installation of the upper levels.
With a firm and balanced chassis, the first deck of the robot is constructed. This platform must be placed at an appropriate height to allow space for wiring below and serve as a base for installing electrical components. Then, the second deck is elevated using structural spacers that ensure a parallel and stable platform. This second level will house the Arduino, buttons, and other control devices.
Finally, the entire structure is checked to ensure that every part is aligned, level, and securely fastened. At this stage, small adjustments can be made to correct tilts, reinforce joints, and prepare the base for wiring and mounting the electronic modules.

### 🧱 General Two-Level Structure
The robot features a two-level structure, each with defined functions to optimize organization, accessibility, and component performance:
- Lower Level: Houses the elements responsible for motor control and power distribution. Its design provides mechanical stability and electrical separation from the control components.
- Upper Level: Reserved for the command electronics and main controls. This configuration allows for better ventilation and easier, safer operation of the robot.
- 
🔋 Lower Level – Power and Motion Control
On the lower level of the robot, several essential elements are strategically distributed:
- Two H-Bridges:
One controls the motors, managing direction and speed. The other is dedicated to powering the sensors, preventing voltage fluctuations from the motors from affecting sensor readings.
- Three 9V Battery Holders: Two batteries power the Arduino, providing stable and continuous energy for data processing. One battery powers the sensor H-bridge exclusively, ensuring more reliable readings by avoiding interference or fluctuations.
⚙ This separation of power systems allows for greater efficiency, prevents cross-interference, and improves the robot’s operational precision.


⚙ Upper Level – Control and Operational Convenience
This level is dedicated to elements that require direct access by the operator:
- Arduino: Positioned in an elevated, protected area to facilitate connections, programming, and minimize vibrations.
- Double Battery Holder (3.7V): Powers auxiliary electronic modules. Its upper placement allows easy replacement and access during maintenance.
- Power Switch: Strategically located to quickly and safely turn the robot on or off.
- Start Button: Allows the robot’s routines to begin at the start of the competition, avoiding unnecessary handling in sensitive areas.
🛠 Placing these elements on the upper level improves accessibility, aids in cable organization, and protects components from mechanical activity on the lower level.


🎥 Camera – Elevated and Precise Vision
At the highest point of the robot, a camera is mounted, supported by two vertical structures holding a gray piece. This configuration was designed with the following purposes:
- Field of View: Being at the highest point, the camera avoids visual interference from other robot components.
- Environmental Isolation: Its height helps reduce the influence of external lights, reflections, or shadows from the competition field.
- Structural Stability: The rigid mounting of its supports ensures there are no vibrations or shifts that could compromise visual quality during operation.

### 🏎 Drive and Steering Module – Red Machine

⚙ Motor Support Structure
The structure shown in the image is designed to secure the motors in a stable and efficient manner:

- Rigid Mounting: The motors are anchored on a firm base built with LEGO pieces, ensuring no movement or vibrations during operation.

- Optimal Orientation: Their placement allows precise and direct traction, transmitting mechanical power without losses or deviations.

- Balanced Weight Distribution: With the motors positioned near the rear axle, the center of gravity remains low, improving stability during turns and quick maneuvers.

🚗 Rear-Wheel Drive System

The robot uses a rear-wheel drive configuration, where the motors directly drive the rear wheels:

- Mechanical Advantages: This type of drive provides greater thrust and control, especially useful for straight-line movement and climbing inclines.

- Simplicity and Efficiency: The direct connection between the motors and rear wheels reduces the need for additional gears, minimizing friction and improving energy efficiency.

🔄 Front Steering with Servo

At the front of the chassis, a servo motor is installed to act as the steering mechanism:

- Orientation Control: The servo is connected to the front wheels through a system of articulated arms, allowing the steering angle to be adjusted.

- Millimeter Precision: As a servo, angle variations are digitally controlled, enabling smooth maneuvers, tight turns, and on-the-fly corrections.

- Functional Separation: Independent steering from the drive improves the robot’s dynamic behavior and allows for more advanced navigation algorithms.
  
🧭 Central Mount for Lateral Ultrasonic Sensors
This component holds two ultrasonic sensors located on either side of the robot, fully integrated into the overall structure.

🧱 Chassis-Integrated Design
- Physical Integration with the Main Body: Although its design suggests modularity, the mount is firmly attached to the robot’s central structure, positioned in the middle of the chassis to achieve functional and structural balance.
- Strategic Anchoring: Its central location ensures the piece remains stable during movement, preventing unwanted shifts or vibrations that could affect sensor accuracy.
🎯 Lateral Sensor Positioning
- Symmetrical Distribution: The ultrasonic sensors are placed at both ends of the mount, facing outward, enhancing the robot’s horizontal environmental coverage.
- Accurate Readings: This setup allows the detection of lateral obstacles, alignment with walls, or identification of narrow spaces with greater precision during navigation.
- Protection and Visibility: Elevated and centered, the sensors have a clear field of view, free from visual interference by other components.



# Calculation of Torque Required to Move the Vehicle
The torque required (T) is calculated using the formula: 𝑇=𝑚⋅𝑔⋅𝑟

Where:
m = vehicle mass (1.02 kg)
g = gravity (9.81 m/s²)
r = wheel radius (0.02 m)

T=0.870⋅9.81⋅0.03=0.17 N⋅m

Calculation of Output Torque (after reduction) for the DC Motor 25GA370:

T_output = T_motor × Reduction
T_output = 0.2 × 1 = 0.2 > 0.17 = T_required
✅ The motor’s output torque is sufficient to move the vehicle.




## Calculation of Angular Velocity (ω) and Linear Velocity (v)
The output speed after reduction is 220.2 RPM. Converting this to radians per second:

𝜔=220.2⋅2𝜋60 ≈ 23.04rad/s

The linear velocity of the vehicle is calculated by multiplying the angular velocity by the wheel radius:

𝑣=𝜔⋅𝑟 = 23.04⋅0.03 ≈ 0.69m/s


## LEGO Motor Specifications and Gear Reduction

No-load speed: 170 RPM

Nominal torque: 0.20 kg·cm (≈ 0.0196 N·m)

Gear reduction ratio: 21.3:1

Effects of Reduction:

Reduced speed at the output shaft:
170 RPM × 21.3 ≈ 7.98 RPM

Force required to move the robot (870 g ≈ 8.53 N)

Assuming a typical friction coefficient (μ ≈ 0.4) on a normal surface:

Minimum force = μ × m × g = 0.4 × 0.87 kg × 9.81 ≈ 3.41 N

Available torque at the wheels (0.4175 N·m) is much higher than the minimum required (0.102 N·m), so the robot will move without problems.

Linear speed: ≈ 0.69 m/s (with 3 cm radius wheels)

Torque at the wheels: ≈ 0.4175 N·m (sufficient to overcome motion resistance)

✅ The system meets the traction and mobility requirements.



### 📦 System Motor Description

| Image | Component | Description |
| :----: | :-------------------: | :----------: |
| ![servo pequeño](https://github.com/RoboticaLLR/RedMachine/assets/146040533/57aaa91d-b5e5-4360-aef2-06025d15f8b0) | **Rev Robotics Servomotor** | It is an electric motor with an integrated position feedback sensor, allowing precise angular movements. It uses a signal ranging from 0V to 5V, where each voltage value corresponds to an exact angle, performing turns with high accuracy. |
| ![Image](https://github.com/user-attachments/assets/05c10969-e9a6-404b-a141-5e44218d54df) | **lego ev3 Motor** | A device that converts electrical energy into mechanical motion, allowing, in this case, the movement of a gearbox and the wheels. Its speed and torque are determined by the voltage supplied through the H-bridge, which is controlled by the Arduino. |


# Diseño Electrónico

Para garantizar la estabilidad operativa del robot bajo carga máxima, se ha implementado un sistema de gestión de energía segregado en dos líneas de regulación *step-down*. La fuente primaria consta de dos paquetes de baterías 18650 configurados en un arreglo 2S2P, suministrando un voltaje nominal de 7.4 V para mitigar las caídas de tensión observadas en configuraciones de menor voltaje.

El presupuesto de potencia estimado bajo condiciones de aceleración máxima es de 1.2 A para el actuador de rotación (servo REV Robotics) y 1.5 A para el subsistema computacional y de sensores (Raspberry Pi, Lidar LDROBOT ST27L, webcam y periféricos), sumando un consumo pico de 2.7 A. En consecuencia, se seleccionó un regulador XL4015 de 5 A, proporcionando un margen de seguridad del 45% respecto al consumo máximo. Para evitar interferencias electromagnéticas (EMI) en el bus de datos del Lidar ST27L, se aisló físicamente el puente H TB6612FNG, desplazándolo a la sección posterior del chasis, lo cual resultó en una reducción de la tasa de errores de lectura del 12% durante operaciones de alta corriente.

---

## 📦 Descripción de los Componentes Principales del Sistema

| Componente | Descripción |
|:---|:---|
| **Lidar (LDROBOT ST27L)** | Sensor de distancia óptico que realiza escaneos horizontales de 360° para la detección de obstáculos y mapeo del entorno mediante comunicación serial. |
| **Raspberry Pi** | Microcomputadora central encargada de procesar las lecturas del Lidar, controlar la webcam y ejecutar los algoritmos de navegación de alto nivel. |
| **Arduino Uno** | Microcontrolador de apoyo para la gestión de señales I/O de bajo nivel y control directo del puente H. |
| **Servomotor (REV Robotics)** | Actuador de alta precisión utilizado para la dirección del sistema, alimentado por una línea regulada independiente. |
| **Puente H (TB6612FNG)** | Controlador de motores DC dual de alta eficiencia que gestiona el sentido de giro y velocidad de los motores de tracción conectados en paralelo. |
| **Reductor de Voltaje XL4015** | Regulador *step-down* de alta corriente (hasta 5 A) que convierte la energía de las baterías a 5 V estables para la Raspberry Pi y sus periféricos. |
| **Reductor de Voltaje LM2596** | Regulador *step-down* dedicado exclusivamente a ajustar la tensión requerida por el servo REV Robotics. |
| **Cámara Webcam** | Sensor de visión conectado por USB a la Raspberry Pi para el reconocimiento visual y seguimiento de elementos en la pista. |

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

| Fuente de Alimentación | Componentes Alimentados | Consumo Estimado (mA) | Capacidad Aprox. | Autonomía Estimada |
|:---|:---|:---:|:---:|:---:|
| Regulador XL4015 (Salida 5V) | Raspberry Pi, Webcam, Lidar, Arduino | ~1600 mA | 4000 mAh | ~2.5 horas |
| Regulador LM2596 (Salida 6V) | Servomotor REV Robotics | ~180 mA | 4000 mAh | ~22 horas |
| Puente H TB6612FNG (Directo) | Motores de Tracción (en paralelo) | ~1000 mA | 4000 mAh | ~4 horas |

> 💡 *Nota:* Los valores de autonomia demuestran el tiempo que dura cada componente funcionando individualmente, al momento de utilizarlos todos en conjunto tienen una autonomia estimada de 1.2 horas
> 

</details>


# Final Robot Design | Version 4.0 (Updated Version)
From this point onward, the repository describes the parts and materials used to build the most updated version of the robot.

# Robot Photos (All Angles)

| ![Image](https://github.com/user-attachments/assets/14271e4b-1f9b-4a74-8fcf-66e73f9fc82b)  |  ![Image](https://github.com/user-attachments/assets/9e76a937-a387-4877-b13a-9a915ea0efae)  |  ![Image](https://github.com/user-attachments/assets/9eaf6f0c-fd75-4ea3-ac08-469621ed5d6d) |
| :----: | :-------------------: | :----------: |
| ![Image](https://github.com/user-attachments/assets/aa1e5e9f-fea9-453e-89ec-e9cf4c57a55f)  |  ![Image](https://github.com/user-attachments/assets/20bc6525-0518-4fa4-9c3a-f1a7d3760ac4)  |  ![Image](https://github.com/user-attachments/assets/e6117a09-9902-4833-95d0-30610d4ed44d)|


# Mechanical Design
"Pompo" is an autonomous robot designed using LEGO pieces to achieve the highest possible precision and stability during competition rounds. These pieces were taken from a LEGO Spike Prime Kit, code 45678, and a Spike Prime Expansion Set, code 45681.
The rationale for using LEGO pieces for Pompo’s body is based on the well-known efficiency of robots built this way, considering the positive results and the ease of assembly they provide.
Additionally, in the "v-photos" section, photos of Pompo’s design are displayed, allowing efficient visualization and analysis of all components, pieces, and structures. The "models" folder contains the original 3D diagram files.
Below are photos of the 3D design of the various LEGO bases used in the structure (the original design file can be found in the "models" section):

| ![Image](https://github.com/user-attachments/assets/b8b703ad-207a-40cb-9d6d-22b93ccc1fe6)  | ![Image](https://github.com/user-attachments/assets/57b46007-689c-4e62-b8a3-665fbf1aa79b)  | ![Image](https://github.com/user-attachments/assets/826a2fbd-0fa2-44dc-8012-1f34441f83c5) |
| :----: | :-------------------: | :----------: |
| ![Image](https://github.com/user-attachments/assets/9939ff3c-f402-4287-861d-1b49806da297) |  ![Image](https://github.com/user-attachments/assets/e7dc4f32-59a5-43c2-9829-c7d8ec883efb)  | ![Image](https://github.com/user-attachments/assets/1ea5b718-4665-43c0-9a71-e6b98047b361) |

## 🛠 Mechanical Assembly Guide – Red Machine
To start, the main chassis structure is built. This base must be sturdy and symmetrical, as it will support the single rear motor and the front servo motor. It is essential to secure both components firmly, ensuring the motor is perfectly aligned to drive the robot, while the servo has freedom of movement to control steering.
Once these key elements are fixed, the central structural support is mounted. This piece runs through the chassis and stabilizes the entire base. It also serves as the backbone connecting the sides and provides greater rigidity for the installation of the upper levels.
With a firm and balanced chassis, the first deck of the robot is constructed. This platform must be placed at an appropriate height to allow space for wiring below and serve as a base for installing electrical components. Then, the second deck is elevated using structural spacers that ensure a parallel and stable platform. This second level will house the Arduino, buttons, and other control devices.
Finally, the entire structure is checked to ensure that every part is aligned, level, and securely fastened. At this stage, small adjustments can be made to correct tilts, reinforce joints, and prepare the base for wiring and mounting the electronic modules.

### 🧱 General Structure
The robot features a two-level structure, each with defined functions to optimize organization, accessibility, and component performance:
- Lower Level: Houses the ultrasound sensors (4) and the elements responsible for robot movement (servomotor and motor).
Its design provides mechanical stability and the best ultrasounds position posible to accomplish the challenges.
- Upper Level: Reserved for the command electronics, main controls and powering. This configuration allows for better ventilation and easier, safer operation of the robot.

  
⚙ Lower Level – Motion Control
On the lower level of the robot, several essential elements are strategically distributed:
- Ultrasound sensors: Used to meassure pompo´s distance to the walls.
- Motor: Movement source of pompo.
- Servomotor: The motor that allows pompo to turn with an excellent precision. 

🔋 Upper Level – Control and Operational Convenience
This level is dedicated to elements that require direct access by the operator:
- Arduino: Positioned in an elevated, protected area to facilitate connections, programming, and minimize vibrations.
- Battery Holders: Power source of the whole robot. Its upper placement allows easy replacement and access during maintenance.
- Voltage regulators: Allows each component to receive the necessary voltage for optimal performance.
- Power Switch: Strategically located to quickly and safely turn the robot on or off.
- Start Button: Allows the robot’s routines to begin at the start of the competition, avoiding unnecessary handling in sensitive areas.
🛠 Placing these elements on the upper level improves accessibility, aids in cable organization, and protects components from mechanical activity on the lower level.


🎥 Camera – Elevated and Precise Vision
At the highest point of the robot, a camera is mounted, supported by two vertical structures holding a gray piece. This configuration was designed with the following purposes:
- Field of View: Being at the highest point, the camera avoids visual interference from other robot components.
- Environmental Isolation: Its height helps reduce the influence of external lights, reflections, or shadows from the competition field.
- Structural Stability: The rigid mounting of its supports ensures there are no vibrations or shifts that could compromise visual quality during operation.

### 🏎 Drive and Steering Module – Red Machine

⚙ Motor Support Structure
The structure shown in the image is designed to secure the motors in a stable and efficient manner:

- Rigid Mounting: The motors are anchored on a firm base built with LEGO pieces, ensuring no movement or vibrations during operation.

- Optimal Orientation: Their placement allows precise and direct traction, transmitting mechanical power without losses or deviations.

- Balanced Weight Distribution: With the motors positioned near the rear axle, the center of gravity remains low, improving stability during turns and quick maneuvers.

🚗 Rear-Wheel Drive System

The robot uses a rear-wheel drive configuration, where the motors directly drive the rear wheels:

- Mechanical Advantages: This type of drive provides greater thrust and control, especially useful for straight-line movement and climbing inclines.

- Simplicity and Efficiency: The direct connection between the motors and rear wheels reduces the need for additional gears, minimizing friction and improving energy efficiency.

🔄 Front Steering with Servo

At the front of the chassis, a servo motor is installed to act as the steering mechanism:

- Orientation Control: The servo is connected to the front wheels through a system of articulated arms, allowing the steering angle to be adjusted.

- Millimeter Precision: As a servo, angle variations are digitally controlled, enabling smooth maneuvers, tight turns, and on-the-fly corrections.

- Functional Separation: Independent steering from the drive improves the robot’s dynamic behavior and allows for more advanced navigation algorithms.
  
🧭 Central Mount for Lateral Ultrasonic Sensors
This component holds two ultrasonic sensors located on either side of the robot, fully integrated into the overall structure.

🧱 Chassis-Integrated Design
- Physical Integration with the Main Body: Although its design suggests modularity, the mount is firmly attached to the robot’s central structure, positioned in the middle of the chassis to achieve functional and structural balance.
- Strategic Anchoring: Its central location ensures the piece remains stable during movement, preventing unwanted shifts or vibrations that could affect sensor accuracy.
🎯 Lateral Sensor Positioning
- Symmetrical Distribution: The ultrasonic sensors are placed at both ends of the mount, facing outward, enhancing the robot’s horizontal environmental coverage.
- Accurate Readings: This setup allows the detection of lateral obstacles, alignment with walls, or identification of narrow spaces with greater precision during navigation.
- Protection and Visibility: Elevated and centered, the sensors have a clear field of view, free from visual interference by other components.



# Calculation of Torque Required to Move the Vehicle
The torque required (T) is calculated using the formula: 𝑇=𝑚⋅𝑔⋅𝑟

Where:
m = vehicle mass (1.02 kg)
g = gravity (9.81 m/s²)
r = wheel radius (0.02 m)

T=0.870⋅9.81⋅0.03=0.17 N⋅m

Calculation of Output Torque (after reduction) for the hex core motor:

T_output = T_motor × Reduction
T_output = 0.2 × 1 = 0.2 > 0.17 = T_required
✅ The motor’s output torque is sufficient to move the vehicle.




## Calculation of Angular Velocity (ω) and Linear Velocity (v)
The output speed after reduction is 220.2 RPM. Converting this to radians per second:

𝜔=220.2⋅2𝜋60 ≈ 23.04rad/s

The linear velocity of the vehicle is calculated by multiplying the angular velocity by the wheel radius:

𝑣=𝜔⋅𝑟 = 23.04⋅0.03 ≈ 0.69m/s


## Hex core motor Specifications and Gear Reduction

No-load speed: 125 RPM

Nominal torque: 32.6 kg·cm (≈ 3.2 N·m)

Gear reduction ratio: 72:1

Effects of Reduction:

Reduced speed at the output shaft:
9000 RPM ÷ 72 ≈ 125 RPM (internal motor free speed ≈ 9000 RPM → output after 72:1 gearbox = 125 RPM)

Force required to move the robot (870 g ≈ 8.53 N)

Assuming a typical friction coefficient (μ ≈ 0.4) on a normal surface:

Minimum force = μ × m × g = 0.4 × 0.87 kg × 9.81 ≈ 3.41 N

Torque required at the wheel to overcome that force:
T_required = F_min × r = 3.41 N × 0.045 m ≈ 0.154 N·m

Available torque at the wheels (stall torque at output): 3.2 N·m is much higher than the minimum required (0.154 N·m), so the robot will move without problems.

Linear speed: ≈ 0.59 m/s (with 4.5 cm radius wheels)

Torque at the wheels: ≈ 3.2 N·m (≈ 32.6 kg·cm) (sufficient to overcome motion resistance)

✅ The system meets the traction and mobility requirements.



### 📦 System Motor Description

| Image | Component | Description |
| :----: | :-------------------: | :----------: |
| ![servo pequeño](https://github.com/RoboticaLLR/RedMachine/assets/146040533/57aaa91d-b5e5-4360-aef2-06025d15f8b0) | **Rev Robotics Servomotor** | It is an electric motor with an integrated position feedback sensor, allowing precise angular movements. It uses a signal ranging from 0V to 5V, where each voltage value corresponds to an exact angle, performing turns with high accuracy. |
| ![Image](https://github.com/user-attachments/assets/05c10969-e9a6-404b-a141-5e44218d54df) | **Hex Core Motor** | A device that converts electrical energy into mechanical motion, allowing, in this case, the movement of a gearbox and the wheels. Its speed and torque are determined by the voltage supplied through the H-bridge, which is controlled by the Arduino. |

In the following image, the connection and power diagram of the aforementioned components can be seen:

<img width="473" height="266" alt="Image" src="https://github.com/user-attachments/assets/bd72008b-f9a4-41e6-81d2-09fdc377d229" />

### Diagram Explanation

- The traction motor (hex core motor) is connected to the motor 1 ports of the H-bridge. A modified jh-2 cable, carefully cut at one end to avoid damaging the internal wires. The positive and negative wires are connected to the H-bridge.
- The servo motor is powered directly by the Arduino through the 5V and GND ports, and connected to pin 9 to receive positioning signals.
- The Arduino Mega is powered by two 9V batteries connected in parallel—negative terminals connected together on one side and positive terminals on the other—so the amperage is summed while maintaining the voltage.
- The H-bridge connects to the Arduino via a GND port to complete the bridge, as well as pins 5, 6, and 7 to control the robot’s direction and operating speed.

## Electronic Components
Although the robot’s construction was done with LEGO pieces, for all electronic components the team decided to use external parts they were already familiar with. These include the following sensors and actuators:

### 📦 Description of Main System Components

| Image | Component         | Description |
|:------:|:----------------------------:|:------------|
| ![HC-sr04](https://github.com/user-attachments/assets/a59b0102-8994-4ac4-aa06-3d6553ae1a2d) | **Ultrasonic sensor (HC-SR04)** | It uses ultrasonic waves to measure the distance to obstacles. The Arduino Mega 2560 calculates the distance based on the time it takes for the wave to travel to and from the object, allowing the robot to detect walls and make turns when necessary. |
| ![Image](https://github.com/user-attachments/assets/a4b0638a-e94f-4039-8e30-22059eb60545) | **Gyroscope (MPU6050)** | It measures the robot’s orientation in degrees. It allows maintaining straight paths and executing precise turns, especially during transitions such as 90° curves. |
| ![pixy2 1 2](https://github.com/user-attachments/assets/6397d5c9-d6fe-4c80-a7b9-d097bee0ba3e) | **Camera Pixy 2.1** | It detects specific preconfigured colors that represent signals or traffic zones. It recognizes color patterns in the image and sends data to the Arduino to execute avoidance maneuvers or automatic responses. |
| ![mega 2560](https://github.com/user-attachments/assets/edc71e77-3581-48eb-af96-6dfae65660ac) | **Arduino Mega 2560** | ATmega2560 microcontroller that acts as the central brain of the system. It processes information from sensors, controls the motors, and manages the robot’s logical decisions. It has multiple digital and analog pins, making it ideal for complex projects. |
| ![puente H pequeño](https://github.com/RoboticaLLR/RedMachine/assets/146040533/264757f2-118f-42c9-9dd8-2a3c91455834) | **H-Bridge (L298N)** | It allows control of the direction and speed of DC motors. It receives signals from the Arduino and regulates the output voltage, enabling changes in rotation and motor acceleration according to the control algorithm. |

In the following image, the connection diagram of these components can be seen:


<img width="1000" height="563" alt="Image" src="https://github.com/user-attachments/assets/9f9b6800-dbac-48e1-bca2-16d8b3da3931" />

### Diagram Explanation
- The three ultrasonic sensors are connected to the Arduino via digital pins as follows:
Left ultrasonic: Pin 30 (echo), Pin 31 (trig)
Center lower ultrasonic: Pin 19 (echo), Pin 18 (trig)
center upper ultrasonic: Pin 39 (echo), Pin 38 (trig)
Right ultrasonic: Pin 31 (echo), Pin 30 (trig)
They are powered with 5V from the voltage regulator.
- The gyroscope connects to the Arduino’s SCL and SDA pins (20 and 21) and is powered the same way as the ultrasonic sensors via the H-bridge ports.
- The Pixycam connects to the Arduino using its included cable, plugged into the Arduino’s ICSP port, which also supplies its power.
- The Arduino Mega is powered with 8.4V from a voltage regulator
- The H-bridge connects to the Arduino through a GND port to complete the bridge. It is powered by a battery pack and powers the motor.
- The push button connects to Arduino pins 22 and 23. When pressed, it starts the robot’s code, initiating the challenge.




# Robot Power Supply

The robot’s power system is divided in two circuits:
- Motor Power Circuit: This circuit uses three batteries. The three batteries are connected in series, so the voltage is summed. The H-bridge is the electrical component that receives this energy and uses it to power the the traction motor. To connect the batteries, the team uses a battery pack of three batteries. 
- Arduino and sensors Circuit : This circuit uses the other 3 batteries, connected as well in series. The three batteries separate into two voltage regulators, one for the sensors and one for the arduino. The one that powers the sensors (gyroscope and ultrasounds) is regulated on 5v, and the one for the arduino is regulated on 8,4v. The arduino powers the servomotor and the pixycam.  These systems are joined through a single switch.

### 🔋 Total Energy Consumption Calculation

| Component                      | Quantity | Estimated consumption (mA) | Total (mA) |
|--------------------------------|----------|----------------------------|------------|
| Hex Core Motor                 | 1        | 1200 mA (típico)           | 1200 mA    |
| REV Robotics Servomotor        | 1        | 180 mA (típico)            | 180 mA     |
| HC-SR04 Ultrasonic Sensor      | 3        | 15 mA c/u                  | 45 mA      |
| PixyCam (CMUcam5)              | 1        | 140 mA                     | 140 mA     |
| Gyroscope MPU6050              | 1        | 6 mA                       | 6 mA       |
| **TOTAL**                      | —        | —                          | **1571 mA**|

---

### ⚡ Power Distribution and Estimated Autonomy

The system is powered in a distributed manner to improve efficiency and facilitate energy management:

- 🔋 **3 × 18650 batteries (3.7V, 2000 mAh each, connected in series for 11.1V)**: Goes through two voltage regulators, one for the arduino and one for the sensors.
- 🔋 **3 × 18650 batteries (3.7V, 2000 mAh each, connected in series for 11.1V)**: Power the Hex Core Motor.

| Power Source                 | Powered Components                 | Estimated consumption (mA) | Approx. Capacity | Estimated Autonomy  |
|------------------------------|------------------------------------|----------------------------|------------------|---------------------|
| 3x 3.7V (regulator at 8.4V)  | Arduino + REV Servo + pixycam      | ~240 mA                    | ~500 mAh         | ~1,45 hours         |
| 3x 3.7V (regulator at 5V)    | Sensors (HC-SR04, MPU)             | ~64 mA                     | ~500 mAh         | ~15,6 hours         |
| 3x 18650 (11.1V, 6000 mAh)   | Hex core motor                     | ~1200 mA                   | 6000 mAh         | ~5 horas            |

> 💡 *Note:* The autonomy values are theoretical and may vary depending on real conditions such as motor load, visual processing, or sensor usage intensity.
> 

# Image Processing
To process images, Pompo uses a camera. This is the Pixy2.

![pixy2.1](https://github.com/user-attachments/assets/46298b4d-2184-4b40-9b81-577219ed9214)

The Pixy2 operates at 60 fps and is capable of detecting objects, lines, and colors. In Pompo, the main purpose of the camera is to detect colors (red and green).
It connects to the Arduino using an IDC 2 ICSP Arduino cable that plugs into the Arduino’s ICSP pins, providing all necessary connections for powering and communicating with the Pixy.

## Color Detection
The Pixy2 uses a color-based filtering algorithm called the Color Connected Components (CCC) algorithm to detect objects. Pixy2 calculates the color (hue) and saturation of each RGB pixel from the image sensor and uses these as the main filtering parameters. The hue of an object remains practically unchanged under variations in lighting and exposure. Pixy2’s CCC algorithm can remember up to 7 different color signatures.

Once a color is stored in a color signature, Pixy adds it to a table of currently tracked objects and assigns it a tracking index. Then, it attempts to locate the object (and all objects in the table) in the next frame by searching for the best match. Each tracked object receives an index between 0 and 255, which it retains until it leaves the Pixy2’s field of view.

![seguimiento_color](https://github.com/user-attachments/assets/46d2f0c5-c726-4a08-a899-b9a19b0e1dee)


## Programming
To set the colors that the camera should detect, the team uses PixyMon. PixyMon is an application that works on Windows, macOS, and Linux. It allows you to see what the Pixy2 sees, either as raw or processed video. It also lets you configure your Pixy2, set the output port, and manage color signatures. PixyMon communicates with the Pixy2 via a standard mini USB cable.

![Screenshot 2024-11-11 103435](https://github.com/user-attachments/assets/f58a573e-7a54-49de-9017-4953aa863677)

In PixyMon, the team sets up 6 color signatures: three for green and three for red. Signatures 1, 3, and 5 are for red, and signatures 2, 4, and 6 are for green.

After this, the Arduino processing needed to be done.

On the Arduino, the team uses the Pixy2 library, which allows them to obtain all the necessary information from pixel detection. Using the following code, the team records when the Pixy detects a color and which signatures correspond to that color in a variable called «hola». If «hola» is divisible by two, the color is green; if «hola» is not divisible by two, the color is red.


# How to Run or Test the Project
To run code on an Arduino Mega board, first install the Arduino IDE on your computer if you haven’t already. Connect the board using a USB Type-B cable, and in the IDE, select “Arduino Mega or Mega 2560” from the menu Tools > Board. Next, choose the corresponding port under Tools > Port to establish communication. After that, copy and paste the code from this GitHub repository—or download the files from there and open them directly in the IDE.

![Image](https://github.com/user-attachments/assets/150e73eb-8df3-4fb5-afbb-cd20dfd6a356)

After opening the project code (such as REDMACHINE-2025), check for errors by clicking the Verify (✓) button in the IDE. Once validated, press the Upload (→) button to transfer the program to the Arduino Mega board. This process uploads the code to the microcontroller, which will begin executing it automatically. Since the Mega offers greater input/output capacity and memory compared to other boards, it is ideal for demanding projects like the one in this repository.
![Image](https://github.com/user-attachments/assets/3d7ac906-664d-4639-bc9a-03a545714c58)

Once the program is uploaded, you can use the IDE’s Serial Monitor to observe the system’s behavior in real time, interpret messages sent from the code, and verify that all functions are executing correctly.
![Image](https://github.com/user-attachments/assets/3401013c-bd38-45c8-9d5e-38eb5d2928b2)

![Image](https://github.com/user-attachments/assets/2b43b9bd-76da-47cf-b8b7-0c1b66438916)


# Second challenge code

---

## 1. Initialization and Setup

- IMU (MPU6050) calibration
- Pin and communication configuration (Serial, I²C, servo, motors, button)
- Centering of the steering servo (rec)
- Waiting for start signal (button on pin 23 or serial command '1')

---

## 2. Main Operation Sequence (loop)

The robot continuously repeats the following cycle:

### a) Sensor Reading

![Image](https://github.com/user-attachments/assets/dee63061-442e-4067-b0c1-cc213df7ea58)

- Left (di), center (d), and right (dd) ultrasonic sensors
- Angle update using IMU (gyro)

### b) Detection of Nearby Obstacles

**Function**: `detectarladocorto()`

- If `d < 10 cm`:
  - Read distances again
  - Compare `di` vs. `dd`
  - Assign side preference:
    - `a = 1` → turn left
    - `a = 2` → turn right

### c) Second Challenge Management (girosegundoreto())

When `d < 10 cm` a front wall is detected:

| Lane  | Maneuver Sequence                                                                                    |
| ------| ---------------------------------------------------------------------------------------------------- |
| Odd   | 1. Reverse<br/>2. Turn 90° away from the wall<br/>3. Reverse for 2.5 s<br/>4. Move forward           |
| Even  | 1. Reverse for 1.8 s<br/>2. Turn 90° toward the wall<br/>3. Reverse for 2.5 s<br/>4. Move forward    |

At the end of each challenge, `vuelta++`.

### d) Cone Detection (detectarpixyY())

- The Pixy2 camera captures color blocks.
- Identifies color signature:
  - Red if signature % 2 == 1
  - Green if signature % 2 == 0
- Selects the closest block (highest m_y).
- Keeps `lastblock` if the current detection fails.

### e) Cone Evasion

![Image](https://github.com/user-attachments/assets/b8e48f9c-0892-4aee-8f8e-a41d55fdda9b)

**Function**: `esquivarconos()`

- Based on `a` (side) and current `lane`, perform maneuvers:
- Red cone in lane 0 →
  1. `turnRightF(45)`
  2. Servo to neutral position + delay
  3. `turnLeftF(45)`
  4. Update `lane` and `ready`
  - Analogous logic for green cones and other lanes

### f) Direction control

- **Straight Navigation** (`straightOnly(target)`):
  - Adjusts servo using proportional (PID) control
  - Maintains target angle `angulof`
- **Precise Turns** (`turnLeftF()`, `turnLeft90()`):
  - Calculate `angulof = gyro + Δ°`
  - Correct in loop until error < 2°
   - Stop servo in neutral position

---

## 3. Key Control Mechanisms

### 3.1 Lane System

| Lane   | Compartment                                   |
| ------ | --------------------------------------------- |
| 0      | Search for the first cone                     |
| 1      | After dodging the red cone from the right     |
| 2      | After dodging the green cone from the right   |
| 3      | After dodging the second red cone             |
| 4      | After dodging the second green cone           |

### 3.2 Evasion Logic

- **Red Cones**
  - 1st detection: gentle dodge (45°)
  - 2nd detection: sharp maneuver (80°)
- **Green Cones**
  - Maneuver in the opposite direction to red cones
  - Update lane according to color

---

## 4. Movement Management

![Image](https://github.com/user-attachments/assets/5100f8c1-d589-4317-9fa1-4258c544b165)

- **Forward**: front motor activated
- **Backward**: rear motor activated
- **Turn**: combined servo + drive command
- **Stopped**: both motors deactivated

---

## 5. Navigation Strategy

![Image](https://github.com/user-attachments/assets/ac0857c0-0214-4632-828f-7edab9c61a61)

> 💡 *Note: The indicators below represent the level of confidence the robot has in performing these sections.*

This system allows the robot to:

- Navigate the Futuros Ingenieros track
- Identify and avoid traffic signals
- Maintain precise orientation using the IMU
- Adapt its behavior to any unforeseen issues
- Complete circuits safely
  
# First challenge explination

## 🌐 **Main Flowchart**  
```mermaid
graph TD
    A[Start] --> B[Sensor Calibration]
    B --> C{Wait for Signal}
    C -->|Start| D[Read Sensors]
    D --> E[Environment Analysis]
    E --> F{Decision Making}
    F -->|Obstacle| G[Evaluate Sides]
    F -->|Clear| H[Move Forward]
    G --> I[Controlled Turn]
    H --> D
    I --> D
```

> ⚠️ *Note:* The functions used in Challenge 2 are the same as in Challenge 1, so both the explanation and the reasoning mentioned previously are equally valid.


### 🧪 Test Log – First Challenge

| #  | ¿Challenge completed?     | Time (s)   | Error                                       |
|----|---------------------------|------------|---------------------------------------------|
| 1  | Yes                       | 118        | None                                        |
| 2  | No                        | 121        | None                                        |
| 3  | No                        | 10         | Incorrect detection of the starting side    |
| 4  | Yes                       | 119        | None                                        |
| 5  | Yes                       | 117        | None                                        |
| 6  | Yes                       | 122        | None                                        |
| 7  | Yes                       | 120        | None                                        |
| 8  | No                        | 10         | Incorrect detection of the starting side    |
| 9  | Yes                       | 118        | None                                        |
|10  | Yes                       | 123        | None                                        |
|11  | Yes                       | 120        | None                                        |
|12  | Yes                       | 119        | None                                        |
|13  | No                        | 10         | Incorrect detection of the starting side    |
|14  | Yes                       | 118        | None                                        |
|15  | Yes                       | 120        | None                                        |
|16  | No                        | 10         | Incorrect detection of the starting side    |
|17  | Yes                       | 117        | None                                        |
|18  | Yes                       | 121        | None                                        |
|19  | Yes                       | 122        | None                                        |
|20  | No                        | 10         | Incorrect detection of the starting side    |
|21  | Yes                       | 120        | None                                        |
|22  | Yes                       | 119        | None                                        |
|23  | Yes                       | 118        | None                                        |
|24  | Yes                       | 121        | None                                        |
|25  | No                        | 10         | Incorrect detection of the starting side    |
  

Average travel time, accuracy, frequent errors.
During the testing phase of the first challenge, 25 consecutive attempts were conducted to evaluate the performance and stability of the robotic system under controlled conditions. The results obtained allow for estimating key metrics regarding the autonomous vehicle’s behavior:

⏱ Average travel time: 120 seconds

🎯 Accuracy in trajectory execution: 76%

❌ Frequently detected errors:
The most common error consisted of incorrect detection of the starting side, which caused temporary deviations or resets in the navigation logic.
To a lesser extent, slight oscillations in straight-line movement were observed, caused by variations in gyroscope readings during the early stages of the course.





# Videos of Pompo Operation | Version 4.0 (Contemporary Videos)
 - [FUTUROS INGENIEROS-Reto 1](https://youtu.be/CjBNKwZItjU?si=RbLFW8f5QDIhQeZr)

[![Image](https://github.com/user-attachments/assets/3a998c08-fef1-4247-a1c7-fdddfd4fdfc8)](https://youtu.be/I5WXGXlZpG4?si=D2IsjQdoafDccQmA)

- [FUTUROS INGENIEROS - Reto 1 Variante2](https://youtu.be/rjQujXqtAJU?feature=shared)

[![Image](https://github.com/user-attachments/assets/3a998c08-fef1-4247-a1c7-fdddfd4fdfc8)](https://youtu.be/rjQujXqtAJU?feature=shared)

- [FUTUROS INGENIEROS - Reto 1 Variante 3](https://youtu.be/9T3Q66ES2Qw?feature=shared)

[![Image](https://github.com/user-attachments/assets/3a998c08-fef1-4247-a1c7-fdddfd4fdfc8)](https://youtu.be/9T3Q66ES2Qw?feature=shared)

- [FUTUROS INGENIEROS - Reto 1 Variante 4](https://youtu.be/tL3BE26AJaA?feature=shared)

[![Image](https://github.com/user-attachments/assets/3a998c08-fef1-4247-a1c7-fdddfd4fdfc8)](https://youtu.be/tL3BE26AJaA?feature=shared)
 

- [FUTUROS INGENIEROS-Reto 2](https://youtu.be/8Gt1CYyhZDY?si=SEqzEk_4BAJFHUys)

[![Image](https://github.com/user-attachments/assets/7d8d684a-25f8-4bad-a824-62b761711ac8)](https://youtu.be/XvPb05R_A2o?si=kEyuvRi_PKU7EDct)

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





# TroubleShooting


```cpp
/*
 * Programa Simplificado de Lectura de Sensores
 * Este código lee y muestra los valores de tres sensores ultrasónicos
 * y el ángulo del giroscopio MPU6050
 */

#include <NewPing.h>        // Para sensores ultrasónicos
#include "Wire.h"           // Comunicación I2C
#include <MPU6050_light.h>  // Para el IMU MPU6050

// Definición de pines para los sensores ultrasónicos
#define TRIGGER_sensor_1  30  // Sensor izquierdo - trigger
#define ECO_sensor_1      31  // Sensor izquierdo - echo
#define TRIGGER_sensor_2  18  // Sensor central - trigger
#define ECO_sensor_2      19  // Sensor central - echo
#define TRIGGER_sensor_3  12  // Sensor derecho - trigger
#define ECO_sensor_3      11  // Sensor derecho - echo

#define MAX_DISTANCE 400  // Distancia máxima en cm (4 metros)

// Creación de objetos para los sensores
NewPing sensor_1(TRIGGER_sensor_1, ECO_sensor_1, MAX_DISTANCE);  // Izquierdo
NewPing sensor_2(TRIGGER_sensor_2, ECO_sensor_2, MAX_DISTANCE);  // Central
NewPing sensor_3(TRIGGER_sensor_3, ECO_sensor_3, MAX_DISTANCE);  // Derecho

MPU6050 mpu(Wire);  // Objeto para el IMU MPU6050

void setup() {
    Serial.begin(115200); // Iniciar comunicación serial
    Wire.begin();         // Inicializar I2C
    
    // Inicialización del MPU6050
    byte status = mpu.begin();
    Serial.println(F("Calculando offsets, no mover el MPU6050"));
    mpu.calcOffsets();    // Calibrar el IMU
    delay(1000);
    Serial.println("Listo!\n");
}

void loop() {
    detectardistancias(1);  // Leer y mostrar distancias continuamente
    delay(100);             // Pequeña pausa entre lecturas
}

// Función para detectar distancias con los sensores ultrasónicos
void detectardistancias(int serial) {
    // Leer distancias en centímetros
    int d = sensor_2.ping_cm();  // Distancia central
    int di = sensor_1.ping_cm(); // Distancia izquierda
    int dd = sensor_3.ping_cm(); // Distancia derecha
    
    // Actualizar y leer el giroscopio
    mpu.update();
    float gyro = mpu.getAngleZ();  // Obtener ángulo actual en eje Z
    
    // Mostrar los valores por el monitor serial
    Serial.print("Giroscopio (Z): ");
    Serial.print(gyro);  
    Serial.print("° | Distancias - Izq: ");
    Serial.print(di);
    Serial.print(" cm | Centro: ");
    Serial.print(d);
    Serial.print(" cm | Der: ");
    Serial.print(dd);
    Serial.println(" cm");
}
```

### Data Visualization:

Displays all values through the serial port in a readable format:

- Gyroscope angle

- Distances detected by each ultrasonic sensor

### Code Usage
  1. Upload the code to your compatible Arduino board.

  2. Open the Serial Monitor (115200 baud).
     
> 💡 *Note: The information will be displayed as follows:*
```text
Gyroscope (Z): 45.32° | Distances - left: 25 cm | Center: 30 cm | right: 0 cm
The values will update every 100 ms.
```


## Possible Hardware Errors
### Ultrasonic Sensors
False positives/negatives: Incorrect readings due to interference or absorbent surfaces

Loose connections: Improper wiring on TRIG/ECHO pins

Limited range: Objects beyond the maximum range (4 m) are not detected

### MPU6050 (IMU)
Gyroscope Drift: Loss of precision in angular measurements over time

Incorrect Calibration: Offset not properly calculated in mpu.calcOffsets()

Vibrations: Abrupt movements affect readings

### Motors and Servo
Mechanical Jams: Physical obstructions in the steering system

Wear: Loss of precision in servo movements

Insufficient Power: Voltage drops affect torque/speed

### Software Errors
Control Logic
Poorly Tuned PID: kp, ki, kd values not optimized

Race Conditions: Conflicts when executing multiple functions

Deadlocks: Locks in control loops

### Communication
Serial Buffer Full: Data loss due to not clearing the buffer

I2C Latency: Delays in communication with MPU6050

Synchronization: Mismatch between sensor readings and actions





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






