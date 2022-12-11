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

def candy_cane(wait):
    stripe_width = 20
    for j in range(num_pixels):
        for i in range(num_pixels):
            is_red = (i+j) % (stripe_width * 2) < stripe_width
                        #g,r,b
            pixels[i] = (0,255,0) if is_red else (255,255,255)
        pixels.show()
        time.sleep(wait)

def candy_cane_onoff(wait):
    stripe_width = 20
    periods = 50
    for p in range(2*periods):
        for i in range(num_pixels):
            is_red = (i) % (stripe_width * 2) < stripe_width
                        #g,r,b
            if p < periods:
                fade = int(255 * (p / periods))
            else:
                fade = int(255 * ((2 * periods) - p) / periods)
            pixels[i] = (0,fade,0) if is_red else (fade,fade,fade)
        pixels.show()
        time.sleep(wait)

try:
    while True:
        # candy_cane(0.01)
        candy_cane_onoff(0.01)
except KeyboardInterrupt:
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
    pixels.show()


