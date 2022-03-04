import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
  

class particle:
    def __init__(self, radius, p_0,v_0,epsilon=1):
        self.rad = radius

        self.mass = radius
        self.inverseMass = 1/self.mass

        self.p = p_0 #2d position vector [x, y]

        self.v = v_0 #2d velocity vector [v_x, v_y]

        self.epsilon = epsilon

    def setVelocity(self, v ):
        self.v = v

    def addImpulse(self, j):
        self.v = j * self.inverseMass + self.v

    def updatePostion(self, dt):
        self.p = self.p + dt * self.v

    def drawParticle(self,dt):

        self.updatePostion(dt)

        thetas = np.linspace(0,2*np.pi,num=30)

        self.xdata = np.add(self.rad*np.cos(thetas), self.p[0])
        self.ydata = np.add(self.rad*np.sin(thetas), self.p[1])

        return self.xdata, self.ydata

    