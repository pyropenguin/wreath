# Simulator
import cv2
import numpy as np

class board(object):
    D18 = 18

class neopixel(object):
    GRB = 1
    RGB = 2

class NeoPixel(object):
    def __init__(self, pixel_pin=None, num_pixels=200, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB) -> None:
        self.im_width  = 512
        self.im_height = 512
        self.wreath_max_radius = self.im_width // 2
        self.wreath_min_radius = self.wreath_max_radius - (self.im_width // 4)
        self.center = (self.im_width // 2, self.im_height // 2)
        self.num_lights = num_pixels
        self.brighness = brightness
        self._pixels = np.zeros((self.num_lights, 3))
    
    def __getitem__(self, key):
        return self._pixels[key]
    
    def __setitem__(self, key, value):
        self._pixels[key] = value
    
    def draw_point_from_center(self, im, angle_deg, distance, color, thickness = 1):
        OFFSET = 90 # degrees
        x = int(self.center[0] + distance * np.cos((angle_deg + OFFSET) * np.pi / 180))
        y = int(self.center[1] + distance * np.sin((angle_deg + OFFSET) * np.pi / 180))
        cv2.circle(im, (x, y), thickness, color, -1)

    def show(self):
        im = np.zeros((self.im_width, self.im_height, 3), dtype = "uint8")

        # Draw center
        cv2.circle(im, self.center, 1, (0, 0, 255), -1)

        for i in range(self.num_lights):
            angle_deg = i * (360 / self.num_lights)
            radius_multiplier = abs((i % 10) - 5) 
            radius = self.wreath_min_radius + radius_multiplier * (self.wreath_max_radius - self.wreath_min_radius) / 5
                    # g, r, b
            color = (self._pixels[i][2] * self.brighness, 
                     self._pixels[i][0] * self.brighness,
                     self._pixels[i][1] * self.brighness)
            self.draw_point_from_center(im, angle_deg, radius, color, 5)

        cv2.namedWindow("Simulator")
        cv2.imshow("Simulator", im)
        cv2.waitKey(10)

if __name__ == "__main__":
    num_pixels = 200
    pixels = NeoPixel()
    for color in [(255,0,0), (0,255,0), (0,0,255)]:
        for i in range(num_pixels):
            pixels[i] = color
            pixels.show()
