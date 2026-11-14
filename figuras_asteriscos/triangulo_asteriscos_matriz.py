from IPython.display import display, HTML
import numpy as np
import numpy as np
n = int(input("altura del triángulo="))
matriz = np.full((n, 2*n-1), ' ', dtype="U1")

for i in range(n):
    for j in range( n-i-1, n-i-1+2*i+1 ):
            matriz[i, j] = "*"
            
          
print(matriz)