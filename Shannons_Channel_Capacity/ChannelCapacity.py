import math

# Boltzmann's constant
k = 1.38e-23
# Temperature (K)
T = 400
# Bandwidth (Hz)
B = 2e6
# Frequency (Hz)
f = 1e9
# Distance (m)
d = 1000
# Speed of light (m/s)
c = 3e8
# Transmitter power (W)
P = 0.001

print("\n")

print("SHANNON'S CHANNEL CAPACITY")

print("\n")

thermalNoise = (k * T * B)
print("Thermal noise, N =", thermalNoise, "W")

freeSpacePathLoss = ((4 * math.pi * f * d) / c) ** 2
print("Free space path loss, L =", freeSpacePathLoss, "W")

receivedSignalStrength = (P / freeSpacePathLoss)
print("Received signal strength, S =", receivedSignalStrength, "W")

channelCapacity = B * math.log2(1 + (receivedSignalStrength/thermalNoise))
print("Channel capacity, C =", channelCapacity, "bps")

print("\n")