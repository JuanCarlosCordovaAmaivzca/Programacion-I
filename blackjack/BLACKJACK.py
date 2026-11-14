import random


def calcular_puntuacion(mano):
    puntos = 0
    ases = 0

    for carta in mano:
        valor = carta[0]

        if valor == "A":
            puntos += 11
            ases += 1
        elif valor in ["J", "Q", "K"]:
            puntos += 10
        else:
            puntos += int(valor)

    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos


def crear_baraja():
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    pintas = ["♠", "♥", "♦", "♣"]
    baraja = [[valor, pinta] for valor in valores for pinta in pintas]
    random.shuffle(baraja)
    return baraja


# Pruebas de la función
mano1 = [["8", "♠"], ["K", "♥"]]
mano2 = [["A", "♦"], ["7", "♣"]]
mano3 = [["A", "♠"], ["9", "♥"], ["5", "♦"]]
mano4 = [["A", "♥"], ["A", "♣"], ["9", "♠"]]
mano5 = [["K", "♠"], ["Q", "♥"], ["5", "♦"]]

print("Pruebas de puntuación:")
print(calcular_puntuacion(mano1))
print(calcular_puntuacion(mano2))
print(calcular_puntuacion(mano3))
print(calcular_puntuacion(mano4))
print(calcular_puntuacion(mano5))
print("-" * 30)


####PARTE DE APUESTA Y CAPITAL COMO EL DE DADOS####
capital = 100
jugando = True

print("=== BIENVENIDO AL CASINO BLACKJACK WUUUUU ===")

while jugando and capital > 0:
    print(f"\nTu capital actual es: ${capital}")

    apuesta = 0
    while apuesta <= 0 or apuesta > capital:
        try:
            apuesta = int(input(f"¿Cuánto deseas apostar? (1 - {capital}): "))
            if apuesta <= 0 or apuesta > capital:
                print("Monto inválido. Ingresa una cantidad dentro de tu capital.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    baraja = crear_baraja()
    jugador = [baraja.pop(), baraja.pop()]
    crupier = [baraja.pop(), baraja.pop()]

    turno_activo = True

    while turno_activo:
        puntos_jugador = calcular_puntuacion(jugador)
        print("\nTus cartas actuales:")
        for carta in jugador:
            print(f"{carta[0]} de {carta[1]}")
        print(f"Tu puntuación actual es: {puntos_jugador}")

        if puntos_jugador > 21:
            print("¡Te has pasado de 21! Has perdido automáticamente.")
            capital -= apuesta
            turno_activo = False
            break
        elif puntos_jugador == 21:
            print("¡Tienes 21 puntos! Te plantas automáticamente.")
            turno_activo = False
            break

        opcion = input("¿Quieres pedir otra carta o plantarte? (pedir/plantar): ").strip().lower()

        if opcion in ["pedir", "p"]:
            nueva_carta = baraja.pop()
            jugador.append(nueva_carta)
            print(f"Has recibido: {nueva_carta[0]} de {nueva_carta[1]}")
        elif opcion in ["plantar", "plantarse", "pl"]:
            print(f"Te has plantado con {puntos_jugador} puntos.")
            turno_activo = False
        else:
            print("Opción no válida. Por favor, escribe 'pedir' o 'plantar'.")

    puntos_jugador = calcular_puntuacion(jugador)

    if puntos_jugador <= 21:
        puntos_crupier = calcular_puntuacion(crupier)
        while puntos_crupier < 17:
            crupier.append(baraja.pop())
            puntos_crupier = calcular_puntuacion(crupier)

        print(f"\nPuntuación del crupier: {puntos_crupier}")
        if puntos_crupier > 21 or puntos_jugador > puntos_crupier:
            print(f"¡Has ganado! Ganaste ${apuesta}.")
            capital += apuesta
        elif puntos_jugador < puntos_crupier:
            print(f"Has perdido ${apuesta}.")
            capital -= apuesta
        else:
            print("Empate. Recuperas tu apuesta.")

    if capital == 0:
        print("\n¡Te has quedado sin fichas! Fin del juego.")
        break

    respuesta = input("\n¿Deseas jugar otra ronda? (s/n): ").strip().lower()
    if respuesta not in ["s", "si", "sí", "y", "yes"]:
        jugando = False

print(f"\nJuego terminado. Te retiras con un capital final de: ${capital}")