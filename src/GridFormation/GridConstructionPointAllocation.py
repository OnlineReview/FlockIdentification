import pandas as pd
from GridFormation import Point
from GridFormation import Triangle
from math import sqrt,floor
class GridConstructionPointAllocation(object):
    '''
    classdocs
    '''

    datafrme=pd.DataFrame()  
    radius=0

    def __init__(self, datafrme,radius):
        '''
        Constructor
        '''
        self.pointid=0
        self.datafrme=datafrme
        self.radius=radius
     
    def getMaxPointId(self):
        return self.pointid   
    def makedict(self):
        Triangledict={}
        self.pointid=0
        for index,rows in self.datafrme.iterrows():
            
            point =Point.Point(rows[2],rows[3])
            point.id=int(rows[0])
            self.pointid=self.pointid+1
            trianG = Triangle.Triangle(self.radius)
            triangle=trianG.giveTriangleFromPoint(point)
            
            point.isOnVertex=False
            if point.x==triangle.uponex and point.y ==triangle.uponey:
                point.isOnVertex=True
            if point.x==triangle.uptwox and point.y==triangle.uptwoy:
                point.isOnVertex=True
            if point.x==triangle.downonex and point.y==triangle.downoney:
                point.isOnVertex=True
            if point.x==triangle.downtwox and point.y==triangle.downtwoy:
                point.isOnVertex=True
            
            if triangle in Triangledict:
                Triangledict[triangle].append(point)
            else:
                Triangledict[triangle]=[]
                Triangledict[triangle].append(point)
        return Triangledict
    
    def getPointList(self,Triangledict):
        return Triangledict.keys()
    
    def constructPointMap(self,Triangledict):
        PointMap={}
        
        for triangle in Triangledict:
            for point in Triangledict[triangle]:
                PointMap[point]= triangle
                
        return PointMap 
    def getNeighbourhood(self,point,Triangledict):
        hexa =[] 
        hexapoints=[]  
        pt=Point.Point(point.x,point.y)
        
        if point.isOnVertex:
            hexa=self.prepareHalfHexagon(point,Triangledict)            
            for triangle in hexa:
                for hpoints in triangle:
                    if hpoints.x>=pt.x:
                        hexapoints.append(hpoints)
        
    
            TrianglesOrPoints=True
            triangles=self.prepareHalfHexagon(pt, Triangledict, TrianglesOrPoints)
            TrianglesOrPoints=False
            extras=self.getExtras(triangles,Triangledict,TrianglesOrPoints)
            self.getExtraPoints(extras,hexapoints,pt)
            return hexapoints            
        else:
            triangle=Triangle.Triangle(self.radius)
            PointMap=self.constructPointMap(Triangledict)
            triangle=PointMap[point]
            
            TrianglesOrPoints=True 
            height=self.radius * sqrt(3)/2
            row=floor(point.y/height)
            if triangle.isbottomUp:
                if height+(point.y-row*height) <=self.radius:    
                            
                    pt= Point.Point(triangle.downonex,triangle.downoney)
                else:          
                      
                    pt=Point.Point(triangle.uponex,triangle.uponey)
#                     
            else:
                if point.x <triangle.downtwox+(self.radius/2):
                    
                    pt=Point.Point(triangle.downtwox,triangle.downtwoy)
                else:
                    if 2*height-(point.y-(row*height))>=self.radius:                        
#                         
                        pt=Point.Point(triangle.downtwox,triangle.downtwoy)
                    else:                        
                        pt=Point.Point(triangle.uponex,triangle.uponey)
            
            triangles=self.prepareHalfHexagon(pt, Triangledict,TrianglesOrPoints) 
            extras=self.getExtras(triangles, Triangledict,TrianglesOrPoints)
            extras=self.getallTriangles(extras)
                       
            triangles=triangles+extras
            
            for triangle in triangles:
                try:
                    triangle=Triangledict[triangle]
               
                    for pts in reversed(triangle): 
                        if pts.x>=point.x:
                            if point.getDist(pts) <=self.radius:
                                hexapoints.append(pts)
#           
                except:
                    pass            
        return hexapoints       
        
    def getallTriangles(self,extras):    
        one=extras[0]
        four=extras[1]
        seven=extras[2]
        ten=extras[3]
        two=Triangle.Triangle(self.radius)
        two.isbottomUp=True
        two.uponex=one.uponex
        two.uponey=one.uponey
        two.downonex=one.downonex
        two.downoney=one.downoney
        two.uptwox=two.uponex+self.radius
        two.uptwoy=two.uponey
        
        three=Triangle.Triangle(self.radius)
        three.isbottomUp=False
        three.uponex=two.uptwox
        three.uponey=two.uptwoy
        three.downtwox=one.downonex
        three.downtwoy=one.downoney
        three.downonex=three.downtwox+self.radius
        three.downoney=three.downtwoy
        
        five=Triangle.Triangle(self.radius)
        five.isbottomUp=False
        five.uponex=three.downonex
        five.uponey=three.downoney
        five.downtwox=four.downonex
        five.downtwoy=four.downoney
        five.downonex=five.downtwox+self.radius
        five.downoney=five.downtwoy
        
        six=Triangle.Triangle(self.radius)
        six.isbottomUp=True
        six.uponex=seven.uponex
        six.uponey=seven.uponey
        six.downonex=seven.downonex
        six.downoney=seven.downoney
        six.uptwox=six.uponex+self.radius
        six.uptwoy=six.uponey
        
        eight=Triangle.Triangle(self.radius)
        eight.isbottomUp=True
        eight.uponex=seven.downtwox
        eight.uponey=seven.downtwoy
        eight.downonex=ten.downonex+self.radius
        eight.downoney=ten.downoney
        eight.uptwox=eight.uponex+self.radius
        eight.uptwoy=eight.uponey
        
        nine=Triangle.Triangle(self.radius)
        nine.isbottomUp=False
        nine.uponex=eight.uponex
        nine.uponey=eight.uponey
        nine.downtwox=ten.downonex
        nine.downtwoy=ten.downoney
        nine.downonex=nine.downtwox+self.radius
        nine.downoney=nine.downtwoy
        
        try:
            
            extras.append(two)
            
        except:
            extras.append([])
            pass
        try:
            
            extras.append(three)
            
        except:
            extras.append([])
            pass
        try:
            extras.append(five)
            
        except:
            extras.append([])
            pass
        try:
            extras.append(six)
            
        except:
            extras.append([])
            pass
        try:
            extras.append(eight)
            
        except:
            extras.append([])
            pass
        try:
            extras.append(nine)
            
        except:
            extras.append([])
            pass
        
                
        return extras
        
    def getExtraPoints(self,extras,hexapoints,point):
         
        upmid=extras[0]
        upright=extras[1]
        downright=extras[2]
        downmid=extras[3]
        if len(upmid)>0:
            for pt in reversed(upmid):
                if pt.x>=point.x:
                    vertex=Point(upmid.uptwox,upmid.uptwoy)
                    angle=180+pt.getAngle(vertex)
                    if angle >=150 and pt.getDist(point) <=self.radius:
                        hexapoints.add(pt)
                else :
                    break
        if len(downmid)>0:
            for pt in reversed(downmid):
                if pt.x >= point.x:
                    vertex=Point(downmid.uptwox,downmid.uptwoy)
                    angle=180-pt.getAngle(vertex)
                    if angle >=150 and pt.getDist(point) <=self.radius:
                        hexapoints.add(pt)
                else:
                    break
        if len(upright)>0:
            for pt in upright:
                if pt.x <= point.x+self.radius and pt.getDist(point) <=self.radius:
                    hexapoints.add(pt)
                else:
                    break
        if len(downright)>0:
            for pt in downright:
                if pt.x <=point.x+self.radius and pt.getDist(point) <= self.radius:
                    hexapoints.add(pt)
                else:
                    break
                
                
    def getExtras(self,triangles,Triangledict,TrianglesOrPoints):
        upmid = triangles[0]
        upright = triangles[1]
        downright = triangles[2]
        downmid = triangles[3]
        
        upMextra = Triangle.Triangle(self.radius)
        upMextra.downonex=upmid.uptwox
        upMextra.downoney=upmid.uptwoy
        upMextra.downtwox=upmid.uponex
        upMextra.downtwoy=upmid.uponey
        upMextra.uponex=upmid.uponex+self.radius/2
        upMextra.uponey=upmid.uponey+(self.radius*sqrt(3)/2)
        upMextra.isbottomUp=False
        
        upRextra = Triangle.Triangle(self.radius)
        upRextra.downonex=upright.downonex
        upRextra.downoney=upright.downoney
        upRextra.uptwox=upright.uponex+self.radius
        upRextra.uptwoy=upright.uponey
        upRextra.uponex=upright.uponex
        upRextra.uponey=upright.uponey
        upRextra.isbottomUp=True
        
        downRextra=Triangle.Triangle(self.radius)
        downRextra.uponex=downright.uptwox
        downRextra.uponey=downright.uptwoy
        downRextra.downtwox=downright.downonex
        downRextra.downtwoy=downright.downoney
        downRextra.downonex=downright.downonex+self.radius
        downRextra.downoney=downright.downoney
        downRextra.isbottomUp=False
        
        downMextra=Triangle.Triangle(self.radius)
        downMextra.uponex=downmid.downtwox
        downMextra.uponey=downmid.downtwoy
        downMextra.uptwox=downmid.downonex
        downMextra.uptwoy=downmid.downoney
        downMextra.downonex=downmid.downtwox+self.radius/2
        downMextra.downoney=downmid.downtwoy-(self.radius*sqrt(3)/2)
        
        extra=[]
        if TrianglesOrPoints:
            trianglestemp=[]
            trianglestemp.append(upMextra)
            trianglestemp.append(upRextra)
            trianglestemp.append(downRextra)
            trianglestemp.append(downMextra)
            return trianglestemp
        try:
            upMextra=Triangledict[upMextra]
            extra.append(upMextra)
        except:
            extra.append([])
            pass
        try:
            upRextra=Triangledict[upRextra]
            extra.append(upRextra)
        except:
            extra.append([])
            pass
        try:
            downRextra=Triangledict[downRextra]
            extra.append(downRextra)
        except:
            extra.append([])
            pass
        try:
            downMextra=Triangledict[downMextra]
            extra.append(downMextra)
        except:
            extra.append([])
            pass
        return extra
        
    def prepareHalfHexagon(self,point,Triangledict,TrianglesOrPoints):
      
        upleft=Triangle.Triangle(self.radius)
        upleft.uponex=point.x-self.radius/2
        upleft.uponey=point.y+(self.radius*sqrt(3)/2)
        upleft.downonex=point.x+0.0
        upleft.downoney=point.y+0.0
        upleft.downtwox=point.x-self.radius
        upleft.downtwoy=point.y+0.0
        upleft.isbottomUp=False
        
        upmid=Triangle.Triangle(self.radius)
        upmid.uponex=upleft.uponex
        upmid.uponey=upleft.uponey
        upmid.uptwox=upmid.uponex+self.radius
        upmid.uptwoy=upmid.uponey
        upmid.downonex=point.x+0.0
        upmid.downoney=point.y+0.0
        upmid.isbottomUp=True
        
        upright=Triangle.Triangle(self.radius)
        upright.uponex=upmid.uptwox
        upright.uponey=upmid.uptwoy
        upright.downonex=point.x+self.radius
        upright.downoney=point.y+0.0
        upright.downtwox=point.x+0.0
        upright.downtwoy=point.y+0.0
        upright.isbottomUp=False
        
        downleft=Triangle.Triangle(self.radius)
        downleft.uponex=upleft.downtwox
        downleft.uponey=upleft.downtwoy
        downleft.uptwox=upleft.downonex
        downleft.uptwoy=upleft.downoney
        downleft.downonex=point.x-self.radius/2
        downleft.downoney=point.y-(self.radius*sqrt(3)/2)
        downleft.isbottomUp=True
        
        downmid=Triangle.Triangle(self.radius)
        downmid.uponex=point.x+0.0
        downmid.uponey=point.y
        downmid.downonex=point.x+self.radius/2
        downmid.downoney=downleft.downoney
        downmid.downtwox=downleft.downonex
        downmid.downtwoy=downleft.downoney
        downmid.isbottomUp=False
        
        downright=Triangle.Triangle(self.radius)
        downright.uponex=point.x+0.0
        downright.uponey=point.y+0.0
        downright.uptwox=point.x+self.radius
        downright.uptwoy=point.y+0.0
        downright.downonex=downmid.downonex
        downright.downoney=downmid.downoney
        downright.isbottomUp=True
        triangles=[]
        if TrianglesOrPoints:
            triangles.append(upmid)
            triangles.append(upright)
            triangles.append(downright)
            triangles.append(downmid)
            return triangles
        hexa=[]
        try:
            upmid=Triangledict[upmid]
            hexa.append(upmid)  
        except:
            emptyl=[]
            hexa.append(emptyl)
            pass
        try:
            upright=Triangledict[upright]            
            hexa.append(upright)
        except:
            emptyl=[]
            hexa.append(emptyl)
            pass
        try:
            downright=Triangledict[downright]            
            hexa.append(downright)
        except:
            emptyl=[]
            hexa.append(emptyl)
            pass
        try:
            downmid=Triangledict[downmid]           
            hexa.append(downmid)
        except:
            emptyl=[]
            hexa.append(emptyl)
            pass
        
        
        return hexa
    
    def getpointsInFlocks(self,flockdict,identified,ptr,pipesize):
        pointslist=[]
        
        for keys ,lists in flockdict.items():
            for pts in lists:
                if pts not in pointslist:
                    pointslist.append(pts)
        num=0

        start=int(ptr) 
        end=int(ptr+pipesize) 
        for i in range(start,end):
            if i in identified:
                num=num | identified[i]
        lists=[]
        for pts in pointslist:

            if 2**(pts.id-1) & num ==2**(pts.id-1):
                lists.append(pts)
        return lists    
            
        