def ingresar_equipos():
    equipos = []
    nombre_equipo = input("Ingrese el nombre del equipo o (ingrese 'ZZZ' para finalizar): ")

    while nombre_equipo != 'ZZZ':
        puntaje = int(input("Ingrese el puntaje en la tabla de posiciones: "))
        goles_a_favor = int(input("Ingrese la cantidad de goles a favor: "))

        # Agregar la información del equipo a la lista
        equipos.append([nombre_equipo, puntaje, goles_a_favor])

        # Solicitar el siguiente equipo
        nombre_equipo = input("Ingrese el nombre del equipo o (ingrese 'ZZZ' para finalizar): ")

    return equipos

def imprimir_goles_primero_ultimo(equipos):
    if equipos:
        # Obtener la cantidad de goles a favor del primer y último equipo
        goles_primero = equipos[0][2]
        goles_ultimo = equipos[-1][2]

        # Imprimir la información
        print(f"Goles a favor del primer equipo: {goles_primero}")
        print(f"Goles a favor del último equipo: {goles_ultimo}")
    else:
        print("La lista de equipos está vacía.")

def imprimir_campeon(equipos):
    if equipos:
        equipo_campeon = equipos[0]
        for equipo in equipos:
            if(equipo[1] == equipo_campeon[1]):
                if(equipo[2]>equipo_campeon[2]):
                    equipo_campeon = equipo
            else:
                if(equipo[1] > equipo_campeon[1]):
                    equipo_campeon = equipos
        print(f"El equipo campeon es: {equipo_campeon}")
    else:
        print("La lista de equipos está vacía.")


lista_equipos = ingresar_equipos()


imprimir_goles_primero_ultimo(lista_equipos)

imprimir_campeon(lista_equipos)