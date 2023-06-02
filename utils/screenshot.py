import ImageGrab
from PIL import ImageDraw
import base64
import os
import sys

try:
    from PIL import Image
    from PIL import ImageOps
except ImportError:
    pass

def pic_to_base64(picpath):
    if os.path.isfile(picpath):
        f = open(picpath, 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        os.remove(picpath)
        return base64.b64decode(ls_f.decode('ascii'))

def screen_as_png():
    filePath = 'screenshot.png'
    img = ImageGrab.grab()
    img.save(filePath)
    return pic_to_base64(filePath)