import math

# Frequency (Hz)
f = 2.4e9
# Distance (m)
d = 10
# Speed of light (m/s)
c = 3e8

print("\n")

freeSpacePathLoss = ((4 * math.pi * f * d) / c) ** 2
print(freeSpacePathLoss)

print("\n")