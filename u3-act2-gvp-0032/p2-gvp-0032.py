import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de juegos con 4 elementos por lista
mc = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]

# Creamos una lista de listas (conformando la tabla)
lista_juegos = [mc, gta, tet, wii, pub]
# print(lista_juegos)

# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
df_juegos = pd.DataFrame(lista_juegos, columns=["Nombre", "Cantidad", "Es_Multijugador", "Año"])
print(df_juegos)

# creamos el archivo CSV y lo guardamos en CSV
df_juegos.to_csv("juegos.csv", index=False)

# crear grafica de lineas
# donde x es nombre en el eje horizontal
# donde y es cantidad en el eje vertical
plt.plot(df_juegos["Nombre"], df_juegos["Cantidad"])
plt.title("Grafica juegos 0032")
plt.xlabel("Nombre de los juegos")
plt.ylabel("Copias vendidas (millones)")
plt.show()

# creamos una grafica de puntos
plt.scatter(df_juegos["Nombre"], df_juegos["Cantidad"])
plt.show()

# grafica de barras
plt.bar(df_juegos["Nombre"], df_juegos["Cantidad"])
# Etiquetas y titulo
plt.title("Juegos 0032")
plt.xlabel("Nombre de los juegos")
plt.ylabel("Copias vendidas (millones)")
# Mostrar la grafica
plt.show()

# ordenar grafica de barras de manera descendente
# de la mas grande a la mas pequeña
df_juegos_ordenar = df_juegos.sort_values("Cantidad", ascending=False)
plt.bar(df_juegos_ordenar["Nombre"], df_juegos_ordenar["Cantidad"])
plt.show()

# coloreando la grafica
plt.bar(df_juegos_ordenar["Nombre"], df_juegos_ordenar["Cantidad"],
        color=["b", "g", "c", "m", "y"])
plt.show()

# grafica de pastel
# plt.plot(df_juegos["Nombre"], df_juegos["Cantidad"])
plt.pie(df_juegos["Cantidad"], labels=df_juegos["Nombre"])
plt.show()