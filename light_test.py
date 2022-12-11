import board
import neopixel
from time import sleep

NUM_PIXELS = 100
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)

# pixels[0] = (255, 0, 0)

colors = [(255,0,0),(0,255,0),(0,0,255)]
for p in range(NUM_PIXELS):
    for i in range(len(colors) * 1):
        color = colors[i % len(colors)]
        pixels[p] = color
        sleep(0.1)
    pixels[p] = (0,0,0)


# bpp - Bytes Per Pixel. Defaults to 3. Set this to 4 if you have RGBW NeoPixels. If you try to fill the NeoPixels with a solid color and they light up as different colors, you will probably want to change this.
# pixel_order - If you are seeing the NeoPixels light up as the same colors, but they are a different color than you expect, you may need to change this value.
