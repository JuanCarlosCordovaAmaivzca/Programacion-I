#Cifrado cesar desplaza x cantidad de posiciones de letras en palabras

def rotar(letra, paso):
    if letra.islower():
        base = ord("a")
    else:
        base = ord("A")
    return chr((ord(letra) - base + paso) % 26 + base)


texto = input("Escribe tu texto: ")

paso = 0
while paso <= 0:
    try:
        paso = int(input("Pasos a recorrer (número mayor que cero): "))
        if paso <= 0:
            print("Error: el número debe ser mayor que cero.")
    except ValueError:
        print("Error: escribe un número entero.")

salida = []
for caracter in texto:
    if caracter.isalpha():
        salida.append(rotar(caracter, paso))
    else:
        salida.append(caracter)

print("Texto cifrado:", "".join(salida))
