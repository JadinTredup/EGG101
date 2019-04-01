# Arduino Robot Car
The following guide provides instructions for building and programming the Arduino Smart Car kit.

## Build Instructions  
Follow the instructions below for building the car. There appears to be some variance in the Quality of instructions provided around the web. Additionally, it appears some acryllic bases have the holes drilled in different positions. You may find along the way that your holes are drilled in different positions. Feel free to take liberty in place the components on the board. It may be better in some situations to place the components on top with foam tape. Also, because we do not expect all of the students to have easy access to a soldering iron, the switch is not used in this set of instructions. The robot can be powered down by removing the plug from the power-port on the Arduino.

### Step 1: Make sure you have the necessary parts
Due to the holes on the base piece not lining up perfectly with the holes on the circuit boards, these instructions use less screws than which come with the kit. If you follow these instructions you should have leftover hardware pieces. The table and photo below show the components necessary for these instructions.  
 

| Part | Qty. |  
| ---------------------- | -------- |  
| Large Acrylic Base Piece | 1 |  
| Acrylic Wheel Fastening Tabs | 4 |
| Arduino Uno | 1 |
| Arduino Sensor Shield | 1 |
| L298N Motor Driver | 1 |
| Ultrasonic Sensor | 1 |
| Ultrasonic Sensor Base | 1 |
| Ultrasonic Sensor Sides | 1 |
| 9g Microservo | 1 |
| White two-arm servo horn | 1 |
| DC Motor | 2 |
| Large Wheel | 2 |
| Caster Wheel | 1 |
| 6 x AA Battery Holder | 1 |
| M3 x 5mm Screws | 15 |
| M3 x 30mm Screws | 4 |
| M3 Nuts | 7 |
| M3 x 10mm Standoffs | 6 |
| M3 x 20mm Standoffs | 2 |
| M1 x 11mm Screws | 4 |
| M1 Nuts | 4 |
| 3mm Self-Tapping Screws | 2 |
| 7mm Self-Tapping Screws | 2 |
| 8mm Pan-Head Screw | 1 |


![Robot Car Components](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/AllParts.JPG)

### Step 2: Remove Paper from Acrylic Base and Differentiate between the Top and Bottom of the Platform  

| Part | Qty. |  
| ---------------------- | -------- |  
| Large Acrylic Base Piece | 1 |  


The following picture shows the way to distinguish which side is the top and which side is the bottom of the base. Credit for the image goes to the source: [Columbia Robot Car Instructions](http://www.cs.columbia.edu/~sedwards/presentations/robot-car-instructions.pdf)  
![Top and Bottom](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/TopBottom.png)

### Step 3: Attach the Motors to the Bottom of the Base  

| Part | Qty. |  
| ---------------------- | -------- |  
| Acrylic Wheel Fastening Tabs | 4 |
| DC Motor | 2 |
| M3 Nuts | 4 |
| M3 x 30mm Screws | 4 |


The kit comes with 4 smaller acrylic pieces used to mount the wheels to the bottom of the base. To attach the motors follow the steps below, with the pictures as a guide:
1. Remove paper from the 4 acrylic tabs
2. Insert two acrylic tabs into the slots from the top side so that they extend to the bottom.
3. Set the two motors next to each slot so that the axles are towards the front of the base and the wires are on the inside.
4. Place the remaining two acrylic tabs on the outside of the motors, in the designated slots. Make sure tabs and motors are flush with the base.
5. Thread the 4 30mm M3 screws sot hat the motors are held between the acrylic tabs and the screw heads are on the outside.
6. Using 4 M3 nuts, tighten the screws so that the motors are held tightly in place.  
![Motors from Above](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/MotorsAbove.JPG) 
![Motors from Angle](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/MotorsAngled.JPG)

### Step 4: Attach the standoffs for the Caster   

| Part | Qty. |  
| ---------------------- | -------- |  
| M3 x 5mm Screws | 4 |
| M3 x 10mm Standoffs | 4 |


Before we attach the caster to the back of the car, we need to attach four standoffs so that the caster reaches the same level as the two wheels. To do this, insert four 5mm M3 screws to the front of the base from the top. On the bottom side, screw four of the 10mm M3 standoffs to the base.  
![Below Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/CasterStandoff1.JPG) 
![Above Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/CasterStandoff2.JPG)

### Step 5: Attach the Wheels and Caster  

| Part | Qty. |  
| ---------------------- | -------- |  
| Large Wheels | 2 |
| Caster Wheel | 1 |
| M3 x 5mm Screws | 4 |


Using four more 5mm M3 screws, mount the caster to the bottom of the board where the standoffs are. After this, mount the two wheels to the motor axles.  
![Wheels Attached](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/Wheels.JPG)

### Step 6: Mount the Arduino and L298N Motor Driver  

| Part | Qty. |  
| ---------------------- | -------- |  
| M3 x 5mm Screws | 6 |
| M3 Nuts | 2 |
| M3 x 10mm Standoffs | 2 |
| M3 x 20mm Standoffs | 2 |


To mount the arduino you must first use 5mm M3 screws to attach two 10mm M3 standoffs to the top of the base in the two spots shown in the picture below.  
![Arduino Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/ArduinoStandoff.JPG)  
  
For the L298N motor driver, we will use two of the 20mm M3 standoffs. These standofs are threaded on one side, and so for the motor driver, it is easier to first attach the standoffs to the driver using the M3 nuts shown below.  
![L298N Driver Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/L298NStandoff.JPG)  
  
After attaching the standoffs, use two more 5mm M3 screws to fasten the arduino to the standoffs and two 5mm M3 screws to attach the driver's standoffs to the base as seen below.  
![Boards Mounted 1](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/Boards1.JPG)  
![Boards Mounted 2](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/Boards2.JPG)

### Step 7: Center the Servo Motor
Before attaching the servo motor to the mount we need to center it so that the horn is oriented properly to give the Ultrasonic Sensor a full range of motion. To do this, connect the servo pins to pin 4 on the Arduino with the brown wire at the ground position (see Step 10 for a visiual reference of the wires position). Connect the Arduino to a host PC via USB cable and upload the file "center_servo_motor.ino" via the Arduino IDE. When this code runs the servo should turn slightly so that it is centered, and then you may unplug the Arduino from the PC.

### Step 8: Mount the Ultrasonic Sensor


| Part | Qty. |  
| ---------------------- | -------- |  
| Ultrasonic Sensor | 1 |
| Ultrasonic Sensor Base | 1 |
| Ultrasonic Sensor Sides | 2 |
| 9g Microservo | 1 |
| White two-arm servo horn | 1 |
| 3mm Self-Tapping Screws | 2 |
| 7mm Self-Tapping Screws | 2 |
| 8mm Pan-Head Screw | 1 |
| M1 x 11mm Screws | 4 |
| M1 Nuts | 4 |

In this step my photos differ slightly from the actual instructions. The instructions tell you to trim the white servo horn so that it fits within the sensor base (on the backside of the item pictured in the first photo below) and then fasten it from the bottom side using the 3mm self-tapping screws. Unfortunately, mine came with the two 7mm screws forced in, making the holes too large for the 3mm self-tapping screws. For this reason, my white servo horn is glued into the sensor base using a high-adhesiv glue (Gorilla Glue to be exact). After securing the white servo horn to the ultrasonic base, the instructions are as follows:  
1. Secure the microservo to the horn with the 8mm pan-head screw so that when the mount is fastened to the base (as seen in the second picture) the large part of the servo is facing forward.  
2. Use the M1 x 11mm screws and the M1 nuts to mount the Ultrasonic base to the large acrylic piece so that the microservo horn is closer to the back (see pictures 2 and 3 below).  
3. Use the 7mm self-tapping screws to secure the black Ultrasonic sides to both sides of the microservo so that the two holes are on the front side.  
4. Secure the Ultrasonic sensor to the mount using the two zip-ties. Make sure the leads for the sensor are facing upwards (see pictures 3 and 4 below).  

![Servo Horn](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/MotorSensorMount.JPG)  
![Mounted Sensor Bottom](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/SensorUnderside.JPG)  
![Mounted Sensor Top](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/SensorTopside.JPG)  
![Ziptie Sensor](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/MountedSensor.JPG)  

### Step 9: Mount the Battery Holder  

| Part | Qty. |  
| ---------------------- | -------- |
| 6 x AA Battery Holder | 1 |
| M3 x 5mm Screw | 1 |
| M3 Nut | 1 |

Mount the battery holder to the back side of the base piece. In my piece there were not two evenly spaced holes and so I could only secure the holder on one end, which seems like a common issue around the internet.  

![Battery Bottom](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/BatteryBottom.JPG)  
![Battery Top](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/BatteryTop.JPG)  

### Step 10: Wiring the Components  


| Part | Qty. |  
| ---------------------- | -------- |
| Female-to-Female Jumper Wires (Short) | 4 |
| Female-to-Female Jumper Wires (Long) | 4 |

Follow these steps to wiring all of the components, pictures and a table are below for reference:  
1. Wire the DC motors to the L298N motor driver so that the black and red wires are each connected to their respective ground and 5V terminals (Picture 1).  
2. Connect the 4 short jumper wires from the header-pins on the L298N motor driver to the pins on the Arduino (Picture 2 and 3).  
3. Use the long jumper wires to connect the pins from the Ultrasonic sensor to the pins on the Arduino (Picture 4).
4. Connect the microservo wires to the pins on the Arduino (Picture 5).

![Motors to Driver](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/DriverWires1.JPG)  
![Arduino from Driver](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/ArduinoWires1.JPG)  
![Driver to Arduino](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/DriverWires2.JPG)  
![Sensor to Arduino](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/SensorWires.JPG) 
![Full Arduino](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/ArduinoWires2.JPG) 

### Step 11: Upload the Code
Finally to run the code, follow these steps:
1. Download this repository and get the "robot_car.ino" file from the "Code" folder.  
2. Connect the Arduino to your computer via USB cable.  
3. Use the IDE to upload "robot_car.ino" to the Arduino then disconnect it from the PC.  
4. Insert batteris into the battery holder and then plug the power plug into the Arduino.  
5. Hit the "reset" button to initialize the program.  

## Explaining the Code
