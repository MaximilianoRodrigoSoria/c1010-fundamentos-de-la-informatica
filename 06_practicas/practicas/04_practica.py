def print_opciones():
    print(f"\n***Ingresar una opcion o (0 para salir)***\n")
    print(f"[1] Ingresar cursos")
    print(f"[2] Imprimir todos los cursos que tengan más de 5 clases")
    print(f"[3] Imprimir los cursos que se dictan en un día de la semana indicado por el usuario")
    print(f"[4] Imprimir el curso más intensivo (definido por la cantidad de clases y la duración de cada clase)")
    print(f"[5] Imprimir los datos en que se dicta un curso indicado por el usuario.")
    print(f"[6] Imprima todos los cursos que comienzan con una letra indicada por el usuario.")
def menu():
    print_opciones()
    cursos = []
    opcion = input("\nIngresar una opcion o (\"salir\" para finalizar): ")
    while(opcion!="salir"):
        if(opcion=="1"):
            cursos = ingresar_datos(cursos)
        else:
            if(opcion=="2"):
               imprimir_cursos_mas_cinco_clases(cursos)
            else:
                if(opcion == "3"):
                    imprimir_curso_por_dia(cursos)
                else:
                    if(opcion=="4"):
                        imprimir_curso_intensivo(cursos)
                    else:
                        if(opcion=="5"):
                            imprimir_datos(cursos)
                        else:
                            if(opcion=="6"):
                                imprimir_cursos_por_letra(cursos)
                            else:
                                print("Opcion no valida")
        print_opciones()
        opcion = input("\nIngresar una opcion o (\"salir\" para finalizar): ")

def ingresar_datos(cursos):
    nombre = input("Ingresar nombre o (\"salir\" para finalizar): ")
    while(nombre!="salir"):
        cant_clases = int(input("Ingresar cantidad de clases: "))
        dia = input("Ingresar dia cursada: ")
        hora_de_comienzo = input("Ingresar horario: ")
        duracion = int(input("Ingresar duracion (en minutos): "))
        if(duracion<=360):
            cursos.append([nombre, cant_clases, dia, hora_de_comienzo, duracion])
        nombre = input("Ingresar nombre o (\"salir\" para finalizar): ")
    return cursos

def imprimir_cursos_mas_cinco_clases(cursos):
    if(cursos):
        for curso in cursos:
            if(curso[1]>5):
                print(f"Este curso tiene mas de 5 clases {curso}")
    else:
        print("No hay cursos disponibles")

def imprimir_curso_por_dia(cursos):
    if(cursos):
        dia = input("Ingrese un dia (Lunes, Martes, etc...): ")
        print(f"Los cursos con el dia {dia}")
        for curso in cursos:
            if (curso[2] == dia):
                print(curso)
    else:
        print("No hay cursos disponibles")
def imprimir_curso_intensivo(cursos):
    if(cursos):
        intensivo = cursos[0]
        for curso in cursos:
            if(intensivo[1]==curso[1] and curso[4]> intensivo[4]):
                intensivo = curso
            else:
                if(curso[1]>intensivo[1]):
                    intensivo = curso
        print(f"El curso mas intensivo es {intensivo}")
    else:
        print("No hay cursos disponibles")

def imprimir_datos(cursos):
    print(cursos)

def imprimir_cursos_por_letra(cursos):
    if (cursos):
        letra = input("Ingresar una letra: ")
        for curso in cursos:
            if (curso[0][0] == letra):
                print(f"Este curso  {curso} tiene la letra {letra}")
    else:
        print("No hay cursos disponibles")

menu()