'''
Main entry point for the application
'''
from time import time
import logging
logging.basicConfig(
    filename=r'/home/jkunze/wreath/logs/main.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

from blue_sparkles import BlueSparkles
from candy_cane import CandyCane
from circle_runners import CircleRunners
from rainbow import Rainbow
from rings import Rings
from video_to_lights import VideoToLights

class Main(object):
    def __init__(self, duration_seconds=3600*4):
        self.blue_sparkles = BlueSparkles()
        self.candy_cane = CandyCane()
        self.circle_runners = CircleRunners()
        self.rainbow = Rainbow()
        self.rings = Rings()
        self.video_to_lights = VideoToLights()
        self.duration_seconds = duration_seconds
        self.start_time = time()
    
    def run_iterations(self, fn, iterations=100):
        for i in range(iterations):
            fn()
            if time() - self.start_time > self.duration_seconds:
                logging.info('Time limit reached')
                raise KeyboardInterrupt # break out of the loop

    def run(self):
        try:
            while True:
                self.run_iterations(self.blue_sparkles.blue_sparkles, 100)
                self.run_iterations(self.candy_cane.candy_cane_onoff, 5)
                self.run_iterations(self.circle_runners.circle_runners, 100)
                self.run_iterations(self.rainbow.rainbow, 5)
                self.run_iterations(self.rings.rings, 5)
                self.run_iterations(self.video_to_lights.video_to_lights, 100)
        except KeyboardInterrupt:
            logging.info('KeyboardInterrupt')
            pass
        except Exception as e:
            logging.exception(e)
        for i in range(self.blue_sparkles.num_pixels):
            self.blue_sparkles.pixels[i] = (0,0,0)
        self.blue_sparkles.pixels.show()

if __name__ == "__main__":
    logging.info('Starting main.py')
    m = Main()
    m.run()
