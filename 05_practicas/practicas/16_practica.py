def menu():
    print(f"[Menu de calculo de conversion]\n")
    print(f"[1.- Dolar\n")
    print(f"[2.- Euro\n")
    print(f"[3.- Real\n")

    opcion = int(input("Ingrese un numero de opcion: "))
    monto = int(input("Ingrese un monto: "))

    if(opcion == 1):
        convertir_dolar(monto)
    else:
        if(opcion == 2):
            convertir_euro(monto)
        else:
            if (opcion == 3):
                convertir_real(monto)
            else:
                print(f"La opcion {opcion} no es valida")



def convertir_dolar(monto):
    precio_dolar = 1100
    monto_obtenido = monto / precio_dolar
    print(f"La cantidad de dolares es {monto_obtenido:.2F}")

def convertir_euro(monto):
    precio_euro = 1400
    monto_obtenido = monto / precio_euro
    print(f"La cantidad de dolares es {monto_obtenido:.2F}")

def convertir_real(monto):
    precio_real = 900
    monto_obtenido = monto / precio_real
    print(f"La cantidad de dolares es {monto_obtenido:.2F}")



menu()
