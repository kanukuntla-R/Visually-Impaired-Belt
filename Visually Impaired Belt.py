import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# Define GPIO pin constants
BUTTON_PIN = 17
ULTRASONIC_PINS = [(18, 23), (24, 25), (5, 6)]  # Each tuple is (TRIG, ECHO)
VIBRATION_MOTORS_PINS = [12, 16, 20, 21, 22]  # Added two more motor pins
IR_SENSOR_PINS = [26, 19]  # Define IR sensor pins

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the button pin
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up ultrasonic sensor pins
for trig, echo in ULTRASONIC_PINS:
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

# Set up vibration motor pins
for motor_pin in VIBRATION_MOTORS_PINS:
    GPIO.setup(motor_pin, GPIO.OUT)

# Set up IR sensor pins
for ir_pin in IR_SENSOR_PINS:
    GPIO.setup(ir_pin, GPIO.IN)
 
# Initial state of the program
running = False
def measure_distance(trig, echo):
    # Send 10us pulse to trigger
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start_time = time.time()
    stop_time = time.time()

    # Save StartTime
    while GPIO.input(echo) == 0:
        start_time = time.time()

    # Save time of arrival
    while GPIO.input(echo) == 1:
        stop_time = time.time()

    # Time difference between start and arrival
    time_elapsed = stop_time - start_time
    # Multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2

    return distance


def vibrate_motor(motor_pin, duration):
    GPIO.output(motor_pin, True)
    time.sleep(duration)
    GPIO.output(motor_pin, False)

def button_callback(channel):
    global running
    running = not running  # Toggle the running state
    if running:
        print("Activated: The program is running")
    else:
        print("Deactivated: The program is stopped")

# Button event detection
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    while True:
        if running:
            # Ultrasonic sensors
            for i in range(3):
                distance = measure_distance(ULTRASONIC_PINS[i][0], ULTRASONIC_PINS[i][1])
                if distance < 50:
                    # Vibrate motor if distance is less than 50cm
                    vibrate_motor(VIBRATION_MOTORS_PINS[i], 0.5)  # Vibrate for 0.5 seconds
            
            # IR sensors
            for i in range(2):
                if GPIO.input(IR_SENSOR_PINS[i]) == GPIO.LOW:
                    # IR sensor detected something, vibrate corresponding motor
                    vibrate_motor(VIBRATION_MOTORS_PINS[i + 3], 0.5)  # Motors for IR sensors are at the end of the list

        time.sleep(0.1)  # Sleep to reduce CPU usage

except KeyboardInterrupt:
    # Clean up the GPIO pins on a Keyboard interrupt
    GPIO.cleanup()


