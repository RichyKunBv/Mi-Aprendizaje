#-*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

# Regreson lineal

# como importar las biliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar el dataset
conjuntoDeDatos = pd.read_csv("Salario.csv")
X = conjuntoDeDatos.iloc[:,:-1].values


y = conjuntoDeDatos.iloc[:,1].values
# le ponemoa y minuscual por que es un vector.
# Dividir el data set en cpnjunto de entrenamiento y el conjunto testing.
#Vamos a tener cuatro variables la x de entrenamiento y la x de text
#Vamos a tener la y de entrnamiento y la y de test


#Para dividir el data set
from sklearn.model_selection import train_test_split
#Recuerden que siempre va el 80% d eprueba y menos de entrenamiento 20%
#el random puede ir cualquier valor
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)



#No hace falta escalado.

from sklearn.linear_model import LinearRegression

regresion = LinearRegression()
regresion.fit(x_train,y_train)
#La extension d elos vectores x y y deben de ser del mismo tamaño


#Para  oredecir vamos a construir un vector

#Vamos a meterle la prediccion.
y_pred = regresion.predict(x_test)

#no le estamos metiendo la y.

#Visualizar los datos de entrenamiento.
#Vamos a ver una nube de dispersion.
plt.scatter(x_train,y_train, color= "red")
#Vamos a contrastarlo con las prediciones
plt.plot(x_train,regresion.predict(x_train),color ="blue")
plt.title("Sueldo y años de experiencia utilizando el conjunto de entrenamiento")
plt.xlabel("Años de experiencia")
plt.ylabel("Ingresos")
plt.show()

#lo anterio es con el entrenamiento.


#Ahora vamos a cambiarlas por el entrenameinto




#Visualizar los datos de test.
#Vamos a ver una nube de dispersion.
plt.scatter(x_test,y_test, color= "red")
#Vamos a contrastarlo con las prediciones


#ojo usamos el mismo de entrenamiento, por que queremos ver como se mueve
plt.plot(x_train,regresion.predict(x_train),color ="blue")
plt.title("Sueldo y años de experiencia utilizando el conjunto de Test")
plt.xlabel("Años de experiencia")
plt.ylabel("Ingresos")
plt.show()

#lo anterio es con el entrenamiento.

