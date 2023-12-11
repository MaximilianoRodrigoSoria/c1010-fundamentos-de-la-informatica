def clasificar_letra(caracter):
    if 'A' <= caracter <= 'Z':
        return "Es una MAYÚSCULA"
    elif 'a' <= caracter <= 'z':
        return "Es una MINÚSCULA"

# Solicitar un carácter al usuario
caracter = input("Ingrese un carácter: ")

# Verificar y mostrar el resultado
resultado = clasificar_letra(caracter)
if resultado:
    print(resultado)

