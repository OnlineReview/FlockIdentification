
from mpl_toolkits import mplot3d
#@UnresolvedImport

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D   
import itertools
from matplotlib import colors as mcolors
class PlotPoints(object):
    '''
    classdocs
    '''
    def __init__(self,timeinstant):
        '''
        Constructor
        '''
        self.fig=plt.figure()
        self.ax = plt.axes(None)
        self.timeinstant=timeinstant
        
    def drawHexGrid(self,dict):
        keylist=dict.keys()
        
        for triangle in keylist:
            x=[]
            y=[]
            if triangle.isbottomUp:
                x.append(triangle.uponex)
                y.append(triangle.uponey)
                x.append(triangle.uptwox)
                y.append(triangle.uptwoy)
                x.append(triangle.downonex)
                y.append(triangle.downoney)
                x.append(triangle.uponex)
                y.append(triangle.uponey)
            else:
                x.append(triangle.uponex)
                y.append(triangle.uponey)
                x.append(triangle.downonex)
                y.append(triangle.downoney)
                x.append(triangle.downtwox)
                y.append(triangle.downtwoy)
                x.append(triangle.uponex)
                y.append(triangle.uponey)
            line=Line2D(x,y)
            plt.plot(x,y,'black')
            self.plotpts(dict[triangle])
        plt.ioff()
#         plt.show()
        self.fig.savefig(str(self.timeinstant)+".png")
        plt.clf()
        
    def plotpts(self,list):
        for pt in list:
            self.ax.scatter(pt.x,pt.y)
    def flocklistplot(self, list):
        clr=-287.76961648886305
        colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        colr=iter(colors.keys())
        for flock in list:
            x=[]
            y=[]
            for pt in flock:
                x.append(pt.x)
                y.append(pt.y)
            try:
                plt.scatter(x,y,color=next(colr))
            except:
                colr=iter(colors.keys())
                plt.scatter(x,y,color=next(colr))
        plt.ioff()
#         plt.show()
        self.fig.savefig(str(self.timeinstant)+"f.png")
        plt.clf()
    def plotpipes(self,dict):
        ax = plt.axes(projection='3d')

        for key, ptrlist in dict.items():
            for pt in ptrlist:
                    ax.scatter(pt.x,pt.y,key)

 
        plt.ioff()
        #plt.show()
        self.fig.savefig("finalclusterhex.png")   
        plt.clf()