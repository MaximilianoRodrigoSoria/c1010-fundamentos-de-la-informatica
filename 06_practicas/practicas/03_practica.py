
def ingreso_legajos():
    legajo = int(input("Ingrese un numero de lagajo o (digite 0 para salir): "))
    legajos =[]
    while(legajo!=0):
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese un apellido: ")
        contraseña = input("Ingrese un contraseña: ")
        legajos.append([legajo,nombre,apellido,contraseña])
        legajo = int(input("Ingrese un numero de lagajo o (digite 0 para salir): "))
    return legajos


def imprimir_alumno(legajos):
    for legajo in legajos:
        print(f"\nLEGAJO: {legajo[0]}")
        print(f"NOMBRE: {legajo[1]}")
        print(f"APELLIDO: {legajo[2]}")
        print(f"CONTRASEÑA: {legajo[3]}")


def legajo_menor(legajos):
    if(legajos):
        menor = legajos[0]
        for legajo in legajos:
            if(legajo[0]< menor[0]):
                menor = legajo
        return menor
    else:
        return []


def nombre_mas_largo(legajos):
    if (legajos):
        mayor = legajos[0]
        for legajo in legajos:
            if(len(legajo[1]) > len(mayor[1])):
                mayor = legajo
        return mayor
    else:
        return []


def controlar_clave(legajos):
    for legajo in legajos:
        if(len(legajo[3])> 6 and legajo[3][-1] in ["1","2","3","4","5","6","7","8","9","0"]):
            print(f"El legajo {legajo} posee una contraseña correcta")
        else:
            print(f"El legajo {legajo[0]} no tiene una contraseña segura")

def menu():
    print(f"\n***Ingresar una opcion o (0 para salir)***\n")
    print(f"[1] Imprimir los datos de todos los alumnos")
    print(f"[2] Imprimir los datos del alumno que tiene el legajo más chico")
    print(f"[3] Imprimir los datos del alumno que tiene el nombre más largo")
    print(f"[4] Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número")
    print(f"[5] Ingresar legajos")
    legajos = []
    opcion = int(input("\nIngresar una opcion: "))
    while(opcion!=0):
        if(opcion==1):
            imprimir_alumno(legajos)
        else:
            if(opcion==2):
                print(f"El legajo mas chico es {legajo_menor(legajos)}")
            else:
                if(opcion == 3):
                    print(f"Legajo con nombre mas largo {nombre_mas_largo(legajos)}")
                else:
                    if(opcion==4):
                        controlar_clave(legajos)
                    else:
                        if(opcion==5):
                            legajos = ingreso_legajos()
                        else:
                            print("Opcion no valida")
        opcion = int(input("\nIngresar una opcion: "))

menu()