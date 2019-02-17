"""
Matrix class
Louis Dous Hervé - 2019
"""

# Je sais pas pourquoi je code "en anglais" mais je commente en français,
# alors me demande pas

import os
import copy
import numbers
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
        # elif not isinstance(value, numbers.Number):
        #     raise TypeError("Value should be a number ('{}' is not a number)".format(value))
        else:
            self.data[key] = Fraction(str(value))

class Matrix:
    
    """ Creates a new matrix with n rows and p columns"""
    def __init__(self, n, p, value = 0, *args):
        self.n = n
        self.p = p
        self.data = list()

        for _ in range(self.n):
            self.data.append(Array(p, value))

    def __getitem__(self, key):
        if key < 0 or key >= self.n:
            raise ValueError("Index {} out of bounds ({} rows)".format(key, self.n))            
        else:
            return self.data[key]
    
    @staticmethod
    def identity(n):
        m = Matrix(n, n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    m.data[i][j] = 1

        return m

    def pow(self, power):
        m = copy.deepcopy(self)
        for i in range(m.n):
            for j in range(m.p):
                m[i][j] = m[i][j] ** power
        return m

    def multiplyByConstant(self, k):
        r = copy.deepcopy(self)
        for i in range(self.n):
            for j in range(self.p):
                r[i][j] *= k
        return r

    def multiply(self, m):
        if not type(m) == Matrix:
            return self.multiplyByConstant(Fraction(str(m)))

        if self.p != m.n:
            raise ValueError("The number of columns of the left matrix is not equal to the number of rows of the right one")

        r = Matrix(self.n, m.p)

        for i in range(r.n):
            for j in range(r.p):
                for k in range(self.p):
                    # J'ai dû réfléchir au moins 10 min pour arriver à cette formule de merde...
                    r[i][j] += self[i][k] * m[k][j]

        return r

    def add(self, m):
        if not type(m) is Matrix:
            raise TypeError("Matrices can only be added with matrices")
        if m.n != self.n or m.p != self.p:
            raise ValueError("Matrices can only be added with same size matrices ({}x{} ; {}x{})".format(self.n, self.p, m.n, m.p))

        r = Matrix(self.n, self.p)

        for i in range(m.n):
            for j in range(m.p):
                r[i][j] = self[i][j] + m[i][j]

        return r

    def getDeterminant(self):
        if self.getSize() != (2, 2):
            raise TypeError("Sorry, but currently, this program is only able to invert 2x2 matrices.")
        else:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

    def isInvertible(self):
        if self.getSize() != (2, 2):
            raise TypeError("Sorry, but currently, this class is only able to invert 2x2 matrices.")
        else:
            return self.getDeterminant() != 0

    def invert(self):
        if self.isInvertible():
            r = Matrix(2, 2)
            r[0][0] = self[1][1]
            r[0][1] = -self[0][1]
            r[1][0] = -self[1][0]
            r[1][1] = self[0][0]
            r *= Fraction(1, self.getDeterminant())

            return r
        else:
            ValueError("This matrix is not invertible... (or I just can't caluclate its inverse)")

    def getSize(self):
        return (self.n, self.p)

    def isSquare(self):
        return self.n == self.p

    def __mul__(self, other):
        return self.multiply(other)

    # def __imul__(self, other):
    #     return self.multiplyByConstant(Fraction(str(other)))

    def __add__(self, other):
        return self.add(other)

    # def __iadd__(self, other):
    #     return self.add(other)

    def __sub__(self, other):
        return self.add(other * -1)

    def __isub__(self, other):
        return self.add(other * -1)

    def __pow__(self, other):
        if other < -1:
            ValueError("Cannot calculate the result of a matrix to that power ({} < -1)")

        if other == -1:
            return self.invert()

        if other == 0:
            if self.isSquare():
                return Matrix.identity(self.n)
            else:
                raise ValueError("Cannot raise a non-square matrix to the power of 0")
            
        return self.pow(other)

    def toString(self, pretty = False):
        if pretty:
            stringified = ""
            longest = 0

            for i in range(self.n):
                for j in range(self.p):
                    l = len(str(self.data[i][j]))
                    if l > longest:
                        longest = l

            for i in range(self.n):
                for j in range(self.p):
                    s = str(self.data[i][j])
                    l = len(s)
                    stringified += s + ' '

                    for _ in range(longest - l):
                        stringified += ' '
                
                stringified += os.linesep

            return stringified

        s = "["
        for i in range(self.n):
            s += '['

            for j in range(self.p):
                s += ', ' if j != 0 else ''
                s += str(self.data[i][j])
            s += ']' + (', ' if i < self.p - 1 else '')

        s += ']'
        return s

    def __str__(self):
        # return self.toString()
        return self.toString(True)

    def __repr__(self):
        return self.toString(True).strip()
                