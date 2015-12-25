'''Module containing the Flock class, meant for containing a group of Bird and
Predator objects
'''
import random
import matplotlib.pyplot as plt
from predator import Predator
from bird import Bird

class Flock(object):
    ''' Class for groups of birds and a possible predator
    '''

    def __init__(self, number, seed=1337, predator=False):
        random.seed(seed)
        self.birds = []
        self.predPresent = False
        if predator:
            self.predPresent = True
            self.predator = Predator()
        else:
            self.predator = None
        for n in range(0,number):
            self.birds.append(Bird())
        # Initialize plot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.ion()
        plt.show()
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)

    def update(self):
        ''' Updates position of all birds and the predator according to rules of
        behavior
        '''
        # Move flock
        for n in range(0, len(self.birds)):
            self.birds[n].update(self.birds, self.predator)
        # Move predator
        if self.predPresent:
            self.predator.update(self.birds)

    def drawPlot(self, m):
        '''  Updates plot
        '''
        for n in range(0, len(self.birds)):
            self.ax.quiver(self.birds[n].x, self.birds[n].y, self.birds[n].vx,
                           self.birds[n].vy)
        if self.predator:
            self.ax.quiver(self.predator.x, self.predator.y,
                           self.predator.vx, self.predator.vy, color='red')
        plt.savefig("png/"+str(m).zfill(4)+".png") # Write to file
        plt.draw()
        self.ax.clear()
