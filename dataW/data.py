


__author__ = 'dante0shy'
__version__ = '0.1'
__date__ = '19/08/2016'

#import numpy as np
import zipfile
import pandas as pd
import log

#open dataW which is in the csv file

class data :
    data=[]
    __dir = ''
    __zip_dir = ''
#__init__(self,dir,zip_dir = 'none')
# init the data structrue
#   self    :   self
#   dir     :   The direction of the file
#   zip_dir :   If it's a zip file ,the data file in the zip
    def __init__(self,dir,zip_dir = 'none'):
        self.__dir=dir
        self.__zip_dir=zip_dir
        if ('.csv' in dir):
            self.data = pd.read_csv(self.__dir)
        else:
            if(('.zip'in self.__dir)and('.csv'in self.__zip_dir)):
                self.data =  pd.read_csv(zipfile.ZipFile(self.__dir).open(self.__zip_dir))
            else:
                log.LogMessage('no file')
   # def getData(self):
#print(pd.read_csv('./input/Chapter03DataSet.csv'))
#data_1 =dataW('./input/game-of-thrones.zip','battles.csv')
#print(data_1.dataW)