import matplotlib.pyplot as plt
import numpy as np

# R = Transmission speed
# d = distance/length of the link

print("\n")

dList = []
RList = []
# For scientific notation
RListSN = []

for d in range(1, 11):
    R = (2 * 10e11 / d)
    # print(R)
    dList.append(d)
    RList.append(R)
    RListSN.append("{:.0e}".format((2 * 10e11 / d)))

print("\nLine distance values in metres - ", dList)
# print("\nTransmission speed values in bps- ", RList)
print("\nTransmission speed values in bps - ", RListSN)

# print("\nNumber of items in the link distance list = ", len(dList))
# print("\nNumber of items in the transmission speed list = ", len(RList))

xpoints = np.array(dList)
ypoints = np.array(RList)

plt.plot(xpoints, ypoints, color = 'green')

plt.xticks(xpoints)
plt.yticks(ypoints)

plt.xlabel("Line Distance (m)")
plt.ylabel("Transmission speed (bps)")

plt.title("Line Distance vs Transmission Speed")

plt.grid()

# PNG, JPG, PDF, etc.
plt.savefig('/Users/abhijeetsingh/PYTHON/CS6865_A2_Q1/Assignment_2_Question_1_Using_Matplotlib.png')

plt.show()

print("\n")