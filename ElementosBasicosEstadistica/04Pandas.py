import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#mostrar las primeras 5 filas
print(df.head())

#Mostrar las ultimas 5 filas
print(df.tail())

#mostrar una fila en especifico

print(df.iloc[7])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#obtener la media de la columna total_rooms
mediadecuarto = df["total_rooms"].mean()
print('La media de total de room es: ' + mediadecuarto)

#mediana
medianadecuarto = df['median_house_value'].median()
print('la mediana de la columna valor mediana de la casa ' + medianadecuarto)

#la suma popular
salariototal = df['population'].sum()
print('El salario total es de: ', salariototal)


#para poder filtrar
vamosahacerunfiltro = df[df['oxeanproximity'] == 'ISLAND']
print('Vamos a hacer un filtro: ')

