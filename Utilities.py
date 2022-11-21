# Angel Higueros
# 20460
# Proyecto 2

import struct
import numpy as np
from numpy import arccos, arctan2


def _color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


class Texture(object):
    def __init__(self, filename):
        self.filename = filename
        self.read()

    def read(self):
        with open(self.filename, "rb") as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(14 + 4)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for _ in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255

                    self.pixels[y].append((r, g, b))

    def getColor(self, tx, ty):
        if not 0 <= tx < 1 or not 0 <= ty < 1:
            return (0, 0, 0)
        x = int(tx * self.width)
        return self.pixels[int(ty * self.height)][x]


class EnvMap(object):
    def __init__(self, filename):
        self.filename = filename
        self.read()

    def read(self):
        with open(self.filename, "rb") as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(14 + 4)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for _ in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255

                    self.pixels[y].append((r, g, b))

    def getColor(self, dir):  # sourcery skip: avoid-builtin-shadow

        dir = dir / np.linalg.norm(dir)

        x = int(((arctan2(dir[2], dir[0]) / (2 * np.pi)) + 0.5) * self.width)
        y = int(arccos(-dir[1]) / np.pi * self.height)

        return self.pixels[y][x]
