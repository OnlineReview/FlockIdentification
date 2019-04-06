
from math import floor, atan,degrees,sqrt,ceil



class Triangle(object):
    '''
    classdocs
    '''
    

    def __init__(self, radius):
        '''
        Constructor
        '''
        self.uponex=0.0
        self.uponey=0.0
        
        self.uptwox=0.0
        self.uptwoy=0.0
        
        self.downonex=0.0
        self.downoney=0.0
        
        self.downtwox=0.0
        self.downtwoy=0.0
        
        self.side=radius
        self.angleone=0.0
        self.angletwo=0.0
        self.anglethree=0.0
        self.x=0.0
        self.y=0.0
        self.isbottomUp=False
        
    def __hash__(self):
        stmt=str(format(float(format(self.uponex,'.15f')),'.7f'))+" "+str(format(float(format(self.uponey,'.15f')),'.7f'))+" "+str(format(float(format(self.uptwox,'.15f')),'.7f'))+" "+str(format(float(format(self.uptwoy,'.15f')),'.7f'))+" "+str(format(float(format(self.downonex,'.15f')),'.7f'))+" "+str(format(float(format(self.downoney,'.15f')),'.7f'))+" "+str(format(float(format(self.downtwox,'.15f')),'.7f'))+" "+str(format(float(format(self.downtwoy,'.15f')),'.7f'))+" "
        return hash(stmt)
        
    def __eq__(self, other):
        cond=str(format(float(format(other.uponex,'.15f')),'.7f'))==str(format(float(format(self.uponex,'.15f')),'.7f')) and str(format(float(format(other.uponey,'.15f')),'.7f'))==str(format(float(format(self.uponey,'.15f')),'.7f')) and str(format(float(format(other.uptwox,'.15f')),'.7f'))==str(format(float(format(self.uptwox,'.15f')),'.7f'))and str(format(float(format(other.uptwoy,'.15f')),'.7f'))== str(format(float(format(self.uptwoy,'.15f')),'.7f'))and str(format(float(format(other.downonex,'.15f')),'.7f'))==str(format(float(format(self.downonex,'.15f')),'.7f'))and str(format(float(format(other.downoney,'.15f')),'.7f'))== str(format(float(format(self.downoney,'.15f')),'.7f'))and str(format(float(format(other.downtwox,'.15f')),'.7f'))==str(format(float(format(self.downtwox,'.15f')),'.7f'))and str(format(float(format(other.downtwoy,'.15f')),'.7f'))==str(format(float(format(self.downtwoy,'.15f')),'.7f'))  
        return cond               
    
    def giveTriangleFromPoint(self,point):
        self.x=point.x+0.0
        self.y=point.y+0.0
        height=self.side*sqrt(3)/2
        row=floor(point.y/height)
        if row %2==0:
            x1=self.side*(ceil(point.x/self.side)-1)        
            y1=row*self.side*sqrt(3)/2
            x2=x1+self.side
            y2=y1
            
            
            anglea=degrees(atan((y1-point.y)/(x1-point.x))) 
            try:
                angleb=180+degrees(atan((y2-point.y)/(x2-point.x)))
            except:
                angleb=90
                pass
            
            if anglea <=60 and angleb>=120:
                self.uponey=(row+1)*height
                self.uponex=x1+(self.side)/2
                self.downonex=x2
                self.downoney=y2
                self.downtwox=x1
                self.downtwoy=y1
            
                self.isbottomUp=False
            else:
                if anglea>=60 and angleb>120:
                    self.uptwox=x1+self.side/2
                    self.uptwoy=(row+1)*height
                    self.uponex=self.uptwox-self.side
                    self.uponey=self.uptwoy
                    self.downonex=x1
                    self.downoney=y1
                    self.isbottomUp=True
                
                else:
                    self.uponey=(row+1)*height
                    self.uponex=x1+self.side/2
                    self.uptwox=x2+self.side/2
                    self.uptwoy=self.uponey
                    self.downonex=x2
                    self.downoney=y2
                    self.isbottomUp=True
                
        else:
            x1=0.0
            y1=0.0
            x2=0.0
            y2=0.0
            if abs(point.x)<self.side/2:
                x1=-1*self.side/2
                x2=self.side/2
                y1=row*height
                y2=y1
            else:
                x1=floor(point.x/self.side)*self.side-self.side/2
                if point.x-x1>self.side:
                    x1=x1+self.side
                x2=x1+self.side
                
                y1=row*height
                y2=y1
                
            
            anglea=degrees(atan((y1-point.y)/(x1-point.x)))
            try:
                angleb=180+degrees(atan((y2-point.y)/(x2-point.x)))
            except:
                angleb=90
                pass
            if anglea<=60 and angleb>=120:
               
                self.uponex=x1+self.side/2
                self.uponey=(row+1)*height
                self.downonex=x2
                self.downoney=y2
                self.downtwox=x1
                self.downtwoy=y1
                
                self.isbottomUp=False
                
            else:
                if anglea>=60 and angleb>=120:
                    self.uponex=x1-self.side/2
                    self.uponey=(row+1)*height
                    self.uptwox=self.uponex+self.side
                    self.uptwoy=self.uponey
                    self.downonex=x1
                    self.downoney=y1
                    self.isbottomUp=True
                
                else:
                    self.uponex=x1+self.side/2
                    self.uponey=(row+1)*height
                    self.uptwox=self.uponex+self.side
                    self.uptwoy=self.uponey
                    self.downonex=x2
                    self.downoney=y2
                    self.isbottomUp=True
        self.uponex=0.0+self.uponex
        self.uponey=0.0+self.uponey
        self.uptwox=0.0+self.uptwox
        self.uptwoy=0.0+self.uptwoy
        self.downonex=0.0+self.downonex
        self.downoney=0.0+self.downoney
        self.downtwox=0.0+self.downtwox
        self.downtwoy=0.0+self.downtwoy
        return self           
        
    