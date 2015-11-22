from math import sqrt
import random

class Pred:

  def __init__(self):
    # Parameters for boids
    self.r = 1.0 # Size of domain
    self.nd = 0.25 # neighbor distance
    self.maxspeed = 0.02
    self.maxforce = 0.02
    # Set random values
    self.x = random.random()*self.r 
    self.y = random.random()*self.r
    self.vx = random.random()*self.maxspeed
    self.vy = random.random()*self.maxspeed

  def borders(self):
    if self.x < 0: self.x = self.r + self.x
    if self.y < 0: self.y = self.r + self.y
    if self.x > self.r: self.x = self.x - self.r
    if self.y > self.r: self.y = self.y - self.r

  def move(self):
    self.x = self.x + self.vx
    self.y = self.y + self.vy
    self.borders()

  def update(self,others):
    self.chase(others)
    self.move()

  def chase(self,others):
   coh = self.cohesion(others)
   self.vx = self.vx + coh[0]
   self.vy = self.vy + coh[1]
   # Normalize to maxspeed
   v = sqrt(self.vx**2+self.vy**2)
   if (v > self.maxspeed):
     self.vx = self.vx/v*self.maxspeed
     self.vy = self.vy/v*self.maxspeed

  def distance(self,other):
    xdist = min(abs(self.x-other.x),self.r-abs(self.x-other.x))
    ydist = min(abs(self.y-other.y),self.r-abs(self.y-other.y))
    return sqrt(xdist**2+ydist**2)

  def distanceVector(self,other):
    # Returns normalized distance vector
    xdist = min(abs(self.x-other.x),self.r-abs(self.x-other.x))
    ydist = min(abs(self.y-other.y),self.r-abs(self.y-other.y))
    if self.x > other.x and self.r-abs(self.x-other.x) > abs(self.x-other.x):
      dx = -xdist
    else:
      dx = xdist
    if self.y > other.y and self.r-abs(self.y-other.y) > abs(self.y-other.y):
      dy = -ydist
    else:
      dy = ydist
    return dx/sqrt(dx**2+dy**2),dy/sqrt(dx**2+dy**2)

  def cohesion(self,others):
    # Steer to align speed with boids within desired distance
    count = 0
    steerx = 0
    steery = 0
    xavg = 0
    yavg = 0
    for n in range(0,len(others)):
      dist = self.distance(others[n])
      if dist < self.nd and dist > 0.0:
        count = count + 1
        xavg = xavg + others[n].x
        yavg = yavg + others[n].y
    if count > 0:
      xavg = xavg / count
      yavg = yavg / count
      # Create ghost boid representing the others
      ghost = Pred()
      ghost.x = xavg
      ghost.y = yavg
      steerx,steery = self.distanceVector(ghost)
      l = sqrt(steerx**2+steery**2)
      steerx = steerx/l*self.maxforce
      steery = steery/l*self.maxforce
      steerx = steerx - self.vx
      steery = steery - self.vy
    return steerx, steery
