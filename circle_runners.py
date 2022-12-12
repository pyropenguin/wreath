import time
import board
import neopixel

class Runner(object):
    def __init__(self, pos, mod, steps, color, num_pixels):
        self.pos = pos
        self.mod = mod
        self.steps = steps
        self.color = color
        self.num_pixels = num_pixels

    def update(self):
        self.pos += self.steps * self.mod
        self.pos = self.pos % self.num_pixels

class CircleRunners(object):
    def __init__(self, num_pixels=200, pixel_pin=board.D18, brightness=1.0, pixel_order=neopixel.GRB):
        self.num_pixels = num_pixels
        self.pixel_pin = pixel_pin
        self.brightness = brightness
        self.pixel_order = pixel_order
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )

        self.runners = [
                # position, mod, steps, color
            Runner(0 + (10 *  0), 10, 1, (255, 0, 0), 200),
            Runner(5 + (10 *  6), 10, 1, (0, 255, 0), 200),
            Runner(3 + (10 * 13), 10, 1, (0, 0, 255), 200),
            Runner(1 + (10 *  0), 10, -1, (255, 255, 0), 200),
            Runner(4 + (10 *  6), 10, -1, (0, 255, 255), 200),
            Runner(2 + (10 * 13), 10, -1, (255, 0, 255), 200),
        ]

    def circle_runners(self, wait=0.05):
        for i in range(self.num_pixels):
            self.pixels[i] = (0,0,0)
            for r in self.runners:
                if r.pos == i:
                    self.pixels[i] = r.color
        for r in self.runners:
            r.update()
        self.pixels.show()
        time.sleep(wait)

    def run(self, wait=0.05):
        try:
            while True:
                self.circle_runners(wait)
        except KeyboardInterrupt:
            for i in range(self.num_pixels):
                self.pixels[i] = (0,0,0)
            self.pixels.show()

if __name__ == "__main__":
    r = CircleRunners()
    r.run()
