'''Module for the Bird class'''
from math import sqrt
from boid import Boid

class Bird(Boid):
    '''Class for bird-like agent following the three rules of Reynolds'''

    def __init__(self):
        super(Bird, self).__init__()
        self.dd = 0.02 # Desired minimum distance to other birds
        self.pd = 0.2 # Desired distance to predators
        self.sepmult = 1.5
        self.almult = 1.0
        self.cohmult = 0.1
        self.premult = 3.5
        self.alpha = -1 # Parameter for cone of vision

    def update(self, others, pred=None):
        ''' Applies rules of behavior and updates positions
        '''
        self.flock(others, pred)
        self.move()

    def flock(self, others, pred):
        ''' Updates velocity according to rules of behavior

        Implements the three rules of Reynolds pluss hiding from a predator if
        present
        '''
        sep = self.separate(others)
        ali = self.align(others)
        coh = self.cohesion(others)
        if pred != None:
            pre = self.hide(pred)
        else:
            pre = (0, 0)
        # Add contributions
        correctionx = self.sepmult*sep[0] + self.almult*ali[0]  \
                         + self.cohmult*coh[0] + self.premult*pre[0]
        correctiony = self.sepmult*sep[1] + self.almult*ali[1]  \
                         + self.cohmult*coh[1] + self.premult*pre[1]
        self.vx = self.vx + correctionx
        self.vy = self.vy + correctiony
        # Normalize to maxspeed
        velocity = sqrt(self.vx**2+self.vy**2)
        if velocity > self.maxspeed:
            self.vx = self.vx/velocity*self.maxspeed
            self.vy = self.vy/velocity*self.maxspeed

    def separate(self, others):
        ''' Returns acceleration to steer away for any other boids within
        desired distance
        '''
        count = 0
        steerx = 0
        steery = 0
        for n in range(0, len(others)):
            dist = self.distance(others[n])
            if dist < self.dd and dist > 0.0:
                count = count + 1
                sx, sy = self.distanceVector(others[n])
                sx = -sx / dist
                sy = -sy / dist
                steerx = steerx + sx
                steery = steery + sy
        if count > 0:
            # Normalize and subtract velocity
            length = sqrt(steerx**2+steery**2)
            steerx = steerx/length*self.maxforce
            steery = steery/length*self.maxforce
            steerx = steerx - self.vx
            steery = steery - self.vy
        return steerx, steery

    def align(self, others):
        ''' Return acceleration to align speed with boids within desired
        distance
        '''
        count = 0
        steerx = 0
        steery = 0
        for n in range(0, len(others)):
            dist = self.distance(others[n])
            sx, sy = self.distanceVector(others[n])
            # Add acceleration for any birds within the cone of vision
            if dist < self.nd and dist > 0.0 and \
                  (sx*self.vx+sy*self.vy)/(self.vx**2+self.vy**2) > self.alpha:
                count = count + 1
                steerx = steerx + others[n].vx
                steery = steery + others[n].vy
        if count > 0:
            length = sqrt(steerx**2+steery**2)
            steerx = steerx/length*self.maxforce
            steery = steery/length*self.maxforce
            steerx = steerx - self.vx
            steery = steery - self.vy
        return steerx, steery

    def cohesion(self, others):
        ''' Return acceleration towards center of mass of nearby birds
        '''
        count = 0
        steerx = 0
        steery = 0
        xavg = 0
        yavg = 0
        for n in range(0, len(others)):
            dist = self.distance(others[n])
            sx, sy = self.distanceVector(others[n])
            # Add acceleration for any birds within the cone of vision
            if dist < self.nd and dist > 0.0 and \
                  (sx*self.vx+sy*self.vy)/(self.vx**2+self.vy**2) > self.alpha:
                count = count + 1
                xavg = xavg + others[n].x
                yavg = yavg + others[n].y
        if count > 0:
            xavg = xavg / count
            yavg = yavg / count
            # Create ghost boid representing the center of mass of the others
            ghost = Boid()
            ghost.x = xavg
            ghost.y = yavg
            steerx, steery = self.distanceVector(ghost)
            length = sqrt(steerx**2+steery**2)
            steerx = steerx/length*self.maxforce
            steery = steery/length*self.maxforce
            steerx = steerx - self.vx
            steery = steery - self.vy
        return steerx, steery

    def hide(self, pred):
        ''' Return acceleration to steer away for a predator
        '''
        steerx = 0
        steery = 0
        dist = self.distance(pred)
        if dist < self.pd and dist > 0.0:
            sx, sy = self.distanceVector(pred)
            steerx = -sx / dist
            steery = -sy / dist
            length = sqrt(steerx**2+steery**2)
            steerx = steerx/length*self.maxforce
            steery = steery/length*self.maxforce
            steerx = steerx - self.vx
            steery = steery - self.vy
        return steerx, steery
