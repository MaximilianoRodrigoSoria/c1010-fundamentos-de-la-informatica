numero = int(input("Ingrese un numero: "))

mitad = numero / 2

# De la mitad del número saco el resto de dividirlo por dos
if(mitad%2==0):
    print(f"La mitad de {numero} es par")
else:
    print(f"La mitad de {numero} es impar")