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

#datos_escogidos = [random.randint(0,1420) for i in range(0,1000)]
datos_escogidos = [83]
df_grafica = pd.DataFrame()

df_grafica['magnitude'] =  [datos['MAG'][i] for datos in Data for i in datos_escogidos]
df_grafica['apertur'] =  [datos['apertura'][i] for datos in Data for i in datos_escogidos]
#df_grafica['error_mag'] =  [datos['MERR'][i] for datos in Data for i in datos_escogidos]
#df_grafica['filtro'] =  [datos['IFILTER'][i] for datos in Data for i in datos_escogidos]
#df_grafica['number'] =  [datos.index[i] for datos in Data for i in datos_escogidos]

plt.figure()
plt.scatter( df_grafica['apertur'], df_grafica['magnitude'])
plt.xlabel("Apertura")
plt.ylabel("Magnitud")
plt.savefig("opaper_standar1.png" )

datos_escogidos = [2]
df_grafica = pd.DataFrame()

df_grafica['magnitude'] =  [datos['MAG'][i] for datos in Data for i in datos_escogidos]
df_grafica['apertur'] =  [datos['apertura'][i] for datos in Data for i in datos_escogidos]
#df_grafica['error_mag'] =  [datos['MERR'][i] for datos in Data for i in datos_escogidos]
#df_grafica['filtro'] =  [datos['IFILTER'][i] for datos in Data for i in datos_escogidos]
#df_grafica['number'] =  [datos.index[i] for datos in Data for i in datos_escogidos]

plt.figure(2)
plt.scatter( df_grafica['apertur'], df_grafica['magnitude'])
plt.xlabel("Apertura")
plt.ylabel("Magnitud")
plt.savefig("opaper_standar2.png" )

datos_escogidos = [849]
df_grafica = pd.DataFrame()

df_grafica['magnitude'] =  [datos['MAG'][i] for datos in Data for i in datos_escogidos]
df_grafica['apertur'] =  [datos['apertura'][i] for datos in Data for i in datos_escogidos]
#df_grafica['error_mag'] =  [datos['MERR'][i] for datos in Data for i in datos_escogidos]
#df_grafica['filtro'] =  [datos['IFILTER'][i] for datos in Data for i in datos_escogidos]
#df_grafica['number'] =  [datos.index[i] for datos in Data for i in datos_escogidos]

plt.figure(3)
plt.scatter( df_grafica['apertur'], df_grafica['magnitude'])
plt.xlabel("Apertura")
plt.ylabel("Magnitud")
plt.savefig("opaper_standar3.png" )

datos_escogidos = [1420]
df_grafica = pd.DataFrame()

df_grafica['magnitude'] =  [datos['MAG'][i] for datos in Data for i in datos_escogidos]
df_grafica['apertur'] =  [datos['apertura'][i] for datos in Data for i in datos_escogidos]
#df_grafica['error_mag'] =  [datos['MERR'][i] for datos in Data for i in datos_escogidos]
#df_grafica['filtro'] =  [datos['IFILTER'][i] for datos in Data for i in datos_escogidos]
#df_grafica['number'] =  [datos.index[i] for datos in Data for i in datos_escogidos]

plt.figure(4)
plt.scatter( df_grafica['apertur'], df_grafica['magnitude'])
plt.xlabel("Apertura")
plt.ylabel("Magnitud")
plt.savefig("opaper_standar4.png" )