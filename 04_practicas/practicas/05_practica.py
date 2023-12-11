def determinar_transporte(cantidad_pasajeros):
    transporte = ""

    if cantidad_pasajeros == 1:
        transporte = "Bicicleta"
    elif cantidad_pasajeros <= 2:
        transporte = "Moto"
    elif cantidad_pasajeros <= 4:
        transporte = "Auto"
    elif cantidad_pasajeros <= 12:
        transporte = "Camioneta"
    elif cantidad_pasajeros <= 40:
        transporte = "Colectivo"
    else:
        transporte = "Avión"

    return transporte

# Solicitar la cantidad de personas a viajar
cantidad_personas = int(input("Ingrese la cantidad de personas a viajar: "))

# Determinar el medio de transporte
medio_transporte = determinar_transporte(cantidad_personas)

# Mostrar el resultado
print(f"Para {cantidad_personas} personas, el medio de transporte recomendado es: {medio_transporte}")
