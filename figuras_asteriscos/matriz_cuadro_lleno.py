from IPython.display import display, HTML
import numpy as np
display(HTML("""
<h2 style="color:green">Triángulo rectángulo</h2>
"""))
n = 7
matriz = np.full((n, n), ' ', dtype="U1")

for fila in range(n):
    for columna in range(n):
        if columna <= fila:
            matriz[fila, columna] = "*"

# Mostrar la figura
for fila in matriz:
    print("".join(fila))