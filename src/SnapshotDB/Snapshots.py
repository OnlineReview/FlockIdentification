
import glob;
import csv
import pandas as pd
import numpy as np
class Snapshots(object):
    '''
    classdocs
    '''
    folderpath=''
    csvpath=''
    def __init__(self, params,csvpath):
        '''
        Constructor
        '''
        self.folderpath=params
        self.csvpath=csvpath
        
    def readFiles(self):
        files=glob.glob(self.folderpath)
        count=0
        for file in files:
            count=count+1
            fileread=open(file, 'r')
            f=fileread.readlines()
            fileread.close()
            write_file = self.csvpath
            with open(write_file, "a") as output:                
                for line in f:
                    lst=line.split()
                    output.write(str(count)+","+lst[0]+","+lst[1]+","+lst[2]+'\n' )
       
    def readCSVTakeSS(self):
        df=pd.read_csv(self.csvpath,low_memory=False, index_col=None, header = None)          
        df=df.values.tolist()            
        ddf={}    
        for rows in df:  
            time=rows[1]
            if time not in ddf:
                ddf[time]=  np.array([rows])
            else:
                ddf[time]=np.concatenate((ddf[time],[rows]),axis=0)

        return ddf
