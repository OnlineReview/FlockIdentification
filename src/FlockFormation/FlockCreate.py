from math import sqrt, asin, degrees,tan,radians
from GridFormation.Point import Point

class FlockCreate(object):
    '''
    classdocs
    '''


    def __init__(self, radius):
        '''
        Constructor
        '''
        self.h1=0
        self.h2=0
        self.k1=0
        self.k2=0
        self.radius=radius
        
    def findCentres(self,pt1,pt2):
        x1=pt1.x
        y1=pt1.y
        x2=pt2.x
        y2=pt2.y
        dist=sqrt((x1-x2)**2+(y1-y2)**2)
        x3=(x1+x2)/2
        y3=(y1+y2)/2
        
        self.h1 = x3 + sqrt(abs(self.radius**2-(dist/2)**2))*(y1-y2)/dist 
        self.k1 = y3 + sqrt(abs(self.radius**2-(dist/2)**2))*(x2-x1)/dist
        self.h2 = x3 - sqrt(abs(self.radius**2-(dist/2)**2))*(y1-y2)/dist
        self.k2 = y3 - sqrt(abs(self.radius**2-(dist/2)**2))*(x2-x1)/dist
        
    def findFlocks(self,centre, cluster,membership): 
        if len(cluster) >=membership:
            return cluster
        else:
            return []
        
    