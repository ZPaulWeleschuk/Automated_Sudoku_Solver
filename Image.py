""" Image class that stores an image and its associated attributes"""


class Image:
    def __init__(self, image, value, threshold, b, g, r):
        self.image = image
        self.value = value
        self.threshold = threshold
        self.b = b
        self.g = g
        self.r = r
