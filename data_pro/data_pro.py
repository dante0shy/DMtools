

#from dataW import data
#import numpy as np
#import scipy as sp
import pandas as pd
import sys
import log

class proprocess :
# normalization(data,col,way = 0 ,flag1 = 0,flag2 = 1)
#   data    :   data need to be done ,which is assumed as float64
#   clo     :   the column which need to be normalization
#   way     :   the way to deal the data
#                   1 means min-max normalization
#                   2 means standardlization normalization
#                   3 means decimal decimal scaliy normalization
#   falg1 ,flag2:   the min and max range when way = 0
    def normalization(data,col,way = 0 ,flag1 = 0,flag2 = 1):
        #print(data)
        if(way == 0):
            Vmax = data.loc[:, col].max()
            Vmin = data.loc[:, col].min()
            if(flag1<flag2):
                i = 0
                while(i < len(data.loc[:,col])):
                    if(not pd.isnull(data.loc[i,col])):
                        data.loc[i, col] = ((data.loc[i,col]-Vmin)/(Vmax-Vmin))*(flag2-flag1)+flag1
                    i=i+1
                return  data
            else:
                log("wrong range!")
                sys.exit(0)
        elif(way == 1):
            std = data.loc[:, col].std()
            i = 0
            while (i < len(data.loc[:,col])):
                if (not pd.isnull(data.loc[i, col])):
                    data.loc[i, col] = (data.loc[i, col] - data.loc[:, col].mean()) / std
                i = i + 1
            return data
        elif(way == 2):
            j10 = 10
            while(j10<=data.loc[:, col].max()):
                j10=j10 * 10
            i = 0
            while (i < len(data.loc[:,col])):
                if (not pd.isnull(data.loc[i, col])):
                    data.loc[i, col] = data.loc[i, col] /j10
                i = i + 1
            return data








#data_1 = data.data('../input/game-of-thrones.zip','battles.csv')
#print(data_1.data['attacker_size'])
#print(data_1.data)
#print(proprocess.normalization(data = data_1.data,col = 'attacker_size').loc[:,'attacker_size'])
#print(proprocess.normalization(data = data_1.data,col = 'attacker_size',way=1).loc[:,'attacker_size'])
#print(proprocess.normalization(data = data_1.data,col = 'attacker_size',way=2).loc[:,'attacker_size'])