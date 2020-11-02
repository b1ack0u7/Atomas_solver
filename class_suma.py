# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:55:13 2020

@author: axelm
"""

def suma_sub(data,i):
    try:
        if (data[i-1] == data[i+1]):
            data[i-1]=data[i]+1
            data.pop(i)
            data.pop(i)
                
    except:
        if (data[i-1] == data[0]):
            data[i-1]=data[i]+1
            data.pop(i)
            data.pop(0)

    return data

def suma_core(data):
    executed=False
    msc=data.copy()
    for i in range(0,len(data)):
        if (data[i] == "+"):
            if (i != len(data)-1):
                if (data[i-1] == data[i+1]):
                    msc[i-1]=data[i-1]+1
                    msc.pop(i)
                    msc.pop(i)
                    
                    ii=i-1
                    executed=True

            else:
                if (data[i-1] == data[0]):
                    msc[i-1]=data[i-1]+1
                    msc.pop(i)
                    msc.pop(0)
                    
                    ii=i-2
                    executed=True
            
    if (executed == True):
        result=suma_sub(msc,ii)
        return result
    else:
        return msc