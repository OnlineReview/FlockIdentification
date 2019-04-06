
import glob;
import csv
import pandas as pd
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
       
    def readCSVTakeSS(self,num):
        df=pd.read_csv(self.csvpath,low_memory=False, index_col=None, header = None)          
        ddf=pd.DataFrame()     
        for index,rows in df.iterrows():           
            if(rows[1]==num):
                ddf=ddf.append(rows)
       
        return ddf