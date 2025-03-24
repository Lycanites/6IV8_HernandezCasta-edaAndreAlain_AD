import pandas as pd
import matplotlib.pyplot as plt

#LLamamos al archivo Proyecto 1
df = pd.read_csv('proyecto1.csv')

#Sacamos la sumatoria de las Ventas totales con la variable: Vent_totales

Vent_totales = df["ventas_tot"].sum()

print("Cantidad de ventas totales $", Vent_totales)

#Conocer cuantos adeudos hay 

Deudor = df[df["B_adeudo"] == 'Con adeudo']
print('Con adeudo', Deudor)

