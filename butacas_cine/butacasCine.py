import numpy as np


def leer_entero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))
            if minimo <= numero <= maximo:
                return numero
            print(f"Debes escribir un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Debes escribir un número entero.")


def mostrar(sala):
    filas, columnas = sala.shape
    print()
    print("PANTALLA".center(columnas * 4 + 9))
    print("         " + "".join(f"{c:>4}" for c in range(1, columnas + 1)))
    for f in range(filas):
        print(f"Fila {f + 1:>2}: " + "".join(f"{sala[f, c]:>4}" for c in range(columnas)))
    print("\nL: libre    X: ocupada    P: propuesta")


def buscar_lugar(sala, cantidad):
    filas, columnas = sala.shape
    for f in range(filas):
        for c in range(columnas - cantidad + 1):
            if np.all(sala[f, c:c + cantidad] == "L"):
                return f, c
    return None, None


def elegir_manual(sala, cantidad):
    filas, columnas = sala.shape
    while True:
        fila = leer_entero(f"Fila [1-{filas}] (0 para cancelar): ", 0, filas)
        if fila == 0:
            return None, None

        primera = leer_entero(f"Número de la primera butaca [1-{columnas}]: ", 1, columnas)
        f = fila - 1
        i = primera - 1

        if i + cantidad > columnas:
            ultima = columnas - cantidad + 1
            print(f"Error: desde la butaca {primera} no caben las {cantidad}.")
            print(f"La primera butaca posible en esa fila es la {ultima} o menor.")
            continue

        if np.any(sala[f, i:i + cantidad] != "L"):
            print("Hay butacas ocupadas en ese bloque. Elige otra.")
            continue

        return f, i


def proponer(sala):
    filas, columnas = sala.shape
    cantidad = leer_entero(f"¿Cuántas butacas necesitas? [1-{columnas}]: ", 1, columnas)

    f, i = buscar_lugar(sala, cantidad)
    if f is None:
        print("No hay suficientes butacas juntas en una misma fila.")
        return

    while True:
        vista = sala.copy()
        vista[f, i:i + cantidad] = "P"
        mostrar(vista)
        print(f"Propuesta: fila {f + 1}, butacas {i + 1} a {i + cantidad}.")

        respuesta = input("¿Aceptas esta propuesta? [s/n]: ").strip().lower()

        if respuesta == "s":
            sala[f, i:i + cantidad] = "X"
            print("¡Reservación realizada!")
            return

        if respuesta == "n":
            f, i = elegir_manual(sala, cantidad)
            if f is None:
                print("Operación cancelada.")
                return
        else:
            print("Escribe s o n.")


def pedir_butaca(sala):
    filas, columnas = sala.shape
    fila = leer_entero(f"Fila [1-{filas}]: ", 1, filas) - 1
    columna = leer_entero(f"Columna [1-{columnas}]: ", 1, columnas) - 1
    return fila, columna


def cancelar(sala):
    f, c = pedir_butaca(sala)
    if sala[f, c] == "L":
        print("La butaca ya está libre.")
    else:
        sala[f, c] = "L"
        print("Reservación cancelada.")


def disponibilidad(sala):
    filas = sala.shape[0]
    libres_por_fila = np.sum(sala == "L", axis=1)
    print()
    for f in range(filas):
        print(f"Fila {f + 1}: {libres_por_fila[f]} libres")
    print(f"\nTotal de butacas libres en la sala: {np.sum(sala == 'L')}")


def main():
    sala = np.full((10, 20), "L", dtype="<U1")

    while True:
        print("\n--- RESERVACIONES DEL CINE ---")
        print("1. Mostrar sala")
        print("2. Reservar butaca")
        print("3. Cancelar reservación")
        print("4. Consultar disponibilidad")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar(sala)
        elif opcion == "2":
            proponer(sala)
        elif opcion == "3":
            mostrar(sala)
            cancelar(sala)
        elif opcion == "4":
            disponibilidad(sala)
        elif opcion == "5":
            print("Programa terminado.")
            break
        else:
            print("Opción inválida.")


main()
