import time
import board
import neopixel
from random import sample


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 200

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER
)

def blue_sparkles(wait):
    num_sparkles = 30
    sparkle_idx  = sample(range(num_pixels), num_sparkles)
    for i in range(num_pixels):
                    #g,r,b
        pixels[i] = (0,0,32) # set background to dark blue
        #pixels[i] = (25,32,0) # set background to yellow
    for i in sparkle_idx:
        pixels[i] = (255,255,255) # set sparkles to full white
    pixels.show()
    time.sleep(wait)

try:
    while True:
        blue_sparkles(0.025)  # candy cane cycle with 100ms delay per step
except KeyboardInterrupt:
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
    pixels.show()


