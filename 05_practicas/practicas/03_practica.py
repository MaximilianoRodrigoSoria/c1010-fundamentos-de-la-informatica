print("Tabla de Códigos ASCII (0-255):\n")
print("+------+------------+")
print("| Valor| Carácter   |")
print("+------+------------+")

for codigo in range(256):
    # Convertir el código ASCII a carácter
    caracter = chr(codigo)
    # Imprimir fila de la tabla
    print(f"| {codigo: <5}| {caracter: <10}|")

print("+------+------------+")


# El <10 autocompleta con espacios hasta contar 10 caracteres
# Realmente no es necesario, solo lo uso para que sea mas estetico
# print(f"| {codigo: <10}| {caracter: <10}|")