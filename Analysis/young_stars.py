#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:09:07 2021

@author: andres
"""

import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt

data = pd.read_csv("new_catalog.dat",index_col=1)
teo_VI = pd.read_csv('zamsvi',sep=' ',index_col=None, names=["V-I","Mag"] )
teo_VR = pd.read_csv('zamsvr',sep=' ',index_col=None, names=["V-R","Mag"] )


# CONSTRUIMOS EL POLINOMIO PARA V-I
Data_train_VI = teo_VI["V-I"].tolist()
resul_train_VI = teo_VI["Mag"].tolist()

x_VI = np.linspace(min(Data_train_VI),max(Data_train_VI),1001)

coef_VI = np.polyfit(Data_train_VI, resul_train_VI,3)
ecu_VI = np.poly1d(coef_VI)
yvals_VI= ecu_VI(x_VI)

print ("ecuacion polinomica para V-I: \n" , ecu_VI)
#y_s = InterpolatedUnivariateSpline(Data_train, resul_train)(x)

plt.figure(1,figsize=(8,8))
plt.plot(Data_train_VI, resul_train_VI, label="teorica", c='black')
plt.plot(x_VI,yvals_VI,label="ajuste", c='red')
plt.scatter(data["abs(V-I)"],data["abs(V)"],color="gray",s=60)
plt.xlabel("V - I")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.savefig("ecuVI.png")

# CONSTRUIMOS EL POLINOMIO PARA V-R
Data_train_VR = teo_VR["V-R"].tolist()
resul_train_VR = teo_VR["Mag"].tolist()

x_VR = np.linspace(min(Data_train_VR),max(Data_train_VR),1001)

coef_VR = np.polyfit(Data_train_VR, resul_train_VR,3)
ecu_VR = np.poly1d(coef_VR)
yvals_VR= ecu_VR(x_VR)

print ("ecuacion polinomica para V-R: \n" , ecu_VR)

plt.figure(2,figsize=(8,8))
plt.plot(Data_train_VR, resul_train_VR, label="teorica", c='black')
plt.plot(x_VR,yvals_VR,label="ajuste", c='red')
plt.scatter(data["abs(V-R)"],data["abs(V)"],color="gray",s=60)
plt.xlabel("V - R")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.savefig("ecuVR.png")

#medimos la diferencia de cada punto al polinomio

data["dif_VI"] = ecu_VI(data["abs(V-I)"]) - data["abs(V)"]
data["dif_VR"] = ecu_VR(data["abs(V-R)"]) - data["abs(V)"]

#Tomoamos solo los datos que la dif sea positiva

Catalogo = data[(data["dif_VI"] > 0.5 ) & (data["dif_VR"] > 0.5)]

#graficamos 

plt.figure(3,figsize=(8,8))
plt.plot(Data_train_VR, resul_train_VR, label="teorica", c='black')
plt.plot(x_VR,yvals_VR,label="ajuste", c='red')
plt.scatter(data["abs(V-R)"],data["abs(V)"],color="gray",s=60)
plt.scatter(Catalogo["abs(V-R)"],Catalogo["abs(V)"],label="Potenciales estrellas Jovenes")
plt.xlabel("V - R")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.xlim((-1,3))
plt.savefig("young_VR.png")


plt.figure(4,figsize=(8,8))
plt.plot(Data_train_VI, resul_train_VI, label="teorica", c='black')
plt.plot(x_VI,yvals_VI,label="ajuste", c='red')
plt.scatter(data["abs(V-I)"],data["abs(V)"],color="gray",s=60)
plt.scatter(Catalogo["abs(V-I)"],Catalogo["abs(V)"],label="Potenciales estrellas Jovenes")
plt.xlabel("V - I")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.xlim((0,4))
plt.savefig("young_VI.png")


Catalogo.to_csv('Catalogo_de_estrellas_jovenes.dat')


"""necesario para el siguente paso"""

data.to_csv("catalogo_sin_separar.dat")