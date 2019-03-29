# Arduino Robot Car
The following guide provides instructions for building and programming the Arduino Smart Car kit.

## Build the Kit
Follow the instructions below for building the car.

### Step 1: Make sure you have the necessary parts
![Robot Car Components](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/AllParts.JPG)

### Step 2: Remove Paper from Acrylic Base and Differentiate between the Top and Bottom of the Platform
The following picture shows the way to distinguish which side is the top and which side is the bottom of the base. Credit for the image goes to the source: [Columbia Robot Car Instructions](http://www.cs.columbia.edu/~sedwards/presentations/robot-car-instructions.pdf)  
![Top and Bottom](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/TopBottom.png)

### Step 3: Attach the Motors to the Bottom of the Base
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
Before we attach the caster to the back of the car, we need to attach four standoffs so that the caster reaches the same level as the two wheels. To do this, insert four 5mm M3 screws to the front of the base from the top. On the bottom side, screw four of the 10mm M3 standoffs to the base.  
![Below Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/CasterStandoff1.JPG) 
![Above Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/CasterStandoff2.JPG)

### Step 5: Attach the Wheels and Caster
Using four more 5mm M3 screws, mount the caster to the bottom of the board where the standoffs are. After this, mount the two wheels to the motor axles.  
![Wheels Attached](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/Wheels.JPG)

### Step 6: Mount the Arduino and L298N Motor Driver
To mount the arduino you must first use 5mm M3 screws to attach two 10mm M3 standoffs to the top of the base in the two spots shown in the picture below.  
![Arduino Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/ArduinoStandoff.JPG)  
  
For the L298N motor driver, we will use two of the 20mm M3 standoffs. These standofs are threaded on one side, and so for the motor driver, it is easier to first attach the standoffs to the driver using the M3 nuts shown below.  
![L298N Driver Standoffs](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/L298NStandoff.JPG)  
  
After attaching the standoffs, use two more 5mm M3 screws to fasten the arduino to the standoffs and two 5mm M3 screws to attach the driver's standoffs to the base as seen below.  
![Boards Mounted 1](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/Boards1.JPG)  
![Boards Mounted 2](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/Boards2.JPG)

### Step 7: Center the Servo Motor

### Step 8: Mount the Ultrasonic Sensor
![Servo Horn](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/MotorSensorMount.JPG)  
![Mounted Sensor Bottom](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/SensorUnderside.JPG)  
![Mounted Sensor Top](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/SensorTopside.JPG)  
![Ziptie Sensor](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/MountedSensor.JPG)  

### Step 9: Mount the Battery Holder
![Battery Bottom](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/BatteryBottom.JPG)  
![Battery Top](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/BatteryTop.JPG)  

### Step 10: Wiring the Components
![Motors to Driver](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/DriverWires1.JPG)  
![Arduino from Driver](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/ArduinoWires1.JPG)  
![Driver to Arduino](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/DriverWires2.JPG)  
![Sensor to Arduino](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/SensorWires.JPG) 
![Full Arduino](https://github.com/JadinTredup/EGG101/blob/master/Robot_Car/Images/ArduinoWires2.JPG) 

### Step 11: Upload the Code
Finally, upload the code (Located in the "Code" directory) to the arduino board. Insert batteries into the battery holder and reset the Arduino to operate the vehicle.

## Explaining the Code
