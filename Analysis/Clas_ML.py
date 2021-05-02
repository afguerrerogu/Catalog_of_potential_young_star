#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 01:52:02 2021

@author: andres
"""

import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv("catalogo_sin_separar.dat")

data["young"] = np.zeros(len(data))


for i in data.index:
    if ((data["dif_VI"][i] > 0.5) & (data["dif_VR"][i] > 0.5) & (data["dif_RI"][i] > 0.5)):
        data["young"][i] = 1
    else:
        data["young"][i] = -1


X_data = np.matrix(data[["abs(V-I)","abs(V-R)","abs(R-I)"]])
X_resul = data["young"]  

train_data, test_data, train_resul, test_resul = train_test_split(X_data,X_resul,
                                                                  test_size=0.2)

d_tree = DecisionTreeRegressor()
d_tree.fit(train_data,train_resul)

predictions = d_tree.predict(test_data)

R2 = d_tree.score(train_data, train_resul)
R2_test = d_tree.score(test_data, test_resul)
deep = d_tree.get_depth()

pres = predictions - test_resul

y = [i for i in range(350)]
x = np.zeros(350)
bbox = dict(boxstyle="round", fc="0.8")

plt.hist(predictions ,density=False, histtype='bar', rwidth=0.9, bins=2,color="k", label="prediction")
plt.hist(test_resul, density=False, histtype='bar', rwidth=0.2,bins=2,color='darkblue',label="test result")
plt.plot(x,y,'--', color="red")
plt.annotate(r"young", (0.4,200),bbox=bbox)
plt.annotate(r"not young", (-0.6,340),bbox=bbox)
plt.xticks(visible=False)
plt.legend()
plt.savefig("histo.png")