import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 200

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

class Runner(object):
    def __init__(self, pos, mod, steps, color):
        self.pos = pos
        self.mod = mod
        self.steps = steps
        self.color = color

    def update(self):
        self.pos += self.steps * self.mod
        self.pos = self.pos % num_pixels

runners = [
        # position, mod, steps, color
    Runner(0 + (10 *  0), 10, 1, (255, 0, 0)),
    Runner(5 + (10 *  6), 10, 1, (0, 255, 0)),
    Runner(3 + (10 * 13), 10, 1, (0, 0, 255)),
]

def circle_runners(wait):
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
        for r in runners:
            if r.pos == i:
                pixels[i] = r.color
    for r in runners:
        r.update()
    pixels.show()
    time.sleep(wait)

try:
    while True:
        circle_runners(0.05) 
except KeyboardInterrupt:
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
    pixels.show()


