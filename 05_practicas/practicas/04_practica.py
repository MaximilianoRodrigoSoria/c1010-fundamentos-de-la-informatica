print(f"Ingrese letras desde el teclado. Para finalizar, escriba 'fin'.\n")

letra = input("Ingrese una letra (o 'fin' para terminar): ")

while(letra != 'fin'):
    codigo = ord(letra)
    print(f"El codigo de la letra \"{letra}\" es {codigo}\n")
    letra = input("Ingrese una letra (o 'fin' para terminar): ")

print(f"\nEl programa ha sido finalizado.")