import pandas as pd
import matplotlib.pyplot as plt

#LLamamos a los archivos Proyecto 1 y Catalogo_Sucursal
df_ventas = pd.read_csv('proyecto1.csv')
df_sucursales = pd.read_csv("Catalogo_sucursal.csv")

#Sacamos la sumatoria de las Ventas totales con la variable: Vent_totales

Vent_totales = df_ventas["ventas_tot"].sum()

# Convertimos fechas al tipo de dato: datetime
df_ventas["B_mes"] = pd.to_datetime(df_ventas["B_mes"], format="%d/%m/%Y")

# Union con el catálogo de sucursales
df_ventas = df_ventas.merge(df_sucursales, on="id_sucursal", how="left")

#Conocer cuantos adeudos hay 
socios_con_adeudo = df_ventas[df_ventas["B_adeudo"] == "Con adeudo"]["no_clientes"].sum()
socios_sin_adeudo = df_ventas[df_ventas["B_adeudo"] == "Sin adeudo"]["no_clientes"].sum()
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100

# Gráfica de ventas totales respecto al tiempo
plt.figure(figsize=(10, 5))
plt.bar(df_ventas["B_mes"], df_ventas["ventas_tot"], color='Black')
plt.xticks(rotation=45)
plt.title("Ventas Totales a lo Largo del Tiempo")
plt.xlabel("Fecha")
plt.ylabel("Ventas Totales")
plt.show()

# Gráfica de desviación estándar de pagos respecto al tiempo
desviacion_std_pagos = df_ventas.groupby("B_mes")["pagos_tot"].std()
plt.figure(figsize=(10, 5))
desviacion_std_pagos.plot(kind="bar", color="skyblue")
plt.xticks(rotation=45)
plt.title("Desviación Estándar de Pagos por Mes")
plt.xlabel("Fecha")
plt.ylabel("Desviación Estándar de Pagos")
plt.show()

# Deuda total de los clientes
deuda_total = df_ventas["adeudo_actual"].sum()

# Porcentaje de utilidad respecto del adeudo
porcentaje_utilidad = ((Vent_totales - deuda_total) / Vent_totales) * 100

# Gráfico circular de ventas por sucursal
ventas_por_sucursal = df_ventas.groupby("suc")["ventas_tot"].sum()
plt.figure(figsize=(8, 8))
ventas_por_sucursal.plot.pie(autopct="%1.1f%%", cmap="viridis")
plt.title("Ventas por Sucursal")
plt.ylabel("")
plt.show()

# Gráfico de deudas totales por sucursal respecto del margen de utilidad
deuda_por_sucursal = df_ventas.groupby("suc")["adeudo_actual"].sum()
utilidad_por_sucursal = df_ventas.groupby("suc")["ventas_tot"].sum() - deuda_por_sucursal

fig, ax = plt.subplots(figsize=(10, 5))
width = 0.4
x = range(len(deuda_por_sucursal))
ax.bar(x, deuda_por_sucursal, width, label="Deuda Total", color="red")
ax.bar(x, utilidad_por_sucursal, width, bottom=deuda_por_sucursal, label="Utilidad", color="green")
ax.set_xticks(x)
ax.set_xticklabels(deuda_por_sucursal.index, rotation=45)
ax.set_ylabel("Monto")
ax.set_title("Deuda Total y Margen de Utilidad por Sucursal")
ax.legend()
plt.show()

# Mostrar métricas calculadas
print("Ventas Totales del Comercio:", Vent_totales)
print("Porcentaje de socios con adeudo:", porcentaje_con_adeudo, "%")
print("Porcentaje de socios sin adeudo:", porcentaje_sin_adeudo, "%")
print("Deuda total de los clientes:", deuda_total)
print("Porcentaje de utilidad respecto del adeudo:", porcentaje_utilidad, "%")
