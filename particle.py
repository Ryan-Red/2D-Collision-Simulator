import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
  

class particle:
    def __init__(self, radius, p_0,v_0):
        self.rad = radius

        self.p = p_0 #2d position vector [x, y]

        self.v = v_0 #2d velocity vector [v_x, v_y]


    def setVelocity(self, v ):
        self.v = v

    def updatePostion(self, dt):
        self.p = self.p + dt * self.v

    def drawParticle(self,dt):

        self.updatePostion(dt)

        thetas = np.linspace(0,2*np.pi,num=30)

        xdata = np.add(self.rad*np.cos(thetas), self.p[0])
        ydata = np.add(self.rad*np.sin(thetas), self.p[1])

        return xdata, ydata

    