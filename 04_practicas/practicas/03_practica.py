n = int(input("Ingrese el primer número (n): "))
m = int(input("Ingrese el segundo número (m): "))
if m % n == 0:
    print(f"{m} es divisible por {n}.")
else:
    print(f"{m} no es divisible por {n}.")