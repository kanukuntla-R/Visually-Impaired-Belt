# Visually Impaired Belt 👁️‍🗨️🚶

A wearable assistive device built using Raspberry Pi and sensors to help visually impaired individuals navigate their surroundings safely. The belt detects obstacles using ultrasonic and IR sensors and provides real-time feedback through vibration motors.

---

## 📌 Features

- Three ultrasonic sensors for obstacle detection
- Two IR sensors for closer object recognition
- Five vibration motors to provide directional feedback
- Toggle button to activate or deactivate the system
- Written in Python using RPi.GPIO

---

## ⚙️ Hardware Used

- Raspberry Pi (any model with GPIO support)
- 3x HC-SR04 Ultrasonic Sensors
- 2x IR Obstacle Sensors
- 5x Vibration Motors
- Push button
- Jumper wires, breadboard or soldered board
- Power bank or portable power supply

---

## 🧠 How It Works

1. Press the button to activate the belt.
2. Ultrasonic sensors measure distance; if an object is within 50cm, the corresponding motor vibrates.
3. IR sensors detect close obstacles like curbs or steps.
4. Each sensor maps to a motor, providing directional haptic feedback.
---

**Built by Ruthvik Kanukuntla & Team**
