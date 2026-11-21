#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:32:10 2020

@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importar el dataset
conjuntoDeDatos = pd.read_csv("AnunciosRedesSociales.csv")


X = conjuntoDeDatos.iloc[:,[2,3]].values
y = conjuntoDeDatos.iloc[:,4].values





#Para dividir el data set
from sklearn.model_selection import train_test_split
#Recuerden que siempre va el 80% d eprueba y menos de entrenamiento 20%
#el random puede ir cualquier valor
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=.25,random_state=0)





#el escalado
from sklearn.preprocessing import StandardScaler
#
escaladorEnX=StandardScaler()
x_train= escaladorEnX.fit_transform(x_train)
x_test =escaladorEnX.fit_transform(x_test)





from sklearn.linear_model import LogisticRegression

clasificador = LogisticRegression(random_state=0)
clasificador.fit(x_train,y_train)


#Preddion ce los resultados con el conjunto de testingç
y_predice = clasificador.predict(x_test)




#Evaluar el rendimiento con una matriz de confusion.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predice)





 #Representacion grafica del algoritmo
from matplotlib.colors import ListedColormap

X_set,y_set = x_train, y_train
X1,X2 = np.meshgrid(np.arange(start= X_set[:,0].min()-1,stop = X_set[:,0].max()+1,step = 0.01),
                    np.arange(start= X_set[:,1].min()-1,stop = X_set[:,1].max()+1,step = 0.01))

plt.contourf(X1,X2,clasificador.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75,cmap = ListedColormap(('red','green')))

plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())

#Los puntos
for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                    c= ListedColormap(('red','green'))(i),label = j)
        
        
        
        
plt.title('Clasificador el conjunto de entrenamiento')
plt.xlabel('edad')
plt.ylabel('Salario estimado')
plt.legend()
plt.show()




 #Representacion grafica del algoritmo
from matplotlib.colors import ListedColormap

X_set,y_set = x_test, y_test
X1,X2 = np.meshgrid(np.arange(start= X_set[:,0].min()-1,stop = X_set[:,0].max()+1,step = 0.01),
                    np.arange(start= X_set[:,1].min()-1,stop = X_set[:,1].max()+1,step = 0.01))

plt.contourf(X1,X2,clasificador.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75,cmap = ListedColormap(('red','green')))

plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())

#Los puntos
for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                    c= ListedColormap(('red','green'))(i),label = j)
        
        
        
        
plt.title('Clasificador el conjunto de test')
plt.xlabel('edad')
plt.ylabel('Salario estimado')
plt.legend()
plt.show()
