import numpy as np

numRenglones = 7
numColumnas = 10

rng = np.random.default_rng(seed=10)
matriz = rng.integers(0, 2, size=(numRenglones, numColumnas), dtype=np.uint8)
print("Matriz original:")
print(matriz)

vecinos = np.zeros((numRenglones, numColumnas), dtype=np.uint8)

for i in range(1, numRenglones-1):
  for j in range(1, numColumnas-1):
    vecinos[i,j] = (matriz[i-1,j-1] + matriz[i-1,j] + matriz[i-1,j+1]
                  + matriz[i,j-1]                   + matriz[i,j+1]
                  + matriz[i+1,j-1] + matriz[i+1,j] + matriz[i+1,j+1])

i = 0
for j in range(1, numColumnas-1):
  vecinos[i,j] = (matriz[i,j-1] + matriz[i,j+1]
                + matriz[i+1,j-1] + matriz[i+1,j] + matriz[i+1,j+1])

i = numRenglones-1
for j in range(1, numColumnas-1):
  vecinos[i,j] = (matriz[i,j-1] + matriz[i,j+1]
                + matriz[i-1,j-1] + matriz[i-1,j] + matriz[i-1,j+1])

j = 0
for i in range(1, numRenglones-1):
  vecinos[i,j] = (matriz[i-1,j] + matriz[i-1,j+1]
                + matriz[i,j+1]
                + matriz[i+1,j] + matriz[i+1,j+1])

j = numColumnas-1
for i in range(1, numRenglones-1):
  vecinos[i,j] = (matriz[i-1,j-1] + matriz[i-1,j]
                + matriz[i,j-1]
                + matriz[i+1,j-1] + matriz[i+1,j])

vecinos[0,0] = matriz[0,1] + matriz[1,0] + matriz[1,1]
vecinos[0,numColumnas-1] = matriz[0,numColumnas-2] + matriz[1,numColumnas-2] + matriz[1,numColumnas-1]
vecinos[numRenglones-1,0] = matriz[numRenglones-2,0] + matriz[numRenglones-2,1] + matriz[numRenglones-1,1]
vecinos[numRenglones-1,numColumnas-1] = matriz[numRenglones-2,numColumnas-1] + matriz[numRenglones-2,numColumnas-2] + matriz[numRenglones-1,numColumnas-2]

print("Suma de vecinos:")
print(vecinos)