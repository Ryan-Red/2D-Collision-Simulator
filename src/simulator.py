import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib as mpl 

from particle import particle 

mpl.rcParams['animation.ffmpeg_path'] = r'/opt/homebrew/bin/ffmpeg'

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
            while(self.leftRightWallCollision(radii[i],trialPos) == True or self.topDownWallCollision(radii[i],trialPos) == True or self.checkObjectCollision(radii[i],trialPos,radii[0:i],initPs) == True):
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
        plt.title("2D Collision Simulator")

    def runAnimation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
                               frames = 500, interval = 5) 

        f = r"animation.mp4" 
        writervideo = animation.FFMpegWriter(fps=60) 
        anim.save(f, writer=writervideo)
        # plt.show()
    
    def getDistance(self,pos1, pos2):

        return np.linalg.norm(pos1-pos2,axis=0)


    def checkObjectCollision(self,radius,pos,radiiList,particleList):
        i = 0

        for i in range(0,len(particleList),1):
            distCenter = self.getDistance(pos,particleList[i])
            minDist = radius + radiiList[i]

            if(distCenter <= minDist):
                return True

        return False



    def leftRightWallCollision(self, radius, pos):

        if((pos[0] + radius) >= self.xlim[1]) or ((pos[0] - radius) <= self.xlim[0]):
            return True
        return False

    def topDownWallCollision(self,radius,pos):
        if((pos[1] + radius) >= self.ylim[1]) or ((pos[1] - radius) <= self.ylim[0]):
            return True
        return False


    def getCollisionNormalVector(self,idx0,idx1):
        n = self.particleList[idx0].p - self.particleList[idx1].p
        n_normalized = n/np.linalg.norm(n,axis=0)
        return n_normalized

    def getCollisionImpulse(self,idx0,idx1,n_normalized):

        epsilon = np.min([self.particleList[idx0].epsilon, self.particleList[idx1].epsilon]) #Coefficient of Restitution for the collision

        v_rel = self.particleList[idx0].v - self.particleList[idx1].v # Relative Velocity
        mu = 1/(self.particleList[idx0].inverseMass + self.particleList[idx1].inverseMass) #Reduced mass

        impulse_j = -1* (1 + epsilon) * np.dot(v_rel,n_normalized) * mu
        
        return impulse_j


    def getObjectCollision(self,idx):
        
        target = self.particleList[idx]
        i = 0
        for i in range(idx+1,self.numParticles,1):
                distCenter = self.getDistance(target.p,self.particleList[i].p)
                minDist = target.rad + self.particleList[i].rad

                if(distCenter <= minDist):
                    n_normalized = self.getCollisionNormalVector(idx,i)
                    impulse_j = self.getCollisionImpulse(idx,i,n_normalized)

                    self.particleList[idx].addImpulse(impulse_j* n_normalized)
                    self.particleList[i].addImpulse(-impulse_j * n_normalized)

                    return True

        return True

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


            self.getObjectCollision(i)
        
    def setup(self):
        self.fig = plt.figure() 
        self.axis = plt.axes(xlim =(-(int)(self.gridSize[0]/2), (int)(self.gridSize[0]/2)),
                             ylim =(-(int)(self.gridSize[1]/2), (int)(self.gridSize[1]/2)))
        
sim  = simulator(numParticles=10)
sim.runAnimation()

# anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)