from PIL import Image
from RGB_HSV import rgb_to_hsv, hsv_to_rgb


class Funcs(object):
    def __init__(self, filename, resultname='result.jpg'):
        self.name = filename
        self.rname = resultname
        self.image = Image.open(self.name)
        self.x, self.y = self.image.size
        self.image.save(self.rname)
        self.result = Image.open(self.rname)
        self.pixels = self.image.load()
        self.pixels_res = self.result.load()

    def brightness(self, delta=100):
        if 0 <= delta <= 200:
            for i in range(self.x):
                for j in range(self.y):
                    self.pixels_res[i, j] = tuple(
                        map(lambda x: x + int(round((delta - 100) / 2, 0)), self.pixels[i, j]))
            self.result.save(self.rname)

    def contrast(self, delta=100):
        if 0 <= delta <= 200:
            delta = delta / 10 ** 2
            for i in range(self.x):
                for j in range(self.y):
                    rgb = []
                    for k in self.pixels[i, j]:
                        x = int(round(((k / 255 - 0.5) * delta + 0.5) * 255, 0))
                        if x > 255:
                            x = 255
                        elif x < 0:
                            x = 0
                        rgb.append(x)
                    self.pixels_res[i, j] = (rgb[0], rgb[1], rgb[2])
            self.result.save(self.rname)

    def saturation(self, delta=100):
        if 0 <= delta <= 200:
            delta = delta / 100
            for i in range(self.x):
                for j in range(self.y):
                    rgb = list(self.pixels[i, j])
                    hsv = list(rgb_to_hsv(rgb[0], rgb[1], rgb[2]))
                    hsv[1] *= delta
                    self.pixels_res[i, j] = tuple(map(int, hsv_to_rgb(hsv[0], hsv[1], hsv[2])))
            self.result.save(self.rname)

    def warmth(self, delta=100):
        if 0 <= delta <= 200:
            delta = (delta - 100) / 100
            for i in range(self.x):
                for j in range(self.y):
                    rgb = self.pixels[i, j]
                    r = rgb[0] + int(round(rgb[0] * delta / 2, 0))
                    b = rgb[2] + int(round(-1 * rgb[2] * delta / 2, 0))
                    self.pixels_res[i, j] = (r, rgb[1], b)
            self.result.save(self.rname)

    def color(self, color, delta=100):
        if 0 <= delta <= 200:
            delta = (delta - 100)
            for i in range(self.x):
                for j in range(self.y):
                    rgb = list(self.pixels[i, j])
                    rgb[color] += delta
                    if rgb[color] > 255:
                        rgb[color] = 255
                    elif rgb[color] < 0:
                        rgb[color] = 0
                    self.pixels_res[i, j] = (rgb[0], rgb[1], rgb[2])
            self.result.save(self.rname)

    def load(self):
        self.image = Image.open(self.rname)
        self.result = Image.open(self.rname)
        self.pixels = self.image.load()
        self.pixels_res = self.result.load()

    def full(self, db, dc, ds, dw, dr, dg, dbl):
        self.super_result = Funcs(self.rname, self.rname)
        self.super_result.brightness(db)
        self.super_result.load
        self.super_result.contrast(dc)
        self.super_result.load
        self.super_result.saturation(ds)
        self.super_result.load
        self.super_result.warmth(dw)
        self.super_result.load
        self.super_result.color(0, dr)
        self.super_result.load
        self.super_result.color(1, dg)
        self.super_result.load
        self.super_result.color(2, dbl)
