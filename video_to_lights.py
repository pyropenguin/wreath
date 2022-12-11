'''
Video mapping to lights
'''
import cv2
import board
import neopixel
from time import sleep

SET_PIXELS = True
SHOW_FRAME = False

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 200

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

# Create a new ImageCapture object
cap = cv2.VideoCapture(0)

prev_frame = None

try:
    # Capture an image
    while True:
        ret, frame = cap.read()
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
            if prev_frame is not None:
                frame = cv2.subtract(tmp, prev_frame)
                _,frame = cv2.threshold(frame, 5, 255, cv2.THRESH_BINARY)
            prev_frame = tmp.copy()
            
            # LED Pixel Loading
            if SET_PIXELS:
                for p in range(num_pixels):
                        w = p % frame.shape[0]
                        h = (p // frame.shape[0]) % frame.shape[1]
                        pgbr = frame[w][h]
                        pixels[p] = (pgbr[1], pgbr[2], pgbr[0])
                pixels.show()

            # Visualization
            if SHOW_FRAME:
                cv2.imshow('Downsampled Frame', frame)
            cv2.waitKey(1)
        else:
            print('No image captured')
            break
except KeyboardInterrupt:
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
    pixels.show()
    cap.release()
    cv2.destroyAllWindows()

