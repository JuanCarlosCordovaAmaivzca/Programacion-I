from IPython.display import display, HTML
import numpy as np

n = int(input("Altura (mitad) del reloj de arena = "))
filas = 2 * n - 1
columnas = 2 * n - 1
matriz = np.full((filas, columnas), ' ', dtype="U1")


matriz[0, :] = "*"
matriz[filas - 1, :] = "*"


for i in range(1, filas - 1):
    matriz[i, i] = "*"
    matriz[i, filas - 1 - i] = "*"


for fila in matriz:
    print("".join(fila))
