def determinar_categoria_edad(anio_nacimiento):
    edad = 2023 - anio_nacimiento

    if edad < 2:
        return "Bebé"
    elif edad <= 12:
        return "Menor"
    elif edad <= 18:
        return "Adolescente"
    elif edad <= 45:
        return "Adulto"
    elif edad <= 60:
        return "Veterano"
    else:
        return "Abuelo"

# Solicitar el año de nacimiento
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))

# Determinar la categoría de edad
categoria_edad = determinar_categoria_edad(anio_nacimiento)

# Mostrar el resultado
print(f"La persona nacida en {anio_nacimiento} pertenece a la categoría de {categoria_edad}.")
