#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:15:43 2021

@author: andres
"""

import pandas as pd
import numpy as np
import  math 
from  matplotlib import pyplot as plt 
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# Leemos los archivos
teo_VI = pd.read_csv('zamsvi',sep=' ',index_col=None, names=["V-I","Mag"] )
teo_VR = pd.read_csv('zamsvr',sep=' ',index_col=None, names=["V-R","Mag"] )
sciencecalibN3L = np.loadtxt('sciencecalibN3L',dtype='str')
sciencecalibN3S = np.loadtxt('sciencecalibN3S',dtype='str')
sciencecalibN3L = pd.DataFrame(sciencecalibN3L,columns=["ID","V","e_V","V-R","e_V-R","V-I","e_V-I"])
sciencecalibN3S = pd.DataFrame(sciencecalibN3S,columns=["ID","V","e_V","V-R","e_V-R","V-I","e_V-I"])

sciencecalibN3L['V'] = pd.to_numeric(sciencecalibN3L['V']) 
sciencecalibN3L['e_V'] = pd.to_numeric(sciencecalibN3L['e_V']) 
sciencecalibN3L['V-R'] = pd.to_numeric(sciencecalibN3L['V-R']) 
sciencecalibN3L['e_V-R'] = pd.to_numeric(sciencecalibN3L['e_V-R'])
sciencecalibN3L['V-I'] = pd.to_numeric(sciencecalibN3L['V-I'])
sciencecalibN3L['e_V-I'] = pd.to_numeric(sciencecalibN3L['e_V-I'])

sciencecalibN3S['V'] = pd.to_numeric(sciencecalibN3S['V']) 
sciencecalibN3S['e_V'] = pd.to_numeric(sciencecalibN3S['e_V']) 
sciencecalibN3S['V-R'] = pd.to_numeric(sciencecalibN3S['V-R']) 
sciencecalibN3S['e_V-R'] = pd.to_numeric(sciencecalibN3S['e_V-R'])
sciencecalibN3S['V-I'] = pd.to_numeric(sciencecalibN3S['V-I'])
sciencecalibN3S['e_V-I'] = pd.to_numeric(sciencecalibN3S['e_V-I'])


#definimos constantes

E_BV = 0.12 # exceso E(B-V)

A_v = 3.1*E_BV
A_r = 0.748*A_v # A_r/A_v = 0.748
A_i = 0.482*A_v # A_i/A_v = 0.482

d = 450 # distancia

# Calculo de magnitudes absolutas
sciencecalibN3L['abs(V)'] = sciencecalibN3L['V']-5*math.log10(d)+5-A_v
sciencecalibN3L['abs(V-I)'] = sciencecalibN3L['V-I'] + A_v-A_i
sciencecalibN3L['abs(V-R)'] = sciencecalibN3L['V-R'] + A_v-A_r
sciencecalibN3L['abs(R-I)'] = sciencecalibN3L['abs(V-I)'] - sciencecalibN3L['abs(V-R)']

sciencecalibN3S['abs(V)'] = sciencecalibN3S['V']-5*math.log10(d)+5-A_v
sciencecalibN3S['abs(V-I)'] = sciencecalibN3S['V-I'] + A_v-A_i
sciencecalibN3S['abs(V-R)'] = sciencecalibN3S['V-R'] + A_v-A_r
sciencecalibN3S['abs(R-I)'] = sciencecalibN3S['abs(V-I)'] - sciencecalibN3S['abs(V-R)']  


plt.figure(1,figsize=(8,8))
plt.plot(teo_VI['V-I'],teo_VI['Mag'],c='indigo',label="V-I")
plt.scatter(sciencecalibN3S['abs(V-I)'],sciencecalibN3S['abs(V)'],c='k',marker='*',label="S")
plt.scatter(sciencecalibN3L['abs(V-I)'],sciencecalibN3L['abs(V)'],c='b',s=0.5,marker='o',label="L")
plt.ylim((19,-2.5))
plt.xlabel(r"V - I")
plt.ylabel(r"V")
plt.legend()
plt.savefig("VvsV-I.png")


plt.figure(2,figsize=(8,8))
plt.plot(teo_VR['V-R'],teo_VR['Mag'],c='indigo',label="V-R")
plt.scatter(sciencecalibN3S['abs(V-R)'],sciencecalibN3S['abs(V)'],c='k',marker='*',label="S")
plt.scatter(sciencecalibN3L['abs(V-R)'],sciencecalibN3L['abs(V)'],c='b',s=0.5,marker='o',label="L")
plt.ylim((19,-2.5))
plt.xlabel(r"V - R")
plt.ylabel(r"V")
plt.legend()
plt.savefig("VvsV-R.png")


plt.figure(3,figsize=(15,8))
plt.plot(teo_VI['V-I'],teo_VI['Mag'],c='indigo',label="V-I")
plt.errorbar(sciencecalibN3S['abs(V-I)'],sciencecalibN3S['abs(V)'],
             xerr=sciencecalibN3S['e_V-I'],c='k' , fmt='.')
plt.errorbar(sciencecalibN3L['abs(V-I)'],sciencecalibN3L['abs(V)'],
             xerr=sciencecalibN3L['e_V-I'],c='b',fmt='o')
plt.ylim((19,-2.5))
plt.xlabel(r"V - R")
plt.ylabel(r"V") 
plt.savefig("barerr.png")


# Figura de los errores


fig,ax = plt.subplots(figsize=(8,8))
ax.scatter(sciencecalibN3S['abs(V)'],sciencecalibN3S['e_V'],c='k',marker='*',label= 'S',s=5)
ax.scatter(sciencecalibN3L['abs(V)'],sciencecalibN3L['e_V'],c='r', marker='o',label= 'L',s=5)
ax.legend()
ax.set_xlabel('V')
ax.set_ylabel('error V')

axins1 = zoomed_inset_axes(ax, zoom = 2.5, loc=6)
axins1.scatter(sciencecalibN3S['abs(V)'],sciencecalibN3S['e_V'],c='k',marker='*',label= 'S',s=5)
axins1.scatter(sciencecalibN3L['abs(V)'],sciencecalibN3L['e_V'],c='r', marker='o',label= 'L',s=5)

x1, x2, y1, y2 = 9,14,-1.5,2.5 
axins1.set_xlim(x1, x2)
axins1.set_ylim(y1, y2)

plt.xticks(visible=True)
plt.yticks(visible=False)

mark_inset(ax, axins1, loc1=1, loc2=4, fc="none", ec="0.5")
plt.savefig("errores.png")



#eliminamos todas las medidas que tengan errores en magnitud mayores a 0.5

sciencecalibN3L = sciencecalibN3L[(sciencecalibN3L['e_V'] <= 0.5) & (sciencecalibN3L['e_V-R'] <= 0.5)
                                  & (sciencecalibN3L['e_V-I'] <=0.5) ]
sciencecalibN3S = sciencecalibN3S[(sciencecalibN3S['e_V'] <= 0.5) & (sciencecalibN3S['e_V-R'] <= 0.5)
                                  & (sciencecalibN3S['e_V-I'] <=0.5) ]

# para medidas con magnitudes menores a 9 vamos a usar las medidas SHORT
# para medidas con magnitudes mayores a 9 vamos a usar las medidas LARGE

sciencecalibN3S = sciencecalibN3S[sciencecalibN3S['abs(V)']<9]
sciencecalibN3L = sciencecalibN3L[sciencecalibN3L['abs(V)']>9]

plt.figure(5,figsize=(15,8))
plt.scatter(sciencecalibN3S['abs(V)'],sciencecalibN3S['e_V'],c='k',marker='*',label= 'S',s=5)
plt.scatter(sciencecalibN3L['abs(V)'],sciencecalibN3L['e_V'],c='r', marker='o',label= 'L',s=5)
plt.xlabel(r"V")
plt.ylabel(r"error V")



catalog = sciencecalibN3S.append(sciencecalibN3L)

plt.figure(6,figsize=(8,8))
plt.plot(teo_VI['V-I'],teo_VI['Mag'],c='indigo',label="V-I")
plt.scatter(sciencecalibN3S['abs(V-I)'],sciencecalibN3S['abs(V)'],c='k',marker='*',label="S")
plt.scatter(sciencecalibN3L['abs(V-I)'],sciencecalibN3L['abs(V)'],c='red',s=1,marker='o',label="L")
plt.scatter(catalog['abs(V-I)'],catalog['abs(V)'], color='green',s=0.1,label="MATCH")
plt.ylim((19,-2.5))
plt.xlabel(r"V - I")
plt.ylabel(r"V")
plt.legend()
plt.savefig("matchV-I.png")

plt.figure(7,figsize=(8,8))
plt.plot(teo_VR['V-R'],teo_VR['Mag'],c='indigo',label="V-R")
plt.scatter(sciencecalibN3S['abs(V-R)'],sciencecalibN3S['abs(V)'],c='k',marker='*',label="S")
plt.scatter(sciencecalibN3L['abs(V-R)'],sciencecalibN3L['abs(V)'],c='red',s=1,marker='o',label="L")
plt.scatter(catalog['abs(V-R)'],catalog['abs(V)'], color='green',s=0.1,label="MATCH")
plt.ylim((19,-2.5))
plt.xlabel(r"V - R")
plt.ylabel(r"V")
plt.legend()
plt.savefig("matchV-R.png")

catalog.to_csv('new_catalog.dat')
