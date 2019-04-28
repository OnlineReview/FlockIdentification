
from GridFormation.Point import Point
import glob
from math import sqrt, sin, radians, nan, isnan, isclose
from _collections import OrderedDict

class FlockFile(object):
    '''
    classdocs
    '''


    def __init__(self,clusterflocks):
        '''
        Constructor
        '''
        self.instant=0
        self.flocks=clusterflocks
        OrderedDict(sorted(self.flocks.items(), key=lambda t: t[0]))
        self.identified={}
        self.radius=0.0
    def getCenter(self,flock):
        p1=flock[0]
        p2=flock[1]
        p3=flock[2]
        center1=Point(0,0)
        center2=Point(0,0)
        print("for points center calculation  ")
        print(str(p1.x)+" "+str(p1.y))
        print(str(p2.x)+" "+str(p2.y))
        print(str(p3.x)+" "+str(p3.y))

        
        q=sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
        midp=Point((p1.x+p2.x)/2,(p1.y+p2.y)/2)
        center1.x = midp.x + sqrt(self.radius**2-(q/2)**2)*(p1.y-p2.y)/q
        center1.y = midp.y + sqrt(self.radius**2-(q/2)**2)*(p2.x-p1.x)/q  
        center2.x = midp.x - sqrt(self.radius**2-(q/2)**2)*(p1.y-p2.y)/q
        center2.y = midp.y - sqrt(self.radius**2-(q/2)**2)*(p2.x-p1.x)/q
        if isclose(p3.getDist(center1),self.radius):
            print("centre is 1 "+str(center1.x)+" "+str(center1.y))
            return center1
        else:
            print("centre is 2 "+str(center2.x)+" "+str(center2.y))
            return center2
        
    
    def checkvalidflocks(self, pipesize, membership, radius, start):
        end=pipesize-1-start
        flocksidentified=[]
        keylist=list(self.flocks.keys())
        for keys in self.flocks[keylist[start]].keys():
            for keye in self.flocks[keylist[end]].keys():
                k=keys & keye
                setBits=[ones for ones in bin(k)[2:] if ones=='1']
                if len(setBits) >= membership:
                    flocksidentified.append(k) 
        if len(flocksidentified) ==0:
            return flocksidentified
        else:
            return self.getflocks(pipesize, membership, radius, start)  
       
    def getflocks(self,pipesize,membership,radius,start):        
        end=pipesize-1-start
        keylist=list(self.flocks.keys())
        if end-start==0:
            return self.flocks[keylist[end]].keys()
        flocksidentified=[]
        if end-start==1:
            for keys in self.flocks[keylist[start]].keys():
                for keye in self.flocks[keylist[end]].keys():
                    k=keys & keye
                    setBits=[ones for ones in bin(k)[2:] if ones=='1']
                    if len(setBits) >= membership:
                        flocksidentified.append(k)
            return flocksidentified
        flocksideninner=self.getflocks(pipesize, membership, radius, start+1)
        for keys in self.flocks[keylist[start]].keys():
            for keye in self.flocks[keylist[end]].keys():
                k=keys & keye
                setBits=[ones for ones in bin(k)[2:] if ones=='1']
                if len(setBits) >= membership:
                    flocksidentified.append(k) 
        flockscurr=[]
        for internal in flocksideninner: 
            for curr in flocksidentified:
                k=internal & curr
                setBits=[ones for ones in bin(k)[2:] if ones=='1']
                if len(setBits) >= membership:
                    if start !=0:
                        flockscurr.append(k)
                    else:
                        flockscurr.append(bin(k))
        return flockscurr
    
    def getflocks1(self,pipesize,membership,radius,start):   
        end=pipesize-1-start
        keylist=list(self.flocks.keys())
        if end-start==0:
            return self.flocks[keylist[end]].keys()
        flocksidentified=[]
        if end-start==1:
            keylist1=self.flocks[keylist[start]].keys()
            keylist2=self.flocks[keylist[end]].keys()
            for keys in keylist1:
                for keye in keylist2:
                    k=keys & keye
                    setBits=[ones for ones in bin(k)[2:] if ones=='1']
                    if len(setBits) >= membership and k not in flocksidentified:
                        flocksidentified.append(k)
            return flocksidentified
        keylist2=self.flocks[keylist[end]].keys()
        keylist1=self.flocks[keylist[start]].keys()
        for keys in keylist1:
            for keye in keylist2:
                k=keys & keye
                setBits=[ones for ones in bin(k)[2:] if ones=='1']
                if len(setBits) >= membership and k not in flocksidentified:
                    flocksidentified.append(k)
        if len(flocksidentified)==0:
            return flocksidentified
        flocksideninner=self.getflocks(pipesize, membership, radius, start+1)
        if len(flocksideninner)==0:
            return flocksideninner 
        flockscurr=[]
        for internal in flocksideninner: 
            for curr in flocksidentified:
                k=internal & curr
                setBits=[ones for ones in bin(k)[2:] if ones=='1']
                if len(setBits) >= membership :
                    if start !=0 :
                        if k not in flockscurr:
                            flockscurr.append(k)
                    else:
                        if bin(k) not in flockscurr:
                            flockscurr.append(bin(k))
        return flockscurr
