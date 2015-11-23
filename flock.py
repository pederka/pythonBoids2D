from boid import Boid
from pred import Pred
import random

class Flock:

  def __init__(self,number,sd=1337,predator=False):
    random.seed(sd)
    self.boids = []
    self.predPresent = False
    if predator:
      self.predPresent = True
      self.pred = Pred()
    else: self.pred=None
    for n in range(0,number):
      self.boids.append(Boid())

  def update(self):
    # Move flock
    for n in range(0,len(self.boids)):
      self.boids[n].update(self.boids,self.pred)
    # Move predator
    if self.predPresent:
      self.pred.update(self.boids)
