from dataW import data
import numpy as np
import scipy as sp
import pandas as pd
import sys
import log
import math

class distance:
    def Minkowski(data , r =2,index=[0,0],col =['@start','@end']):
        dist = 0.0
        i=0
        j=0
        if ((col[0]== '@start')):
            col=[data.columns[0],data.columns[len(data.columns)-1]]
        else:
            while(j<len(data.columns)):
                if(col[0] == data.columns[j] ):
                    break
                j=j+1

        while(i<len(col)):
            if(i+1<len(col)):
                while(col[i+1] != data.columns[j]):
                    dist =dist +math.pow (abs(float(data.ix[index[0],j]) - float(data.ix[index[1],j])) ,r)
                    j = j+1
                dist = dist + math.pow(abs(float(data.ix[index[0], j]) - float(data.ix[index[1], j])),r)
                i=i+2
            else:
                dist =dist + math.pow(abs(float(data.ix[index[0],j])-float(data.ix[index[1],j])),r)
                i = i+1
        dist = math.pow(dist,(1/r))
        return dist

data_1 = data.data('../input/BNPcsv.zip','train.csv')

print(distance.Minkowski(data = data_1.data,index=[0,1],col = ['v1','v2']))

#print(data_1.data.columns[0])