## Conda environment "env_testing"

from turtle import color
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ypoints = np.array([395.42, 355.47, 332.07, 315.47, 302.59, 292.07, 283.17, 275.47, 268.67, 262.59])

plt.plot(xpoints, ypoints, color = 'green')

plt.xticks(xpoints)
plt.yticks(ypoints)

plt.xlabel("Distance (m)")
plt.ylabel("Channel capacity (Mbps)")

plt.title("Channel Capacity vs Distance")

plt.grid()

# PNG, JPG, PDF, etc.
plt.savefig('/Users/abhijeetsingh/PYTHON/University_Assignments/CS6865_A1_Q3/Assignment_1_Question_3_Using_Matplotlib.png')

plt.show()