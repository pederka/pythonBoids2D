'''Simple script for running the program'''
from flock import Flock

# Parameters
time_steps = 200
number_of_birds = 150
is_predator_present = True

# Initialize flock
myFlock = Flock(number_of_birds, predator=is_predator_present)

# Run simulation
for m in range(0, time_steps):
    myFlock.update()
    myFlock.drawPlot(m)
