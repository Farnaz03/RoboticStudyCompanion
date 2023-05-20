# To do: Debug program to run both servos --- error with pulsewidth 

import pigpio
import time

# Connect to the pigpio daemon
pi = pigpio.pi()

# Set the GPIO pin for the servo
# GPIO_PIN = [13, 21]
GPIO_PIN = 13

def servo_fcn (PIN):
    # Set the initial pulse width to stop the servo
    pi.set_servo_pulsewidth(PIN, 1500)

    # Wait for the servo to stop
    time.sleep(1)

    # Set the pulse width to rotate the servo clockwise
    pi.set_servo_pulsewidth(PIN, 2000)

    # Wait for the servo to rotate
    time.sleep(1)

    # Set the pulse width to rotate the servo counterclockwise
    pi.set_servo_pulsewidth(PIN, 1000)

    # Wait for the servo to rotate
    time.sleep(1)

    # Stop the servo
    pi.set_servo_pulsewidth(PIN, 1500)

    # Disconnect from the pigpio daemon
    pi.stop()

servo_fcn(GPIO_PIN)
# servo_fcn(GPIO_PIN1)