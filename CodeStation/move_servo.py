# https://aiyprojects.withgoogle.com/voice/#makers-guide--gpio-expansion-pins

from gpiozero import Servo
from aiy.pins import PIN_A
from aiy.pins import PIN_B
import time

def wave_hi():
    # Create a servo with the custom values to give the full dynamic range.
    tuned_servo = Servo(PIN_A, min_pulse_width=.0005, max_pulse_width=.0019)
    tuned_servo1 = Servo(PIN_B, min_pulse_width=.0005, max_pulse_width=.0019)
    
    # Move the Servo to wave hi.
    tuned_servo.value = 1  # Set the servo angle to 90 degrees.
    time.sleep(0.5)
    # tuned_servo1.value = -1
    # time.sleep(0.5)
    tuned_servo.value = None  # Set the servo angle to neutral.

if __name__ == '__main__':
    wave_hi()
