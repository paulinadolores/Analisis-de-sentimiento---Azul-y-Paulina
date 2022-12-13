import pandas as pd
import matplotlib.pyplot as plt

###Leemos el archivo csv

df = pd.read_csv("data_covid.csv")

###Verificamos que el dataset fue cargado con exito
print(df)

####Hacemos la suma de los datos nulos
print(df.isnull().sum())

###Breve resumen del dataset
print(df.info())


###Mostramos las primeras filas
print(df.head())

###Mostramos las ultimas filas
print(df.tail())

####para saber la cantidad de columnas que tenemos
print(df.shape)

###columnas 
print(df.columns)

####La cantidad de datos que tiene cada columna

print(df.count())

# Limpiamos los elementos nulos
###No limpiamos la fecha de fallecimiento ya que quizas el dato esta null porque no fallecieron
data = df.dropna(subset=['tipo_contagio'])
data = df.dropna(subset=['resultado'])
data = df.dropna(subset=['fecha_alta'])
data = df.dropna(subset=['provincia'])
data = df.dropna(subset=['fecha_resultado'])
data = df.dropna(subset=['fecha_test'])
data = df.dropna(subset=['barrio'])
data = df.dropna(subset=['edad'])
data = df.dropna(subset=['fecha_alta'])

print(data)

###Limpieza total del dataset 
#print(df.dropna(1))


#Graficos matplot
cantidad_casos = df.groupby('edad')['resultado'].count()
cantidad_casos.plot(kind='bar')
#plt.show()