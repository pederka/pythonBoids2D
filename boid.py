from math import sqrt

class Boid:

  def __init__(self,x,y,vx,vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    # Parameters for boids
    self.r = 1.0 # Size of domain
    self.dd = 0.02 # Desired distance
    self.nd = 0.08 # neighbor distance
    self.maxspeed = 0.02
    self.maxforce = 0.02
    self.sepmult = 1.5
    self.almult = 1.0
    self.cohmult = 0.1

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
    self.flock(others)
    self.move()

  def flock(self,others):
   sep = self.separate(others)
   ali = self.align(others)
   coh = self.cohesion(others)
   # Add contributions
   correctionx = self.sepmult*sep[0] + self.almult*ali[0] + self.cohmult*coh[0]
   correctiony = self.sepmult*sep[1] + self.almult*ali[1] + self.cohmult*coh[1] 
   self.vx = self.vx + correctionx
   self.vy = self.vy + correctiony
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
    if self.x > other.x and self.r - self.x > self.dd:
      dx = -xdist
    else:
      dx = xdist
    if self.y > other.y and self.r - self.y > self.dd:
      dy = -ydist
    else:
      dy = ydist
    return dx/sqrt(dx**2+dy**2),dy/sqrt(dx**2+dy**2)

  def separate(self,others):
    # Steer away for any other boids within desired distance
    count = 0
    steer = [0,0]
    steerx = 0
    steery = 0
    for n in range(0,len(others)):
      dist = self.distance(others[n])
      if dist < self.dd and dist > 0.0:
        count = count + 1
        sx,sy = self.distanceVector(others[n])
        sx = -sx / dist
        sy = -sy / dist
        steerx = steerx + sx
        steery = steery + sy
    if count > 0:
      # Normalize and subtract velocity
      l = sqrt(steerx**2+steery**2)
      steerx = steerx/l*self.maxforce
      steery = steery/l*self.maxforce
      steerx = steerx - self.vx
      steery = steery - self.vy
    return steerx, steery

  def align(self,others):
    # Steer to align speed with boids within desired distance
    count = 0
    steerx = 0
    steery = 0
    for n in range(0,len(others)):
      dist = self.distance(others[n])
      if dist < self.nd and dist > 0.0:
        count = count + 1
        steerx = steerx + others[n].vx
        steery = steery + others[n].vy
    if count > 0:
      l = sqrt(steerx**2+steery**2)
      steerx = steerx/l*self.maxforce
      steery = steery/l*self.maxforce
      steerx = steerx - self.vx
      steery = steery - self.vy
    return steerx, steery

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
      ghost = Boid(xavg,yavg,0,0)
      steerx,steery = self.distanceVector(ghost)
      l = sqrt(steerx**2+steery**2)
      steerx = steerx/l*self.maxforce
      steery = steery/l*self.maxforce
      steerx = steerx - self.vx
      steery = steery - self.vy
    return steerx, steery
