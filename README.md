# 🤖 Arduino Robot with Ultrasonic Sensor and Servo Control 🚗

This Arduino project controls a robot using an ultrasonic sensor to detect obstacles and a servo motor to scan the surroundings.

## 📝 Description

The robot moves forward until it detects an obstacle within a certain range using the ultrasonic sensor. When an obstacle is detected, it stops, backs up, and scans the surroundings using the servo motor. Based on the scan results, it either turns left or right to avoid obstacles.

## 🛠️ Hardware Requirements

- Arduino board
- L298N motor driver
- Ultrasonic sensor (HC-SR04)
- Servo motor
- Chassis, wheels, and motors for the robot

## 🔧 Installation

1. Install the required libraries:
   - Servo library
   - NewPing library (for the ultrasonic sensor)

2. Connect the hardware components according to the wiring diagram.

3. Upload the provided Arduino sketch to your Arduino board.

## 📌 Pin Configuration

- LeftMotorForward: 7
- LeftMotorBackward: 6
- RightMotorForward: 5
- RightMotorBackward: 4
- Trig pin (Ultrasonic sensor): A1
- Echo pin (Ultrasonic sensor): A2
- Servo pin: 10

## 🚀 Usage

1. Power up the Arduino board and deploy the robot.

2. The robot will start moving forward.

3. When an obstacle is detected within the specified range, the robot will stop, back up, and scan the surroundings.

4. Based on the scan results, the robot will turn left or right to avoid obstacles.

5. The process repeats as the robot continues to navigate its environment.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.


