cant_numeros = int(input("Ingrese la cantidad de numeros: "))
sumatoria = 0
for i in range(1, cant_numeros + 1):
    numero = int(input("Ingresa un numero: "))
    sumatoria += numero

promedio = sumatoria/cant_numeros
print(f"\nEl promedio dio {promedio:.2f}")