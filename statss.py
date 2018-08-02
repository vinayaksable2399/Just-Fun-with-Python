# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:40:19 2018

@author: vinayak sable

"""
from numpy import *
from math import *


__all__ = ['mode','median'
           ,'avg','var','cov','corr'
           ]

def mode(x):
        y=set(x)
        a=1
        m="given array no mode"
        for i in y:
            b=x.count(i)
            if(a<b):
                a=b
                m=i
        return(m)
def median(x):
        x=sorted(x)
        l=len(x)
        if(l%2!=0):
            return(x[int(l/2)])
        else:
            m=(x[int(l/2)]+x[int(l/2)-1])/2
            return(m)
def avg(x):
        s=0
        for i in x:
            s=s+i
        return(s/len(x))
def var(x):
       y=list(map(lambda x: x**2,x))
       a=avg(y)-avg(x)**2
       return(a)

def cov(x,y):
       z=list(map(lambda x,y:x*y,x,y))
       a=avg(z)-avg(x)*avg(y)
       return(a)

def corr(x,y):       
       assert len(x)==len(y),"two array length are differnt"
       a=cov(x,y)/sqrt(var(x)*var(y))
       return(a)

