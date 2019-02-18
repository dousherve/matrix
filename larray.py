"""
Array class - 
Louis Dous Hervé - 2019
"""

from fractions import Fraction

class Array:

    def __init__(self, size, value = 0):
        self.size = size
        self.data = [Fraction(str(value))] * self.size

    def __getitem__(self, key):
        if key < 0 or key >= self.size:
            raise ValueError("Index {} out of bounds ({} columns)".format(key, self.size))
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.size:
            raise ValueError("Index {} out of bounds ({} columns)".format(key, self.size))

        try:
            self.data[key] = Fraction(str(value))
        except ValueError:
            print("Invalid literal for Fraction object")