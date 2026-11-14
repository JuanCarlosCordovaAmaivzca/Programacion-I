#versión2
import numpy as np

# Cada número aparece exactamente dos veces
numParejas = 5
baraja = np.zeros(numParejas*2, np.int8)

baraja[::2] = np.arange(1, numParejas+1)
baraja[1::2] = np.arange(1, numParejas+1)

print(f"Inicializadas {baraja}")
np.random.shuffle(baraja)
print(f"Desordenadas: {baraja}")

descubiertas = np.zeros(numParejas*2, np.int8)
parejas_encontradas = 0
intentos = 0

while parejas_encontradas < numParejas:
    print("\nPosición:", end=" ")
    for i in range(baraja.size):
        print(f"{i + 1:^3}", end=" ")
    print("\nCarta:   ", end=" ")
    for i in range(baraja.size):
        if descubiertas[i] == 1:
            print(f"{baraja[i]:^3}", end=" ")
        else:
            print(f"{'*':^3}", end=" ")
    print()

    texto1 = input("Primera posición: ")
    texto2 = input("Segunda posición: ")

    if not texto1.isdigit() or not texto2.isdigit():
        print("Escribe solo números.")
        continue

    p1 = int(texto1) - 1
    p2 = int(texto2) - 1

    if p1 < 0 or p1 >= baraja.size or p2 < 0 or p2 >= baraja.size:
        print("Posición fuera del tablero.")
        continue

    if p1 == p2:
        print("Elige dos posiciones distintas.")
        continue

    if descubiertas[p1] == 1 or descubiertas[p2] == 1:
        print("Una de esas cartas ya está descubierta.")
        continue

    intentos += 1
    print(f"Carta {p1 + 1}: {baraja[p1]}   Carta {p2 + 1}: {baraja[p2]}")

    if baraja[p1] == baraja[p2]:
        print("¡Pareja encontrada!")
        descubiertas[p1] = 1
        descubiertas[p2] = 1
        parejas_encontradas += 1
    else:
        print("No son iguales, memoriza las posiciones.")

print(f"\n¡Ganaste! Encontraste todas las parejas en {intentos} intentos.")

# Conjunto universo
U = np.arange(1, 11)  # Del 1 al 10

# Conjuntos representados mediante arreglos
A = np.array([1, 2, 3, 4, 5, 3])
B = np.array([4, 5, 6, 7])

A = np.unique(A)
B = np.unique(B)


#Version1: con ciclos
# Reservar espacio suficiente para todos los elementos
union = np.empty(A.size + B.size, dtype=A.dtype)
cantidad = 0

for conjunto in (A, B):
    for elemento in conjunto:
        encontrado = False

        for i in range(cantidad):
            if union[i] == elemento:
                encontrado = True
                break

        if not encontrado:
            union[cantidad] = elemento
            cantidad += 1

# Conservar únicamente las posiciones utilizadas
union = union[:cantidad].copy()

print("Unión:", union)

#versión1 con ciclos
import numpy as np

A = np.array([1, 2, 3, 4, 5])
B = np.array([4, 5, 6, 7])

# La intersección no puede superar el tamaño del arreglo menor
interseccion = np.empty(min(A.size, B.size), dtype=A.dtype)
cantidad = 0

for elemento in A:
    # Buscar el elemento en B
    pertenece_B = False

    for otro in B:
        if elemento == otro:
            pertenece_B = True
            break

    if pertenece_B:
        # Verificar que no esté ya en el resultado
        repetido = False

        for i in range(cantidad):
            if interseccion[i] == elemento:
                repetido = True
                break

        if not repetido:
            interseccion[cantidad] = elemento
            cantidad += 1

interseccion = interseccion[:cantidad].copy()

print("Intersección:", interseccion)
# Intersección: [4 5]

#Version1: con ciclos
import numpy as np

U = np.arange(1, 11)
A = np.array([1, 2, 3, 4, 5])

complemento = np.empty(U.size, dtype=U.dtype)
cantidad = 0

for elemento in U:
    pertenece_A = False

    for otro in A:
        if elemento == otro:
            pertenece_A = True
            break

    if not pertenece_A:
        complemento[cantidad] = elemento
        cantidad += 1

# Conservar únicamente las posiciones utilizadas
complemento = complemento[:cantidad].copy()

print("Complemento de A:", complemento)
# Complemento de A: [ 6  7  8  9 10]

#verión1
import numpy as np

A = np.array([1, 2, 3, 4, 5])
B = np.array([4, 5, 6, 7])

diferencia = np.empty(A.size, dtype=A.dtype)
cantidad = 0

for elemento in A:
    pertenece_B = False

    for otro in B:
        if elemento == otro:
            pertenece_B = True
            break

    if not pertenece_B:
        # Evitar duplicados en el resultado
        repetido = False

        for i in range(cantidad):
            if diferencia[i] == elemento:
                repetido = True
                break

        if not repetido:
            diferencia[cantidad] = elemento
            cantidad += 1

diferencia = diferencia[:cantidad].copy()

print("A - B:", diferencia)
# A - B: [1 2 3]

#versión1
import numpy as np

A = np.array([1, 2, 3, 4, 5])
B = np.array([4, 5, 6, 7])

diferencia_simetrica = np.empty(
    A.size + B.size, dtype=np.result_type(A.dtype, B.dtype)
)
cantidad = 0

# Primero buscar elementos de A que no estén en B;
# después, elementos de B que no estén en A.
for origen, otro_conjunto in ((A, B), (B, A)):
    for elemento in origen:
        pertenece_otro = False

        for otro in otro_conjunto:
            if elemento == otro:
                pertenece_otro = True
                break

        if not pertenece_otro:
            repetido = False

            for i in range(cantidad):
                if diferencia_simetrica[i] == elemento:
                    repetido = True
                    break

            if not repetido:
                diferencia_simetrica[cantidad] = elemento
                cantidad += 1

diferencia_simetrica = diferencia_simetrica[:cantidad].copy()

print("Diferencia simétrica:", diferencia_simetrica)
# Diferencia simétrica: [1 2 3 6 7]

print(A.dtype, B.dtype)
dtype=np.result_type(A.dtype, B.dtype)
print(dtype)

print(np.isin(B, A))
# [ True  True False False]