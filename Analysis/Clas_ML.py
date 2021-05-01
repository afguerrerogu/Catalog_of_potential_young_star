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



X_data = np.matrix(data[["abs(V-I)","abs(V-R)","abs(R-I)"]])
X_resul = np.matrix(data[["dif_VI","dif_VR"]])  

train_data, test_data, train_resul, test_resul = train_test_split(X_data,X_resul,
                                                                  test_size=0.2)

d_tree = DecisionTreeRegressor()
d_tree.fit(train_data,train_resul)

predictions = d_tree.predict(test_data)

