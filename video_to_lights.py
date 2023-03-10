'''
Video mapping to lights
'''
import cv2
import board
import neopixel
from time import sleep
import numpy as np

SET_PIXELS = True
SHOW_FRAME = False

def dampening_factor(x, dmp_start=200, dmp_end=800):
    damp = 1 - (x - dmp_start) / (dmp_end - dmp_start)
    damp = min(damp, 1)
    damp = max(damp, 0)
    return damp

class VideoToLights(object):
    def __init__(self, num_pixels=200, pixel_pin=board.D18, brightness=0.4, pixel_order=neopixel.GRB):
        self.num_pixels = num_pixels
        self.pixel_pin = pixel_pin
        self.brightness = brightness
        self.pixel_order = pixel_order
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )
        # Create a new ImageCapture object
        self.cap = cv2.VideoCapture(0)
        self.prev_frame = None

        self.frame_avg_length = 20
        self.frame_avg = np.full(self.frame_avg_length, np.nan)
    
    def video_to_lights(self, wait=0.001):
        # Capture an image
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            #print('Original frame size:', frame.shape)
            frame = cv2.flip(frame, 0)
            if SHOW_FRAME:
                cv2.imshow('Original Frame', frame)
            
            # Downsampling pyramid stack
            frame = cv2.pyrDown(frame)
            frame = cv2.pyrDown(frame)
            frame = cv2.pyrDown(frame)
            frame = cv2.pyrDown(frame)
            frame = cv2.pyrDown(frame)
            frame = cv2.pyrDown(frame)
            #print('Downsampled frame size:', frame.shape)
            
            tmp = frame.copy()
            if self.prev_frame is not None:
                frame = cv2.subtract(tmp, self.prev_frame)
                _,frame = cv2.threshold(frame, 5, 255, cv2.THRESH_BINARY)
            self.prev_frame = tmp.copy()

            self.frame_avg = np.roll(self.frame_avg, 1)
            self.frame_avg[0] = np.mean(frame)
            frame_sum = np.nansum(self.frame_avg)
            #print('Frame sum:', frame_sum, "Dampeing:", dampening_factor(frame_sum))
            frame = cv2.multiply(frame, dampening_factor(frame_sum))

            # LED Pixel Loading
            if SET_PIXELS:
                for p in range(self.num_pixels):
                        w = p % frame.shape[0]
                        h = (p // frame.shape[0]) % frame.shape[1]
                        pgbr = frame[w][h]
                        self.pixels[p] = (pgbr[1], pgbr[2], pgbr[0])
                self.pixels.show()

            # Visualization
            if SHOW_FRAME:
                cv2.imshow('Downsampled Frame', frame)
            cv2.waitKey(int(wait*1000))
        else:
            print('No image captured')
            return

    def run(self, wait=0.001):
        try:
            while True:
                self.video_to_lights(wait)
        except KeyboardInterrupt:
            for i in range(self.num_pixels):
                self.pixels[i] = (0,0,0)
            self.pixels.show()
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    v = VideoToLights()
    v.run()

