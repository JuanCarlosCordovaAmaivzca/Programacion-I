import string


def evaluar_contrasena(contrasena):
    observaciones = []

    if len(contrasena) < 10:
        observaciones.append(
            f"La contraseña tiene {len(contrasena)} caracteres; se requieren al menos 10."
        )
    if not any(c in string.punctuation for c in contrasena):
        observaciones.append(
            "La contraseña no contiene ningún carácter especial (por ejemplo: !@#$%&*)."
        )
    if not any(c.isdigit() for c in contrasena):
        observaciones.append("La contraseña no contiene ningún dígito numérico.")
    if not any(c.islower() for c in contrasena):
        observaciones.append("La contraseña no contiene ninguna letra minúscula.")
    if not any(c.isupper() for c in contrasena):
        observaciones.append("La contraseña no contiene ninguna letra mayúscula.")

    return observaciones


def presentar_requisitos():
    print("Validador de contraseñas")
    print("-" * 24)
    print("Requisitos de seguridad:")
    print("  - Mínimo 10 caracteres.")
    print("  - Al menos una letra mayúscula.")
    print("  - Al menos una letra minúscula.")
    print("  - Al menos un dígito numérico.")
    print("  - Al menos un carácter especial.")
    print()


def main():
    presentar_requisitos()
    contrasena = input("Ingrese la contraseña a evaluar: ")

    if contrasena.strip() == "":
        print("Error: no se ingresó ninguna contraseña.")
        return

    observaciones = evaluar_contrasena(contrasena)

    if not observaciones:
        print("Resultado: la contraseña cumple con todos los requisitos de seguridad.")
    else:
        print("Resultado: la contraseña no cumple con los requisitos de seguridad.")
        print("Observaciones:")
        for observacion in observaciones:
            print(f"  - {observacion}")


main()