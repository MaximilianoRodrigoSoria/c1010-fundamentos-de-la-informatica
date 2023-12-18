

def ingresar_productos():
    codigo = int(input("Ingrese un codigo: "))
    refrigeracion = input("\"R\"=requiere frío o \"N\"=no requiere frío: ")
    productos = []
    while(not(codigo == 999 and refrigeracion == "N")):
        nombre = input("Ingrese un nombre: ")
        descripcion = input("Ingrese un descripcion: ")
        precio = float(input("Ingrese un precio: "))
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        productos.append([codigo, refrigeracion, nombre, descripcion, precio,nombre_proveedor])
        codigo = int(input("Ingrese un codigo: "))
        refrigeracion = input("\"R\"=requiere frío o \"N\"=no requiere frío: ")
    return productos

def agregar_stock(productos):
    stock = []
    if(productos):
        for producto in productos:
            print(f"Este es el actual producto {producto} cuanta cantidad hay? ")
            cantidad = int(input("Cantidad: "))
            stock.append([producto, cantidad])
        return stock


def imprimir_R_N(productos):
    if(productos):
        refrigeracion = input("Ingrese \"R\"=requiere frío o \"N\"=no requiere frío para mostar por pantalla: ")
        if(refrigeracion=="R"):
            for producto in productos:
                if(producto[1]=="R"):
                    print(f"Producto refrigerado {producto}")
        else:
            for producto in productos:
                if (producto[1] == "N"):
                    print(f"Producto refrigerado {producto}")
    else:
        print("No hay productos")

def devolver_R_N(productos, refrigeracion):
    lista_productos = []
    if(productos):
        if(refrigeracion=="R"):
            for producto in productos:
                if(producto[1]=="R"):
                    lista_productos.append(producto)
        else:
            for producto in productos:
                if (producto[1] == "N"):
                    lista_productos.append(producto)
        return lista_productos
    else:
        return []


def cantidad_R_N(productos, refrigeracion):
    cont_r= 0
    cont_n=0
    for producto in productos:
        if(producto[1]==refrigeracion):
            cont_r+=1
        else:
            cont_n+=1
    if (refrigeracion=="R"):
        print(f"Cantidad de Productos refrigerado {cont_r}")
    else:
        print(f"Cantidad de Productos no refrigerado {cont_n}")


def stock_cero(stock):
    for item in stock:
        if(item[1] == 0):
            print(f"Código {item[0][0]}, nombre del artículo {item[0][2]}, y nombre del proveedor {item[0][5]}")


def imprimir_opciones():
    print(f"\n***Ingresar una opcion o (0 para salir)***\n")
    print(f"[0] Salir del menu")
    print(f"[1] Imprimir los datos de los artículos que necesitan o no refrigeración, dependiendo del valor ingresado por el usuario")
    print(f"[2] Imprimir la cantidad de artículos que precisan refrigeración")
    print(f"[3] Imprimir la cantidad de artículos que no requieren refrigeración")
    print(f"[4] Imprimir los datos de los artículos cuyo stock es 0")
    print(f"[5] Imprimir la información completa de los artículos que no requieren frío")
    print(f"[6] Cargar productos")
    print(f"[7] Cargar stock")
def menu():
    productos = []
    stock = []
    imprimir_opciones()
    opcion = int(input("Ingrese el numero de opcion: "))
    while(opcion != 0):
        if(opcion==1):
            imprimir_R_N(productos)
        else:
            if(opcion==2):
                cantidad_R_N(productos,"R")
            else:
                if(opcion==3):
                    cantidad_R_N(productos,"N")
                else:
                    if(opcion==4):
                        stock_cero(stock)
                    else:
                        if(opcion==5):
                            agregar_stock(devolver_R_N(productos, "N"))
                        else:
                            if(opcion==6):
                                productos = ingresar_productos()
                            else:
                                print("Opcion erronea")


        imprimir_opciones()
        opcion = int(input("Ingrese el numero de opcion: "))

menu()