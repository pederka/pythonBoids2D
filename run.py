from flock import Flock

myFlock = Flock(100,predator=True)
for m in range (0,126):
  myFlock.update()
  myFlock.drawPlot(m)
