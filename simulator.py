import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np

from particle import particle 

class simulator:
    def __init__(self,numParticles=10,gridSize=[100,100],dt=0.1):

        self.numParticles = numParticles
        self.gridSize = gridSize
        self.dt = dt
        self.xlim = [-(int)(self.gridSize[0]/2), (int)(self.gridSize[0]/2)]
        self.ylim = [-(int)(self.gridSize[1]/2), (int)(self.gridSize[1]/2)]

        minDim = min(gridSize)/2 #/2 because grid goes from -D/2 to D/2 on both axes
        velFactor = 10
        posFactor = 1
        radFactor = minDim/6

        radii = np.random.rand(numParticles)*radFactor
        initVs = (np.random.rand(numParticles,2)- 0.5)*2 * minDim/velFactor #2D simulator (for now)

        i = 0
        initPs = []
        for i in range(0,self.numParticles,1):
            trialPos = (np.random.rand(2)-0.5) * minDim
            while(self.leftRightWallCollision(radii[i],trialPos) == True or self.topDownWallCollision(radii[i],trialPos) == True):
                trialPos = (np.random.rand(2)-0.5) * minDim

            print(trialPos)
            initPs.append(trialPos)



        self.particleList = []
        i = 0
        for i in range(0,numParticles,1):
            part = particle(radii[i],initPs[i],initVs[i])
            self.particleList.append(part)

        self.setup()

    def animate(self,i):
        i = 0
        self.axis.clear()
        self.checkCollision()
        for i in range(0,self.numParticles):
            xdata, ydata = [], []
            
            xdata, ydata = self.particleList[i].drawParticle(self.dt)
            self.axis.plot(xdata,ydata)
        plt.xlim(self.xlim)
        plt.ylim(self.ylim)

    def runAnimation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
                               frames = 500, interval = 10) 
        plt.show()
    
    def leftRightWallCollision(self, radius, pos):

        if((pos[0] + radius) >= self.xlim[1]) or ((pos[0] - radius) <= self.xlim[0]):
            return True
        return False

    def topDownWallCollision(self,radius,pos):
        if((pos[1] + radius) >= self.ylim[1]) or ((pos[1] - radius) <= self.ylim[0]):
            return True
        return False

    def checkCollision(self):
        i = 0
        for i in range(0, self.numParticles,1):
            particle = self.particleList[i]

            # Hitting the left or right walls
            if(self.leftRightWallCollision(particle.rad, particle.p) == True):
                vel = particle.v
                vel[0] = -1*vel[0]

                self.particleList[i].setVelocity(vel)

            if(self.topDownWallCollision(particle.rad, particle.p) == True):

                vel = particle.v
                vel[1] = -1*vel[1]

                self.particleList[i].setVelocity(vel)




        
    def setup(self):
        self.fig = plt.figure() 
        self.axis = plt.axes(xlim =(-(int)(self.gridSize[0]/2), (int)(self.gridSize[0]/2)),
                             ylim =(-(int)(self.gridSize[1]/2), (int)(self.gridSize[1]/2)))
        
sim  = simulator(numParticles=10)
sim.runAnimation()

# anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)