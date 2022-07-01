# Python code for custom simulation of CSMA/CD network with exponential back off.

import random

# random.randrange()

loopTracker = 0
average = 0
collisionCounter = 0

slot_time = 51.2e-6

# Number of hosts = 1, 10, 50, 100
N = int(input("\nEnter the number of hosts = "))

# Number of runs
R = int(input("\nEnter the number of simulation runs = "))

# Simulation
for i in range(0, R):
    
    collisionCounter = 0
    loopTracker = 0
    
    for j in range(0, N):
        pass
    
# Could not figure out how to code this problem.