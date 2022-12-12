import time
import board
import neopixel

class CandyCane(object):
    def __init__(self, num_pixels=200, pixel_pin=board.D18, brightness=0.2, pixel_order=neopixel.GRB):
        self.num_pixels = num_pixels
        self.pixel_pin = pixel_pin
        self.brightness = brightness
        self.pixel_order = pixel_order
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )

    def candy_cane(self, wait=0.001):
        stripe_width = 20
        for j in range(self.num_pixels):
            for i in range(self.num_pixels):
                is_red = (i+j) % (stripe_width * 2) < stripe_width
                            #g,r,b
                self.pixels[i] = (0,255,0) if is_red else (255,255,255)
            self.pixels.show()
            time.sleep(wait)

    def candy_cane_onoff(self, wait=0.001):
        stripe_width = 20
        periods = 50
        for p in range(2*periods):
            for i in range(self.num_pixels):
                is_red = (i) % (stripe_width * 2) < stripe_width
                            #g,r,b
                if p < periods:
                    fade = int(255 * (p / periods))
                else:
                    fade = int(255 * ((2 * periods) - p) / periods)
                self.pixels[i] = (0,fade,0) if is_red else (fade,fade,fade)
            self.pixels.show()
            time.sleep(wait)

    def run(self, wait=0.001):
        try:
            while True:
                # self.candy_cane(wait)
                self.candy_cane_onoff(wait)
        except KeyboardInterrupt:
            for i in range(self.num_pixels):
                self.pixels[i] = (0,0,0)
            self.pixels.show()

if __name__ == "__main__":
    c = CandyCane()
    c.run()
