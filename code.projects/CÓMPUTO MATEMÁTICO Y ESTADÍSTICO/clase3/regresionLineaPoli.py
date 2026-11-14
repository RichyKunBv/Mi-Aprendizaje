# -*- coding: utf-8 -*-

# como importar las biliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




#Importar el dataset
conjuntoDeDatos = pd.read_csv("Salarios.csv")
X = conjuntoDeDatos.iloc[:,1:2].values
y = conjuntoDeDatos.iloc[:,2].values


#No dividimos los datos de entrenamientopor que toda la informaicon es necesaria



#Ajustar la regresion lineal con el dataset.
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)



#Ajustar la regresion polinomica con el dataset.
from sklearn.preprocessing import PolynomialFeatures
#Aqui lo que vemos es que esta X pero no estan sus potencias que son X2, hasta el orden que queramos.
#esto lo hace la biblioteca proprocessing
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)
#fit crea el modelo
#fit tranforma crea y aplica le modelo.
#la columna de unos a veces lo necesita el lenguaje de programacion.
#ahora necesitamos un nuevo objeto de regresión
lin_reg_2 = LinearRegression()
#Usamos la mismas
lin_reg_2.fit(X_poly,y)
#Simplemente tranformmos las variables


#Visualizacion de los resultador del modleo linea y del pñinomico


#Del Modelo lineal

plt.scatter(X,y,color="red")
plt.plot(X,lin_reg.predict(X), color="blue")
plt.title("Modelo de regresion lineal")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()
#Analizar las graficas. POr que es malo el moodelo lineal

#MOdelo polinomico.
#solo le cambiomos con el modelo que hicimos con dos
plt.scatter(X,y,color="red")
#Solo estoy utilizando el X por que son los puntos que estoy utilizanado.
plt.plot(X,lin_reg_2.predict(X_poly), color="blue")
# esto es igual alo siguiente
#plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)), color="blue")
plt.title("Modelo de regresion polinomico")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()



#Que oasa le le agegamos un grado mas
#en este caso seria de grado 3

poly_reg3 = PolynomialFeatures(degree = 3)
X_poly3 = poly_reg3.fit_transform(X)
lin_reg_3 = LinearRegression()
lin_reg_3.fit(X_poly3,y)


#MOdelo polinomico gradi 3


plt.scatter(X,y,color="red")
plt.plot(X,lin_reg_3.predict(X_poly3), color="blue")
plt.title("Modelo de regresion polinomico grado 3")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()





#Grado 4


poly_reg4 = PolynomialFeatures(degree = 4)
X_poly4 = poly_reg4.fit_transform(X)
lin_reg_4 = LinearRegression()
lin_reg_4.fit(X_poly4,y)





#Para que no se vean lospunto unidos ppor rectas `podemos suavizar agregando mas puntos.
#.1 soon los intervalos
X_grid = np.arange(min(X),max(X), 0.1)
#Tranformas el filas, X_grid y el numero de columnas
X_grid = X_grid.reshape(len(X_grid),1)


#MOdelo polinomico gradi 3
plt.scatter(X,y,color="red")
plt.plot(X_grid,lin_reg_4.predict(poly_reg4.fit_transform(X_grid)), color="blue")
plt.title("Modelo de regresion polinomico grado 4")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()




#Prediccion de los modelos




lin_reg.predict([[6.5]])
#este modelo no predice bien.


#Neceitamos agrergar eñ objeto para que se adecue al grado dado que las deimensiones no son las mism,a
#es decir tengo que hacer la tranformacion polinomica
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))



lin_reg_3.predict(poly_reg3.fit_transform([[6.5]]))




lin_reg_4.predict(poly_reg4.fit_transform([[6.5]]))



#Neceitamos agrergar eñ objeto para que se adecue al grado dado que las deimensiones no son las mism,a
lin_reg_2.predict(poly_reg.fit_transform([[8]]))



lin_reg_3.predict(poly_reg3.fit_transform([[8]]))




lin_reg_4.predict(poly_reg4.fit_transform([[8]]))



