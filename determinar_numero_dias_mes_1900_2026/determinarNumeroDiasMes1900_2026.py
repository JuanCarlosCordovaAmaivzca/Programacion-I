anio = int(input("Ingrese el año (mayor a 1582): "))
mes = int(input("Ingrese el mes (1 al 12): "))
dia = int(input("Ingrese el día: "))


a = (14 - mes) // 12
b = anio - a
c = mes + (12 * a) - 2


indicador = dia + b + (b // 4) - (b // 100) + (b // 400) + (31 * c) // 12

resultado = indicador % 7

if resultado == 0:
    print("El día es Domingo")
elif resultado == 1:
    print("El día es Lunes")
elif resultado == 2:
    print("El día es Martes")
elif resultado == 3:
    print("El día es Miércoles")
elif resultado == 4:
    print("El día es Jueves")
elif resultado == 5:
    print("El día es Viernes")
else:
    print("El día es Sábado")