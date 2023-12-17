# Parte a: Ingresar números hasta ingresar 0
def ingresar_numeros():
    numeros = []
    numero = float(input("Ingrese un número (0 para finalizar): "))

    while numero != 0:
        numeros.append(numero)
        numero = float(input("Ingrese un número (0 para finalizar): "))

    return numeros


# Parte b: Calcular el promedio de una lista de números
def calcular_promedio(lista_numeros):
    if not lista_numeros:
        return 0  # Evitar división por cero
    suma = calcular_suma(lista_numeros)
    promedio = suma / len(lista_numeros)
    return promedio


# Parte c: Calcular la suma de una lista de números
def calcular_suma(lista_numeros):
    if lista_numeros:
        sumatoria = 0
        for numero in lista_numeros:
            sumatoria += numero
        return sumatoria
    else:
        return None

# Parte d: Encontrar el número máximo en una lista
def encontrar_maximo(lista_numeros):
    if lista_numeros:
        maximo = lista_numeros[0]
        for numero in lista_numeros:
            if(numero > maximo):
                maximo = numero
        return maximo
    else:
        return None


# Parte e: Encontrar el número mínimo en una lista
def encontrar_minimo(lista_numeros):
    if lista_numeros:
        minimo = lista_numeros[0]
        for numero in lista_numeros:
            if(numero < minimo):
                minimo = numero
        return minimo
    else:
        return None


# Ejemplo de uso
numeros_ingresados = ingresar_numeros()
promedio = calcular_promedio(numeros_ingresados)
suma = calcular_suma(numeros_ingresados)
maximo = encontrar_maximo(numeros_ingresados)
minimo = encontrar_minimo(numeros_ingresados)

print(f"Lista de números ingresados: {numeros_ingresados}")
print(f"Promedio: {promedio}")
print(f"Suma: {suma}")
print(f"Número máximo: {maximo}")
print(f"Número mínimo: {minimo}")
