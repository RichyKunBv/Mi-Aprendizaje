#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: eduardo
"""

# como importar las biliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




#Importar el dataset
conjuntoDeDatos = pd.read_csv("Salarios.csv")
X = conjuntoDeDatos.iloc[:,1:2].values
y = conjuntoDeDatos.iloc[:,2].values




#Crear modelo
#Documentacion
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
# para apremdizaje cpnjuntos
from sklearn.ensemble import RandomForestRegressor
#n_estimators por default vienen 10. que es el numeor de arboles.
#ciretrion . minimum square error
#max_features
regresion = RandomForestRegressor(n_estimators = 100, random_state=0)
regresion.fit(X,y)






#Prediccion de los datosl
y_pred= regresion.predict([[6.5]])




#Visualizacion de los dDatos


#MOdelo polinomico gradi 3
plt.scatter(X,y,color="red")
plt.plot(X,regresion.predict(X), color="blue")
plt.title("Modelo de Arboles")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()
