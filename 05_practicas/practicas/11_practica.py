def mostrar_multiplos(n, m):
    # Calcular el límite superior del rango (m - n), cuantas veces debe repetir
    limite_superior = m - n

    # Mostrar los múltiplos de n en el rango [n, m]
    print(f"Múltiplos de {n} en el rango [{n}, {m}]:")
    for i in range(limite_superior + 1):
        multiplo = n + i
        if multiplo % n == 0:
            print(multiplo)


# Ejemplo de uso
n = int(input("Ingresa un numero : "))
m = int(input("Ingresa un numero : "))

# Verificar que n sea menor o igual a m
if n > m:
  print(f"El valor de {n} debe ser menor o igual a {m}.")
else:
  mostrar_multiplos(n, m)