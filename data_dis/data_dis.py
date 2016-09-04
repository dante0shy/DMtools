
__author__ = 'dante0shy'
__version__ = '0.2'
__date__ = '24/08/2016'



from dataW import data
import numpy as np
import scipy as sp
import pandas as pd
import sys
import log
import math


#class distance:


#Minkowski(data , r =2,index=[0,0],col =['@start','@end'])
# calculate the Minkowski Distance for two row in particular some columns
#   data    :   the data need to be processed
#   r       :   the r in Minkowski
#   index   :   two data need to compare
#   col     :   the columns which particpate in the calculate
#               the columns need to be in pair
#               Exampl: col = [('v1','v5')] means column v1-v5
#                       col = ['v1'] means column v1
#                       col = [('v1','v3'),('v5','v7')] means column v1-v3 ,v5-v7
#   retuen  :   the distance of this two point
def Minkowski(data , r =2,index=[0,0],col =[('@start','@end')]):
        dist = 0.0
        i=0
        j=0
        if ((col[0]== tuple(('@start',"@end")))):
            col=[(data.columns[0],data.columns[len(data.columns)-1])]
        else:
            while(j<len(data.columns)):
                if(isinstance(col[0],tuple)):
                    if(col[0][0] == data.columns[j] ):
                        break
                else:
                    if (col[0] == data.columns[j]):
                        break
                j=j+1


        while(i<len(col)):
            while (j < len(data.columns)):
                if (isinstance(col[i],tuple)):
                    if (col[i][0] == data.columns[j]):
                        break
                else:
                    if (col[i] == data.columns[j]):
                        break
                j = j + 1
            if(isinstance(col[i],tuple)):
                while(col[i][1] != data.columns[j]):
                    if(pd.isnull(data.ix[index[0],j]) or pd.isnull(data.ix[index[1],j])  ):
                        log.LogMessage("null number!")
                        sys.exit(0)
                    dist =dist +math.pow (abs(float(data.ix[index[0],j]) - float(data.ix[index[1],j])) ,r)
                    j = j+1
                if (pd.isnull(data.ix[index[0], j]) or pd.isnull(data.ix[index[1], j])):
                    log.LogMessage("null number!")
                    sys.exit(0)
                dist = dist + math.pow(abs(float(data.ix[index[0], j]) - float(data.ix[index[1], j])),r)
                j=j+1
            else:
                if (pd.isnull(data.ix[index[0], j]) or pd.isnull(data.ix[index[1], j])):
                    log.LogMessage("null number!")
                    sys.exit(0)
                dist =dist + math.pow(abs(float(data.ix[index[0],j])-float(data.ix[index[1],j])),r)
            i = i+1
        dist = math.pow(dist,(1/r))
        return dist


#test data


#data_1 = data.data('../input/BNPcsv.zip','train.csv')
#data_1.data=data_1.data.fillna(data_1.data.mean())
#print(data_1.data.ix[ :,'v1'])

#print(Minkowski(data = data_1.data,index=[0,1],col = [('v1','v2'),'v4']))

#print(Minkowski(data_1  = data_1.data.ix[0,:],data_2= data_1.data.ix[2,:],col = ['v1','v2']))

#print(data_1.data.columns[0])

