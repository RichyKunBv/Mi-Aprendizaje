import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

conjuntoDeDatos = pd.read_csv("Salarios.csv")
X = conjuntoDeDatos.iloc[:,1:2].values
y = conjuntoDeDatos.iloc[:,2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)


plt.scatter(X,y,color="red")
plt.plot(X,lin_reg.predict(X), color="blue")
plt.title("Modelo de regresion lineal")
plt.xlabel("Posicion del empleado")
plt.ylabel("Suelo")
plt.show()