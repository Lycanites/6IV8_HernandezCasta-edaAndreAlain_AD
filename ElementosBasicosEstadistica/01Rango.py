import pandas as pd

# Escribir un programa que pregunte al usuario por las ventas de un rango de años,. antes y despues de aplicarles un descuento

inicio = int(input('introduce el año de ventas inicial: '))
fin = int(input('Introduce el año final de ventas: '))

ventas = {}

for i in range(inicio, fin +1):
    ventas[i] = float(input('Introduce las ventas del año: ' + str(i) ": "))
    ventas = pd.Series(ventas)
    print('ventas \n', ventas)
    print('ventas con descuento \n', ventas *0.9)
