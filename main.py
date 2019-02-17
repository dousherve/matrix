from matrix import *

a = Matrix(2, 5)
b = Matrix(5, 3)

a[0][0] = 1
a[0][1] = 4
a[0][2] = 3
a[0][3] = 8
a[0][4] = 9
a[1][0] = 3
a[1][1] = 7
a[1][2] = 5
a[1][3] = 1
a[1][4] = 2

print(a)

b[0][0] = 8
b[0][1] = 13
b[0][2] = 9
b[1][0] = 14
b[1][1] = 1
b[1][2] = 7
b[2][0] = 11
b[2][1] = 8
b[2][2] = 5
b[3][0] = 9
b[3][1] = 5
b[3][2] = 3
b[4][0] = 2
b[4][1] = 4
b[4][2] = 6

print(b)

ab = a * b
print(ab)

ab *= -1
print(ab)

c = Matrix(2, 2)
c[0][0] = 4
c[0][1] = 3
c[1][0] = 7
c[1][1] = 9

print("det C = {}".format(c.getDeterminant()))

print(c.invert())