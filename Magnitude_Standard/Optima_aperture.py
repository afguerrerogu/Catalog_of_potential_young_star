#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:34:58 2021

@author: andres
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
sns.set()

Data=[]
for i in range(8,16):
    Data.append(pd.read_csv('magnitude_aper'+str(i)+'.data', sep=" ",names=['colum'+str(x) for x in range(0,17)]))

for i in range(0,8):
    for j in [1,3,5,7,9,11,13,15]:
        Data[i] = Data[i].drop('colum'+str(j), axis='columns')
        Data[i].rename(columns={'colum'+str(0):'XINIT','colum'+str(2):'YINIT','colum'+str(4):'IFILTER',
                        'colum'+str(6):'OTIME','colum'+str(8):'XAIRMASS','colum'+str(10):'XCENTER'
                        ,'colum'+str(12):'YCENTER','colum'+str(14):'MAG','colum'+str(16):'MERR'}, inplace=True)
        
suma = 8
for data in Data:
    #data = data.replace({'INDEF':1000})
    data['apertura'] = suma   
    suma += 1

def trans(datos):
    for data in range(8):
        datos[i] = Data[i].replace({'INDEF':1000})
    return datos

trans(Data)

for i in range(7):
    Data[i].replace({'INDEF':1000})
    prim = Data[i]['MAG'] 
    seg = Data[i+1]['MAG'] 

#datos_escogidos = [random.randint(0,1420) for i in range(0,1000)]
datos_escogidos = [1155,2]
df_grafica = pd.DataFrame()

df_grafica['magnitude'] =  [datos['MAG'][i] for datos in Data for i in datos_escogidos]
df_grafica['apertur'] =  [datos['apertura'][i] for datos in Data for i in datos_escogidos]
df_grafica['error_mag'] =  [datos['MERR'][i] for datos in Data for i in datos_escogidos]
df_grafica['filtro'] =  [datos['IFILTER'][i] for datos in Data for i in datos_escogidos]
df_grafica['number'] =  [datos.index[i] for datos in Data for i in datos_escogidos]

fig = plt.plot(figsize=(15,15))
plt.scatter( df_grafica['apertur'], df_grafica['magnitude'],label=df_grafica['number'])
plt.legend()

# datos_escogidos = [128]
# df_grafica = pd.DataFrame()

# df_grafica['magnitude'] =  [datos['MAG'][i] for datos in Data for i in datos_escogidos]
# df_grafica['apertur'] =  [datos['apertura'][i] for datos in Data for i in datos_escogidos]
# df_grafica['error_mag'] =  [datos['MERR'][i] for datos in Data for i in datos_escogidos]
# df_grafica['filtro'] =  [datos['IFILTER'][i] for datos in Data for i in datos_escogidos]
# df_grafica['number'] =  [datos.index[i] for datos in Data for i in datos_escogidos]

# plt.scatter( df_grafica['apertur'], df_grafica['magnitude'],)
        
# df_grafica.plot['apertur']['magnitude']#, c=df_grafica['filtro'] 
# plt.xlabel('Apertura')
# plt.ylabel('Magnitud')

