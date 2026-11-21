#-*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""
#Utiliza todas la variables.

# como importar las biliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importar el dataset
conjuntoDeDatos = pd.read_csv("50_startups.csv")
X = conjuntoDeDatos.iloc[:,:-1].values
y = conjuntoDeDatos.iloc[:,4].values



#Procesamos  los datos categoricos antes dlee ntrnamiento
#Datos Categoricos.
#Codificar Datos Categoricos.



from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer



#etiquedaCodificada_X = LabelEncoder()
#Ahora e sla tercera columna donde estan los datos categoricos.


#X[:,3]= etiquedaCodificada_X.fit_transform(X[:,3])
#variableOneHotEncoder = OneHotEncoder(categorical_features=[3])
#X = variableOneHotEncoder.fit_transform(X).toarray()


ls = ColumnTransformer([('State',OneHotEncoder(categories='auto'),[3])], remainder='passthrough')
X=ls.fit_transform(X).astype(float)

#Ahora necesitamos el verdadero sy el falso3
#Ahora a y no lo necesito por que la variable independiente no lo necesita.
#Evitar la tranmpa p eñ `rpblema de las variables dummy
#hay que eliminar un elemento.
#Eliminamos la primer columna que es una variable dummy
#podriamos eliminar la que quisieramos.
X=X[:,1:]






#Para dividir el data set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=0)


#Ajustar el modelo de regresion lineal multiple con el conjunto de entrenamiento.
#La bilbioteca esta preparada para la regresion linear simple y multiple


from sklearn.linear_model import LinearRegression
regresion = LinearRegression()
regresion.fit(x_train,y_train)


#Prediccion de loa resultados en test.
y_pred = regresion.predict(x_test)  
# se compara con resptecto y_test

#Construir la eliminacion hacia atras-
# Con el objetivo de construi un modelo optimo

#La biblioteca nos sirve para eliminar variables.

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


#para agregarlo en la primera columna
#X = np.append(arr = X, values = np.ones((50,1)).astype(int),axis =1)
#0 en fila 1 en columna

#Para agregarlo en la primera columna
X = np.append(arr = np.ones((50,1)).astype(int), values = X,axis =1,)

#Se crea una variable de significacion
SL= 0.05

X_opt = X[:,[0,1,2,3,4,5]].tolist()


#Necesitamos crear otro modelo de regresion con la biblioteca de statsmodel
regresion_OLS = sm.OLS(endog= y, exog= X_opt).fit()
#exog es la que nos pide la columna d eunos. endog = endogeno exog=exogeno
#esta hace lo mismo que la scklearn en el fit.
regresion_OLS.summary()
print(regresion_OLS.summary())





X_opt = X[:,[0,1,3,4,5]].tolist()
#Necesitamos crear otro modelo de regrwsion con la bibñioteca de statsmodel
regresion_OLS = sm.OLS(endog= y, exog= X_opt).fit()
#exog es la que nos pide la columna d eunos. endog = endogeno exog=exogeno
#esta hace lo mismo que la scklearn en el fit.
regresion_OLS.summary()
print(regresion_OLS.summary())




X_opt = X[:,[0,3,4,5]].tolist()
#Necesitamos crear otro modelo de regrwsion con la bibñioteca de statsmodel
regresion_OLS = sm.OLS(endog= y, exog= X_opt).fit()
#exog es la que nos pide la columna d eunos. endog = endogeno exog=exogeno
#esta hace lo mismo que la scklearn en el fit.
regresion_OLS.summary()
print(regresion_OLS.summary())




X_opt = X[:,[0,3,5]].tolist()
#Necesitamos crear otro modelo de regrwsion con la bibñioteca de statsmodel
regresion_OLS = sm.OLS(endog= y, exog= X_opt).fit()
#exog es la que nos pide la columna d eunos. endog = endogeno exog=exogeno
#esta hace lo mismo que la scklearn en el fit.
regresion_OLS.summary()
print(regresion_OLS.summary())

#Es mejor la de arriba


X_opt = X[:,[0,3]].tolist()
#Necesitamos crear otro modelo de regrwsion con la bibñioteca de statsmodel
regresion_OLS = sm.OLS(endog= y, exog= X_opt).fit()
#exog es la que nos pide la columna d eunos. endog = endogeno exog=exogeno
#esta hace lo mismo que la scklearn en el fit.
regresion_OLS.summary()
print(regresion_OLS.summary())








