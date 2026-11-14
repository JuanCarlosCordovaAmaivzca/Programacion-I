ancho = 41
alto = 20

for fila in range(alto):
    for col in range(ancho):
        dibujar = False

        if fila < 10 and (col == 20 - fila * 2 or col == 20 + fila * 2):
            dibujar = True

        if fila == 10:
            dibujar = True

        if fila >= 10 and fila < 19 and (col == 0 or col == 40):
            dibujar = True

        if fila == 19:
            dibujar = True

        if (fila == 13 or fila == 16) and col >= 4 and col <= 10:
            dibujar = True
        if (col == 4 or col == 10) and fila >= 13 and fila <= 16:
            dibujar = True

        if (fila == 13 or fila == 16) and col >= 28 and col <= 34:
            dibujar = True
        if (col == 28 or col == 34) and fila >= 13 and fila <= 16:
            dibujar = True

        if fila == 15 and col >= 16 and col <= 24:
            dibujar = True
        if (col == 16 or col == 24) and fila >= 15 and fila <= 19:
            dibujar = True

        if fila == 5 and col == 25:
            dibujar = True
        if fila == 17 and col == 7:
            dibujar = True

        if dibujar:
            print("*", end="")
        else:
            print(" ", end="")

    print()
