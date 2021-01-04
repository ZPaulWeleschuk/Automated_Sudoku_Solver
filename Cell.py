""" Cell class that represents each tile on a sudoku board"""


class Cell:
    def __init__(self, originalValue, newValue, xpixel, ypixel):
        self.originalValue = originalValue
        self.newValue = newValue
        self.xpixel = xpixel
        self.ypixel = ypixel
