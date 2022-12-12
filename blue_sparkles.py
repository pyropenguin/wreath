import time
import board
import neopixel
from random import sample

class BlueSparkles(object):
    def __init__(self, num_pixels=200, pixel_pin=board.D18, brightness=1.0, pixel_order=neopixel.GRB):
        self.num_pixels = num_pixels
        self.pixel_pin = pixel_pin
        self.brightness = brightness
        self.pixel_order = pixel_order
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )

    def blue_sparkles(self, wait=0.025):
        num_sparkles = 30
        sparkle_idx  = sample(range(self.num_pixels), num_sparkles)
        for i in range(self.num_pixels):
                        #g,r,b
            self.pixels[i] = (0,0,32) # set background to dark blue
            #pixels[i] = (25,32,0) # set background to yellow
        for i in sparkle_idx:
            self.pixels[i] = (255,255,255) # set sparkles to full white
        self.pixels.show()
        time.sleep(wait)

    def run(self, wait=0.025):
        try:
            while True:
                self.blue_sparkles(wait)
        except KeyboardInterrupt:
            for i in range(self.num_pixels):
                self.pixels[i] = (0,0,0)
            self.pixels.show()

if __name__ == "__main__":
    b = BlueSparkles()
    b.run()
