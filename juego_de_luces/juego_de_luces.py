#Juego de luces donde al eleccionar una se apagan/encienden las vecinas

import numpy as np

import emoji


cantidad = 10
luces = np.zeros(cantidad, dtype=np.uint8)

cuantas = np.random.randint(1, cantidad+1)
posiciones = np.random.choice(cantidad, size=cuantas, replace=False)

for posicion in posiciones:
    if posicion > 0:
        luces[posicion - 1] = 1-luces[posicion - 1]
    if posicion < cantidad - 1:
        luces[posicion + 1] = 1-luces[posicion + 1]
    luces[posicion] = 1-luces[posicion]

if luces.sum() == 0:
    luces[0] = 1
    luces[1] = 1


def mostrar_tablero():
    print("\nPosición:", end=" ")
    for i in range(luces.size):
        print(f"{i + 1:^2}", end=" ")

    print("\nEstado:  ", end=" ")
    for luz in luces:
        simbolo = emoji.emojize(
            ':red_circle:' if luz == 1 else ':black_circle:')
        print(f"{simbolo}", end=" ")

    print(f"\n{emoji.emojize(':red_circle:')} Encendida   {emoji.emojize(':black_circle:')} Apagada")


movimientos = 0

while luces.sum() > 0:
    mostrar_tablero()

    texto = input(f"\nElige una posición (1-{cantidad}) o 0 para salir: ")

    if not texto.isdigit():
        print("Escribe un número, por favor.")
        continue

    elegida = int(texto)

    if elegida == 0:
        print("Saliste del juego.")
        break

    if elegida < 1 or elegida > cantidad:
        print("Esa posición no existe.")
        continue

    posicion = elegida - 1

    if posicion > 0:
        luces[posicion - 1] = 1-luces[posicion - 1]
    if posicion < cantidad - 1:
        luces[posicion + 1] = 1-luces[posicion + 1]
    luces[posicion] = 1-luces[posicion]

    movimientos += 1

if luces.sum() == 0:
    mostrar_tablero()
    print(f"\n¡Ganaste! Apagaste todas las luces en {movimientos} movimientos.")
