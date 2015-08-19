import os
import time
from PIL import Image, ImageDraw


def get_brightness(image, width, height):
    s = 0
    for i in range(width):
        for j in range(height):
            pixel = 0
            for color in range(3):
                pixel += image[i, j][color]
            s += pixel // 3
    s /= width * height
    return s

max_lvl = 100
min_lvl = 0
alpha = 0.85
delta = 50
while True:
    os.system('fswebcam /tmp/snapshot.jpg 2> /dev/null')
    image = Image.open('/tmp/snapshot.jpg')
    width = image.size[0]
    height = image.size[1]
    image = image.load()
    cur_illumination = get_brightness(image, width, height)
    lvl = int(min_lvl + (max_lvl - min_lvl) * (cur_illumination / (255 - delta)) * alpha)
    lvl = min(lvl, max_lvl)
    os.system('xbacklight -set {}'.format(lvl))
    time.sleep(20)
