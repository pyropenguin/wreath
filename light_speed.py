import time
import board
import neopixel
# import simulator
# from simulator import board, neopixel
from random import sample, seed

class Streak(object):
    def __init__(self, start_pixel, length, speed, color):
        assert start_pixel % 10 == 5
        self.start_pixel = start_pixel
        self.pixel = start_pixel
        self.length = length
        self.speed = speed
        self.color = color
    
    def update(self, pixels):
        do_delete = True
        for i in range(self.pixel, self.pixel + self.length):
            if i >= self.start_pixel and i <= self.start_pixel + 5:
                pixels[i] = self.color
                do_delete = False
        self.pixel += self.speed
        return do_delete

class LightSpeed(object):
    def __init__(self, num_pixels=200, pixel_pin=board.D18, brightness=0.7, pixel_order=neopixel.GRB):
        self.num_pixels = num_pixels
        self.pixel_pin = pixel_pin
        self.brightness = brightness
        self.pixel_order = pixel_order
        self.reset()
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )
        # self.pixels = simulator.NeoPixel(
        #     self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        # )
        seed(42)
    
    def reset(self):
        self.frame = 0
        self.streaks = []

    def light_speed(self, wait=0.025):
        num_new_streaks_per_frame = self.frame // 12 + 3
        new_streaks_every_n_frames = 2
        if self.frame % new_streaks_every_n_frames == 0:
            possible_starts = range(5, self.num_pixels - 5, 10)
            for start_pixel in sample(possible_starts, num_new_streaks_per_frame):
                self.streaks.append(
                    Streak(start_pixel = start_pixel,
                           length = min(5, self.frame // 30 + 1), 
                           speed  = self.frame // 30 + 1, 
                           color  = (255,255,255)))
        
        for i in range(self.num_pixels):
            blue_white_change_rate = 5
            blue_white_start = 255 // blue_white_change_rate
            if self.frame < blue_white_start:
                self.pixels[i] = (
                    0, # g
                    0, # r
                    min(self.frame * blue_white_change_rate,255)) # b
            else:
                self.pixels[i] = (
                    min((self.frame - blue_white_start) * blue_white_change_rate,255), # g
                    min((self.frame - blue_white_start) * blue_white_change_rate,255), # r
                    255) # b
        for streak in self.streaks:
            do_delete = streak.update(self.pixels)
            if do_delete:
                self.streaks.remove(streak)
        self.pixels.show()
        time.sleep(wait)
        self.frame += 1

    def run(self, wait=0.025):
        try:
            while True:
                while self.frame < 125:
                    self.light_speed(wait)
                self.reset()
        except KeyboardInterrupt:
            for i in range(self.num_pixels):
                self.pixels[i] = (0,0,0)
            self.pixels.show()

if __name__ == "__main__":
    l = LightSpeed()
    l.run()
