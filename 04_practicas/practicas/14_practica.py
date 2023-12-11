def calcular_pulsaciones(sexo, edad):
    if sexo.lower() == "femenino":
        pulsaciones = (220 - edad) / 10
    elif sexo.lower() == "masculino":
        pulsaciones = (210 - edad) / 10
    else:
        return "Sexo no válido"

    return pulsaciones

# Solicitar el sexo y la edad al usuario
sexo = input("Ingrese el sexo (Femenino/Masculino): ")
edad = int(input("Ingrese la edad: "))

# Calcular y mostrar el número de pulsaciones
pulsaciones = calcular_pulsaciones(sexo, edad)

print(f"El número de pulsaciones por cada 10 segundos es: {pulsaciones:.2f}")
