from SnapshotDB.Snapshots import Snapshots
from GridFormation import GridConstructionPointAllocation
from FlockFormation.FlockCreate import FlockCreate
from GridFormation.Point import Point
from operator import attrgetter
from Plotting.PlotPoints import PlotPoints



#################################
import pandas as pd
from math import sqrt, isclose
from Pipelining.FlockFile import FlockFile
import time


x=Snapshots('txt files','output.csv')
clusterflocks={}
identified={}
pipesize=13
flockfile=FlockFile(clusterflocks)
allpointsallsnapshot={}
timeinstant=0
inittime=time.time()
for ptr in range(15):
    
    timeinstant=30*ptr
    df=x.readCSVTakeSS(timeinstant)
    if len(df)==0:
        continue
    starttime=time.time()
    Triangledict={}
    e=1
    drawhex=PlotPoints(timeinstant)
    starttime=time.time()
    y=GridConstructionPointAllocation.GridConstructionPointAllocation(df,e)
    Triangledict=y.makedict()
    starttime=time.time()
    PointList=y.constructPointMap(Triangledict) 
    PointMap=PointList     
    PointList=sorted(PointList,key=attrgetter('x','y'))
    
    membership=5
    radius=e/2
    starttime=time.time()
    f=FlockCreate(radius)
    flocklist=[]
    for pt in PointList:
        point=pt
        rightSemiCircle=y.getNeighbourhood(point, Triangledict)
        if point not in rightSemiCircle:
            rightSemiCircle.append(point)
        count=len(rightSemiCircle)
        
        if count < membership:
            continue
        for i in range(count-1):
            for j in range(i+1,count):
                pt1=rightSemiCircle[i]
                pt2=rightSemiCircle[j]
                f.findCentres(pt1,pt2)
                searcharea=[]
                
                for p in rightSemiCircle:
                    if isclose(p.getDist(Point(f.h1,f.k1)),radius,rel_tol=1e-14) or p.getDist(Point(f.h1,f.k1))<=radius :
                        searcharea.append(p)
                flock1=f.findFlocks(1, searcharea, membership)
                flock1=sorted(flock1,key=attrgetter('x','y'))
                
                    
                if len(flock1)>0 and flock1 not in flocklist:
                    flocklist.append(flock1)
                searcharea=[]
                for p in rightSemiCircle:
                    if isclose(p.getDist(Point(f.h2,f.k2)),radius,rel_tol=1e-14) or p.getDist(Point(f.h2,f.k2)) <= radius:
                        searcharea.append(p)
                flock2=f.findFlocks(2, searcharea, membership)
                flock2=sorted(flock2,key=attrgetter('x','y'))
                
                if len(flock2)>0 and flock2 not in flocklist:
                    flocklist.append(flock2)
           
    starttime=time.time()    
    flockdict={}
    for flocks in flocklist:
        c=0
        for pts in flocks:
            a=2**(pts.id-1)
            c=c|a
        flockdict[c]=flocks
        keylist=list(flockdict.keys())
        if len(flockdict)==0:
            flockdict[c]=flocks
            removed=False
            flag=False
        for key in keylist:
            if key ==c:
                continue
            ans =key &c
            if ans==key:
                del flockdict[key]
            if ans==c:
                del flockdict[c]
                break
        
    clusterflocks[timeinstant/30]=flockdict  
    
    
    if len(clusterflocks)==pipesize:        
        binflockslist=flockfile.getflocks(pipesize, membership, radius,0)# list of all flocks in form of binary string
        
        orlist=0
        for bins in binflockslist:            
            orlist=orlist | int(bins,2)
        identified[ptr]=orlist 
        allpointsallsnapshot[((timeinstant/30)-pipesize+1)*30]=y.getpointsInFlocks(clusterflocks[(timeinstant/30)-pipesize+1], identified,((timeinstant/30)-pipesize+1),pipesize)
        del clusterflocks[(timeinstant/30)-pipesize+1]
        
    
    starttime=time.time() 
ptr=int(timeinstant/30)
for remaining in range(pipesize-1):
    allpointsallsnapshot[timeinstant]=y.getpointsInFlocks(clusterflocks[int(timeinstant/30)], identified,ptr , pipesize)
    timeinstant=timeinstant-30
#plotting hexagonal grid#####################
# drawhex=PlotPoints()
# drawhex.drawHexGrid(Triangledict)
#############################################
# drawhex.plotpipes(allpointsallsnapshot)
