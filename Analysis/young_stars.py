#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:09:07 2021

@author: andres
"""

import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt
import os

data = pd.read_csv("new_catalog.dat",index_col=1)
teo_VI = pd.read_csv('zamsvi',sep=' ',index_col=None, names=["V-I","Mag"] )
teo_VR = pd.read_csv('zamsvr',sep=' ',index_col=None, names=["V-R","Mag"] )
teoricas = np.loadtxt('zams_explained.dat', usecols=(9,10,12,14,15),)
teoricas = pd.DataFrame(teoricas,columns=["V-R","V-I","Mv","Mr","Mi"])
teoricas["R-I"] = teoricas["Mr"] - teoricas["Mi"]


# CONSTRUIMOS EL POLINOMIO PARA V-I
Data_train_VI = teo_VI["V-I"].tolist()
resul_train_VI = teo_VI["Mag"].tolist()

x_VI = np.linspace(min(Data_train_VI),max(Data_train_VI),1001)

coef_VI = np.polyfit(Data_train_VI, resul_train_VI,3)
ecu_VI = np.poly1d(coef_VI)
yvals_VI= ecu_VI(x_VI)

print ("ecuacion polinomica para V-I: \n" , ecu_VI)
print("full: \n", np.polyfit(Data_train_VI, resul_train_VI,3,full=True))
#y_s = InterpolatedUnivariateSpline(Data_train, resul_train)(x)

plt.figure(1)
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
print("full: \n", np.polyfit(Data_train_VR, resul_train_VR,3,full=True))

plt.figure(2)
plt.plot(Data_train_VR, resul_train_VR, label="teorica", c='black')
plt.plot(x_VR,yvals_VR,label="ajuste", c='red')
plt.scatter(data["abs(V-R)"],data["abs(V)"],color="gray",s=60)
plt.xlabel("V - R")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.savefig("ecuVR.png")

# CONSTRUIMOS EL POLINOMIO PARA R-I

Data_train_RI = teoricas["R-I"].tolist()
resul_train_RI = teoricas["Mv"].tolist()

x_RI = np.linspace(min(Data_train_RI),max(Data_train_RI),1001)

coef_RI = np.polyfit(Data_train_RI, resul_train_RI,3)
ecu_RI = np.poly1d(coef_RI)
yvals_RI= ecu_RI(x_RI)

print ("ecuacion polinomica para R-I: \n" , ecu_RI)
print("full: \n", np.polyfit(Data_train_RI, resul_train_RI,3,full=True))

plt.figure(3)
plt.plot(Data_train_RI, resul_train_RI, label="teorica", c='black')
plt.plot(x_RI,yvals_RI,label="ajuste", c='red')
plt.scatter(data["abs(R-I)"],data["abs(V)"],color="gray",s=60)
plt.xlabel("R - I")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.savefig("ecuRI.png")


#medimos la diferencia de cada punto al polinomio

data["dif_VI"] = ecu_VI(data["abs(V-I)"]) - data["abs(V)"]
data["dif_VR"] = ecu_VR(data["abs(V-R)"]) - data["abs(V)"]
data["dif_RI"] = ecu_RI(data["abs(R-I)"]) - data["abs(V)"]

#Tomoamos solo los datos que la dif sea positiva

Catalogo = data[(data["dif_VI"] > 0.5 ) & (data["dif_VR"] > 0.5) & (data["dif_RI"] > 0.5)]

#graficamos 

plt.figure(4)
plt.plot(Data_train_VR, resul_train_VR, label="teorica", c='black')
plt.plot(x_VR,yvals_VR,label="ajuste", c='red')
plt.scatter(data["abs(V-R)"],data["abs(V)"],color="gray",s=60)
plt.scatter(Catalogo["abs(V-R)"],Catalogo["abs(V)"],label="Potenciales estrellas Jovenes",c="darkblue")
plt.xlabel("V - R")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.xlim((-1,3))
plt.savefig("young_VR.png")


plt.figure(5)
plt.plot(Data_train_VI, resul_train_VI, label="teorica", c='black')
plt.plot(x_VI,yvals_VI,label="ajuste", c='red')
plt.scatter(data["abs(V-I)"],data["abs(V)"],color="gray",s=60)
plt.scatter(Catalogo["abs(V-I)"],Catalogo["abs(V)"],label="Potenciales estrellas Jovenes",c="darkblue")
plt.xlabel("V - I")
plt.ylabel("V")
plt.legend()
plt.ylim((19,-2.5))
plt.xlim((0,4))
plt.savefig("young_VI.png")

plt.figure(6)
plt.plot(Data_train_RI, resul_train_RI, label="teorica", c='black')
plt.plot(x_RI,yvals_RI,label="ajuste", c='red')
plt.scatter(data["abs(R-I)"],data["abs(V)"],color="gray",s=60)
plt.scatter(Catalogo["abs(R-I)"],Catalogo["abs(V)"],label="Potenciales estrellas Jovenes",c="darkblue")
plt.xlabel("R - I")
plt.ylabel("V")
plt.legend()
plt.ylim((18,-2.5))
plt.xlim((-0.5,3))
plt.savefig("young_RI.png")

Catalogo = Catalogo.drop(["Unnamed: 0", "V","e_V","V-R","e_V-R","V-I","e_V-I","dif_VI","dif_VR","dif_RI"],axis=1)
Catalogo.columns = ["V","V-I","V-R","R-I"]
Catalogo.to_csv('Catalogo_de_estrellas_jovenes.dat')


m2 = np.loadtxt('/home/andres/Documentos/Documents/tecnicasobservacionales/Catalog_of_potential_young_star/Catalog_match/2m',
                dtype=str)
m2 = pd.DataFrame(m2,columns=["dec","AR","ID","NN"])

m2["id"] = pd.to_numeric(m2["ID"], errors='coerce')
m2 = m2.drop(["NN","ID"],axis=1)

m2 = m2.drop_duplicates(subset=["id"])

catalogo_fin = pd.merge(left=Catalogo,right=m2, left_on='ID', right_on='id')

catalogo_fin.index = catalogo_fin["id"] 
catalogo_fin = catalogo_fin.drop(["id"],axis=1)

catalogo_fin["V"] = round(catalogo_fin["V"],5)
catalogo_fin["V-I"] = round(catalogo_fin["V-I"],5)
catalogo_fin["V-R"] = round(catalogo_fin["V-R"],5)
catalogo_fin["R-I"] = round(catalogo_fin["R-I"],5)


catalogo_fin.to_csv("catalogofin.csv")

catalogo_fin.to_latex(caption="Catalogo de potenciales estellas jovenes",
                            label="cat",
                            buf="tablalatex")

"""necesario para el siguente paso"""

data.to_csv("catalogo_sin_separar.dat")