# Py code implementing the 1-server computational PIR for a non-binary database using Paillier encryption and decryption (Tutorial 7)

# Conda environment "env_testing"

import numpy as np
import gmpy2
from gmpy2 import mpz

# Random 2D matrix of size 4 by 4 with values from 0 to 10
x = np.random.randint(11, size = (4, 4))
print("\n", x)
print("\nElement at index (1, 4) = ", x[0][3])
# print("\nElement at index (1, 4) = ", x[0, 3])

p = 7
q = 11
n = (p * q)
g = (n + 1)
l = (p - 1) * (q - 1)
r = 4
nsquare = (n ** 2)

print("\nPublic key = (", g, ",", n, ")")
print("Private key = (", p, ",", q, ",", l, ")")

# Construct a query for the index (1, 4)

# Query for row 1
row1 = (0 * x[0, 0]) + (0 * x[0, 1]) + (0 * x[0, 2]) + (1 * x[0, 3])
# print(row1)
print("\nRow 1 Column 4")
print("Before encryption = ", row1)
c1 = int(((g ** row1) * (r ** n)) % nsquare)
print("After encryption = ", c1)

# Query for row 2
row2 = (0 * x[1, 0]) + (0 * x[1, 1]) + (0 * x[1, 2]) + (1 * x[1, 3])
# print(row2)
print("\nRow 2 Column 4")
print("Before encryption = ", row2)
c2 = int(((g ** row2) * (r ** n)) % nsquare)
print("After encryption = ", c2)

# Query for row 3
row3 = (0 * x[2, 0]) + (0 * x[2, 1]) + (0 * x[2, 2]) + (1 * x[2, 3])
# print(row3)
print("\nRow 3 Column 4")
print("Before encryption = ", row3)
c3 = int(((g ** row3) * (r ** n)) % nsquare)
print("After encryption = ", c3)

# Query for row 4
row4 = (0 * x[3, 0]) + (0 * x[3, 1]) + (0 * x[3, 2]) + (1 * x[3, 3])
# print(row4)
print("\nRow 4 Column 4")
print("Before encryption = ", row4)
c4 = int(((g ** row4) * (r ** n)) % nsquare)
print("After encryption = ", c4, "\n")

combinedQuery = (c1, c2, c3, c4)
print("All encrypted column 4 values = ", combinedQuery)

x = int((combinedQuery[0] ** l) % nsquare)
# print(x)
y = int(pow(l, -1, n))
# print(y)
z = int((x - 1) / 77)
# print(z)
p = int((z * y) % n)
print("\nAfter decryption, element at index (1, 4) = ", p, "\n")

# Was not able to get this code to work.

# Was supposed to use a 100 x 100 database. But instead just implemented the example from tutorial 7.