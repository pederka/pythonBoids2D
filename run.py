import matplotlib.pyplot as plt
import matplotlib as mpl
from flock import Flock
import time


myFlock = Flock(200,predator=True)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
plt.show()
plt.xlim(0,1)
plt.ylim(0,1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

for m in range (0,200):
  plt.xlim(0,1)
  plt.ylim(0,1)
  #time.sleep(0.02)
  for n in range(0,len(myFlock.boids)):
    ax.plot(myFlock.boids[n].x,myFlock.boids[n].y,'o',color='black')
  ax.plot(myFlock.pred.x,myFlock.pred.y,'o',color='red')
  plt.savefig("png/"+str(m).zfill(4)+".png")
  plt.draw()
  ax.clear()
  myFlock.update()
