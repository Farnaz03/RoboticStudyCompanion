# https://aiyprojects.withgoogle.com/voice/#makers-guide--gpio-expansion-pins

from gpiozero import Servo
from aiy.pins import PIN_A
from aiy.pins import PIN_B
import time

# Create a servo with the custom values to give the full dynamic range.
tuned_servo = Servo(PIN_A, min_pulse_width=.0005, max_pulse_width=.0019)
tuned_servo1 = Servo(PIN_B, min_pulse_width=.0005, max_pulse_width=.0019)

# Move the Servos back and forth until the user terminates the example.
while True:
    print("ping")
    tuned_servo.max()
    tuned_servo1.max()
    time.sleep(2)
    tuned_servo.mid()
    tuned_servo1.mid()
    time.sleep(2)
    tuned_servo.min()
    tuned_servo1.min()
    time.sleep(2)

# To stop servos, send detach or pulse signal


# max_pulse_width is the maximum pulse width that the servo expects to receive.
# Pulse width is a measure of the duration of the electrical signal that is sent to the servo to control its position. 
# The pulse width is measured in microseconds, and typically ranges from 500 to 2500 microseconds. 
# By specifying the max_pulse_width parameter when creating the Servo object, you can customize the range of motion of the servo. 
# In this case, max_pulse_width is set to 1.9 milliseconds (1900 microseconds), which means that the servo will rotate to 
# its maximum angle when it receives a pulse of this duration.