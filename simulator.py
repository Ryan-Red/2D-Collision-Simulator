import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np

from particle import particle 

class simulator:
    def __init__(self,numParticles=10,gridSize=[100,100],dt=0.1):

        self.numParticles = numParticles
        self.gridSize = gridSize
        self.dt = dt

        minDim = min(gridSize)/2 #/2 because grid goes from -D/2 to D/2 on both axes
        velFactor = 10
        posFactor = 1
        radFactor = minDim/2

        radii = np.random.rand(numParticles)*radFactor
        initVs = (np.random.rand(numParticles,2)- 0.5)*2 * minDim/velFactor #2D simulator (for now)
        initPs = (np.random.rand(numParticles,2)-0.5)*2 * minDim/posFactor

        self.particleList = []
        i = 0
        for i in range(0,numParticles,1):
            part = particle(radii[i],initPs[i],initVs[i])
            self.particleList.append(part)

        self.setup()

    def animate(self,i):
        i = 0
        self.axis.clear()
        for i in range(0,self.numParticles):
            xdata, ydata = [], []
            xdata, ydata = self.particleList[i].drawParticle(self.dt)
            self.axis.plot(xdata,ydata)
        plt.xlim([-(int)(self.gridSize[0]/2), (int)(self.gridSize[0]/2)])
        plt.ylim([-(int)(self.gridSize[1]/2), (int)(self.gridSize[1]/2)])

    def runAnimation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
                               frames = 500, interval = 20) 
        plt.show()

    def setup(self):
        self.fig = plt.figure() 
        self.axis = plt.axes(xlim =(-(int)(self.gridSize[0]/2), (int)(self.gridSize[0]/2)),
                             ylim =(-(int)(self.gridSize[1]/2), (int)(self.gridSize[1]/2)))
        
sim  = simulator(numParticles=30)
sim.runAnimation()

# anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)