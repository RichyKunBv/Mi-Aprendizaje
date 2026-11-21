#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:25:44 2020

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
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html



from sklearn.tree import DecisionTreeRegressor
regresion = DecisionTreeRegressor(random_state=0)
#podmeos poner el que quewramos en el random state
regresion.fit(X,y)




#Prediccion de los datosl
y_pred= regresion.predict([[6.5]])
print(y_pred)



#Visualizacion de los dDatos


#MOdelo polinomico gradi 3
plt.scatter(X,y,color="red")
plt.plot(X,regresion.predict(X), color="blue")
plt.title("Arbol")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()

#Aqui pasa por todos los puntos. es como habiamos visto lo esta clasificando por el punto mas cercano `por eso clasifica
#en este punto.
#es decir no podra predecir mas alla del nivel 10.





