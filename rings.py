import time
import board
import neopixel
from random import sample

class Rings(object):
    def __init__(self, num_pixels=200, pixel_pin=board.D18, brightness=0.2, pixel_order=neopixel.GRB):
        self.num_pixels = num_pixels
        self.pixel_pin = pixel_pin
        self.brightness = brightness
        self.pixel_order = pixel_order
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )

    def rings(self, wait=0.2):
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
            for i in range(self.num_pixels):
                if i % num_rings == r:
                    c = viridis[r]
                                #g,r,b
                    self.pixels[i] = (c[1], c[0], c[2])
                else:
                    self.pixels[i] = (0,0,0) # set background to black
            self.pixels.show()
            time.sleep(wait)

    def run(self, wait=0.2):
        try:
            while True:
                self.rings(wait)
        except KeyboardInterrupt:
            for i in range(self.num_pixels):
                self.pixels[i] = (0,0,0)
            self.pixels.show()

if __name__ == "__main__":
    r = Rings()
    r.run()
