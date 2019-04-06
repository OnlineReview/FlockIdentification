from math import sqrt, degrees,atan

class Point(object):
    '''
    classdocs
    '''
    

    def __init__(self, x,y):
        '''
        Constructor
        '''
        self.id=0
        self.x=x+0.0
        self.y=y+0.0
        self.isOnVertex=False
    
    def getAngle(self,vertex):
        angle= degrees(atan((vertex.y-self.y)/(vertex.x-self.x)))
        return angle
    def getDist(self,vertex):
        return sqrt((self.x-vertex.x)**2+(self.y-vertex.y)**2)
        
    def __hash__(self):
        stmt=str(self.x)+" "+str(self.y)

        return hash(stmt)
        
    def __eq__(self, other):
        cond = self.x==other.x and self.y==other.y
        return cond           