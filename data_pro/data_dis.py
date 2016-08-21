

from dataW import data
import numpy as np
import scipy as sp
import pandas as pd
import sys
import log

class proprocess :

    #__data=pd.DataFrame()

    #def __init__(self,data):
      #  self.__data=data


    def normalization(data,col,way = 0 ,flag1 = 0,flag2 = 1):
        #print(data)
        if(way == 0):
            Vmax = data.loc[0,col]
            Vmin = data.loc[0,col]
            print(Vmax)
            j = 0
            while(j<len(data[col])):
                if(pd.isnull(data.loc[j,col])):
                    if(data.loc[j,col]<Vmin):
                        Vmin=data.loc[j,col]
                    if(data.loc[j,col]>Vmax):
                        Vmax=data.loc[j,col]
            if(flag1<flag2):
                i = 0
                while(data.loc[j,col]):
                    if(pd.isnull(data.loc[j,col])):
                        data.loc[j, col] = ((data.loc[j,col]-Vmin)/(Vmax-Vmin))*(flag2-flag1)+flag1
                        i=i+1
            else:
                log("wrong range!")
                sys.exit(0)
        elif(way == 1):
            Vmean = data[col].ix(0)
            j = 0



    #deal with the missing dataW
    #def data_missing_replce(self,way = 'default',word = 0 ,col = 'all' ):
    #    if(way.lower().find('default')):
     #       return 0


data_1 = data.data('../input/game-of-thrones.zip','battles.csv')
#print(data_1.data['attacker_size'])
#print(data_1.data)
print(proprocess.normalization(data = data_1.data,col = 'attacker_size'))

