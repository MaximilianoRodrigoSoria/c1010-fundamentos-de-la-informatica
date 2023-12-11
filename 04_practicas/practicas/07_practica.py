def determinar_categoria_altura(sexo, altura):
    if sexo.lower() == "femenino":
        if altura < 145:
            return "Petisa"
        elif 145 <= altura < 170:
            return "Normal"
        else:
            return "Alta"
    elif sexo.lower() == "masculino":
        if altura < 160:
            return "Petiso"
        elif 160 <= altura < 190:
            return "Normal"
        else:
            return "Alto"
    else:
        return "Sexo no válido"

# Solicitar el sexo y la altura
sexo = input("Ingrese el sexo (Femenino/Masculino): ")
altura = float(input("Ingrese la altura en centímetros: "))

# Determinar la categoría de altura
categoria_altura = determinar_categoria_altura(sexo, altura)

# Mostrar el resultado
print(f"La persona de sexo {sexo.capitalize()} y altura {altura} cm es de categoría: {categoria_altura}")
