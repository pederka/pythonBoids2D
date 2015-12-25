'''Module for the Boid (Bird-oid-object) class, a superclass for both Bird and Predator'''
from math import sqrt
import random

class Boid(object):
    '''The Boid class, a superclass for bird-like agents'''
    def __init__(self):
        # Parameters for boids
        self.r = 1.0
        self.nd = 0.08 # neighborhood distance
        self.maxspeed = 0.02
        self.maxforce = 0.02
        # Set initial position and velcity
        self.x = random.random()*self.r
        self.y = random.random()*self.r
        self.vx = random.random()*self.maxspeed
        self.vy = random.random()*self.maxspeed

    def borders(self):
        ''' Enforces periodic boundary condition

        After being called, variables x and y are in the interval [0,r]
        '''
        if self.x < 0:
            self.x = self.r + self.x
        if self.y < 0:
            self.y = self.r + self.y
        if self.x > self.r:
            self.x = self.x - self.r
        if self.y > self.r:
            self.y = self.y - self.r

    def move(self):
        ''' Updates position of the boid based on current velocity
        '''
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.borders()

    def distance(self, other):
        ''' Returns the Euclidian distance between the boid and another
        '''
        xdist = min(abs(self.x-other.x), self.r-abs(self.x-other.x))
        ydist = min(abs(self.y-other.y), self.r-abs(self.y-other.y))
        return sqrt(xdist**2+ydist**2)

    def distanceVector(self, other):
        ''' Returns the normalized distance vector between the boid and another

        Output is the x and y components of normalized distance vector
        '''
        xdist = min(abs(self.x-other.x), self.r-abs(self.x-other.x))
        ydist = min(abs(self.y-other.y), self.r-abs(self.y-other.y))
        if self.x > other.x and self.r-abs(self.x-other.x) > abs(self.x-other.x):
            dx = -xdist
        else:
            dx = xdist
        if self.y > other.y and self.r-abs(self.y-other.y) > abs(self.y-other.y):
            dy = -ydist
        else:
            dy = ydist
        if dx == 0 and dy == 0:
            return 0, 0
        return dx/sqrt(dx**2+dy**2), dy/sqrt(dx**2+dy**2)
