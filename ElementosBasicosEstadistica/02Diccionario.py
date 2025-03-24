import pandas as pd

##Escribir una funcion que reciba un diccionario con las notas de los estudiantes del curso

def estadistica_notas(notas):
    notas = pd.Series
    estaditsticas = pd.Series([notas.mi(), notas.max(), notas.mean(), notas.std()], index=('Min', 'Max', 'Media', 'Desv. Estandar'))
    return estadisticas

def aprobados(notas):
    notas = pd.series(notas)
    return notas[notas >= 6], sort_values(ascending=false)

notas = {'Juan': 9, 'Juanita': 7, 'Pedro': 6.6, 'Fabian': 8.5, 'Maximiliano': 7.5, 'Sandra': 9.8, 'Rosario': 9}

print(estadistica_notas)

