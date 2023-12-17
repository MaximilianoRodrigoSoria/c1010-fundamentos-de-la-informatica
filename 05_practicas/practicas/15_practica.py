def menu():
    print(f"[Menu de calculo de area]\n")
    print(f"[1.- Círculo\n")
    print(f"[2.- Cuadrado\n")
    print(f"[3.- Rectángulo\n")

    opcion = int(input("Ingrese un numero de opcion: "))

    if(opcion == 1):
        area_circulo()
    else:
        if(opcion == 2):
            area_cuadrado()
        else:
            if (opcion == 3):
                area_rectangulo()
            else:
                print(f"La opcion {opcion} no es valida")



def area_circulo():
    pi = 3.14
    radio = int(input("Ingrese el radio del circulo: "))
    area = pi * (radio * radio)
    print(f"Calculo de area de circulo dio {area:.2F}")

def area_cuadrado():
    lado = int(input("Ingrese el lado del cuadrado: "))
    area = lado * lado
    print(f"Calculo de area de un cuadrado dio {area:.2F}")

def area_rectangulo():
    base = int(input("Ingrese la base del rectangulo: "))
    altura = int(input("Ingrese la altura del rectangulo: "))
    area = base * altura
    print(f"Calculo de area de un rectangulo dio {area:.2F}")



menu()