


__author__ = 'dante0shy'
__version__ = '0.1'
__date__ = '19/08/2016'

#import numpy as np
import zipfile
import pandas as pd
import log

#open data which is in the csv file

class data :
    data=[]
    __dir = ''
    __zip_dir = ''
    def __init__(self,dir,zip_dir = 'none'):
        __dir=dir
        __zip_dir=zip_dir
        if ('.csv' in dir):
            self.data = pd.read_csv(__dir)
        else:
            if(('.zip'in __dir)and('.csv'in __zip_dir)):
                self.data =  pd.read_csv(zipfile.ZipFile(__dir).open(__zip_dir))
            else:
                log.LogMessage('no file')
   # def getData(self):
#print(pd.read_csv('./input/Chapter03DataSet.csv'))
#data_1 =data('./input/game-of-thrones.zip','battles.csv')
#print(data_1.data)