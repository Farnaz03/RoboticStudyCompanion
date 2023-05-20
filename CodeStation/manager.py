#!/usr/bin/env python3

#import scripts
import light_neopixel
import speak_gpt
import move_servo

import time


try:

    #NeoPixel = RED = power on & loading
    light_neopixel.pixels.fill((255, 0, 0))
    light_neopixel.pixels.show()
    time.sleep(3)

    # print("Ready to go ... ")
    # # #NeoPixel = GREEN = Ready to listen
    # light_neopixel.pixels.fill((0, 255, 0))
    # light_neopixel.pixels.show()
    # time.sleep(5)

    #Servo waves 
    # #Wave Hi
    # move_servo.wave_hi()
    # print("waving Hi!")
    # time.sleep(5)

    # #Speak GPT
    # # Call the main loop function in speak_gpt.py
    print("Starting GPT ...")
    speak_gpt.main_loop()
    
    # # wait for 1 second
    # time.sleep(1)
   

    
finally:
    # Turn off all LEDs
    light_neopixel.pixels.fill((0, 0, 0))
    light_neopixel.pixels.show()
    print("okay, bye ...")
