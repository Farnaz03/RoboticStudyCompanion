# To run: sudo python3 neopixel_test.py
import board
import neopixel
import time

# Define the number of pixels in the NeoPixel ring
NUM_PIXELS = 16

# Initialize the NeoPixel ring
pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS)

# Set the color of all pixels to red
pixels.fill((255, 0, 0))
pixels.show()

# Wait for 2 seconds
time.sleep(2)

# Turn off all LEDs
pixels.fill((0, 0, 0))
pixels.show()