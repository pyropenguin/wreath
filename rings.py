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

def rings(wait):
    num_rings = 10
                    # r,   g,   b
    viridis = [( 68,   1,  84),
               ( 72,  40, 120),
               ( 62,  74, 137),
               ( 49, 104, 142),
               ( 38, 130, 142),
               ( 31, 158, 137),
               ( 53, 183, 121),
               (109, 205,  89),
               (180, 222,  44),
               (253, 231,  37)]
    for r in range(num_rings):
        for i in range(num_pixels):
            if i % num_rings == r:
                c = viridis[r]
                            #g,r,b
                pixels[i] = (c[1], c[0], c[2])
            else:
                pixels[i] = (0,0,0) # set background to black
        pixels.show()
        time.sleep(wait)

try:
    while True:
        rings(0.2)
except KeyboardInterrupt:
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
    pixels.show()


