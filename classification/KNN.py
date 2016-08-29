__author__ = 'dante0shy'
__version__ = '0.1'
__date__ = '25/08/2016'

from dataW import data
from data_dis import data_dis
from data_pro import data_pro
import numpy as np
import scipy as sp
import pandas as pd
import sys
import log
import math
from operator import itemgetter

def KNN(data,data_set,goal_col ,K=2):
    i=0
    data_NN=[]
    #print(data_NN[0][0])
    data.ix[ :,goal_col]= 0
    #print(data)
    data_all=pd.concat([data_set, data], axis=0,keys=['a','b'])
    #print(data_all.ix[10,:])
    while(i<len(data_all.ix['a'])):
        dist=data_dis.Minkowski(data_all,index=[i,len(data_all.ix['a'])],col=[])
        #print(dist)
        data_NN.append(tuple((i,dist)))
        data_NN=sorted(data_NN,key =itemgetter(1))
        #if(len(data_NN)<K):
         #   data_NN.append(tuple((i,dist)))
         #   sorted(data_NN,key = lambda data: data[1])
        #else:
        if(len(data_NN)>K):
            del data_NN[len(data_NN)-1]
        i=i+1



df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.ix[0,'d']=1

df1=pd.DataFrame({'a':[1],'b':[2],'c':[3]})




print(KNN(df1,df,'d'))


#print([ i for i in df.ix[0,:]])
#print(pd.Series([pd.NaT],index=['d']))
#df1.append()

#print(df)
#df1.ix[:,'d']=0
#print(df1)
#print(pd.concat([df,df1],axis=0))