from flock import Flock

myFlock = Flock(150,predator=True)
for m in range (0,200):
  myFlock.update()
  myFlock.drawPlot(m)
