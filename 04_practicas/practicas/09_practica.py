def clasificar_caracter(caracter):
    # Obtener el valor ASCII del carácter
    ascii_valor = ord(caracter)

    # Verificar si es una letra
    if 65 <= ascii_valor <= 90 or 97 <= ascii_valor <= 122:
        return "Letra"
    # Verificar si es un dígito
    elif 48 <= ascii_valor <= 57:
        return "Dígito"
    # Verificar si es un carácter especial
    elif (32 <= ascii_valor <= 47) or (58 <= ascii_valor <= 64) or (91 <= ascii_valor <= 96) or (123 <= ascii_valor <= 126):
        return "Carácter especial"
    else:
        return "Otro tipo de carácter"

# Solicitar un carácter al usuario
caracter = input("Ingrese un carácter: ")

# Determinar la clasificación del carácter
clasificacion = clasificar_caracter(caracter)

# Mostrar el resultado
print(f"El carácter '{caracter}' es: {clasificacion}")