import random
from boid import Boid

class Flock:

  def __init__(self,number,sd=1337):
    random.seed(sd)
    self.boids = []
    for n in range(0,number):
      x = random.random() 
      y = random.random()
      vx = random.random()*0.02
      vy = random.random()*0.02
      self.boids.append(Boid(x,y,vx,vy))

  def update(self):
    for n in range(0,len(self.boids)):
      self.boids[n].update(self.boids)
