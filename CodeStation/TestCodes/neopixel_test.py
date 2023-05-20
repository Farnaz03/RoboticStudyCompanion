#https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage 

# To run: sudo python3 neopixel_test.py

import board
import neopixel
import time

# Define the number of pixels in the NeoPixel ring
NUM_PIXELS = 16

# Initialize the NeoPixel ring
pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS)

# Set the color of all pixels to green
pixels.fill((255,0, 0))
pixels.show()

# Wait for 2 seconds
time.sleep(5)

# # # Turn off the LED at index 2
# pixels[1] = (0, 0, 255)
# pixels[2] = (0, 0, 255)
# pixels[3] = (0, 0, 255)
# pixels.show()

# # Wait for another 2 seconds
# time.sleep(5)

# Turn off the LED at index 2
# pixels[7] = (0, 0, 255)
# pixels[9] = (0, 0, 255)
# pixels.show()

# Wait for another 2 seconds
# time.sleep(2)

# Turn off all LEDs
pixels.fill((0, 0, 0))
pixels.show()

# Turn off the LED at index 2
# pixels[1] = (0, 0, 0)
# pixels[2] = (0, 0, 0)
# pixels[3] = (0, 0, 0)
