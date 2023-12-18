# a)
#Codigo Ascii de vocales
# a | 97
# e | 101
# i | 105
# o | 111
# u | 117

def cantidad_vocales(palabra):
    cantidad = 0
    for letra in palabra:
        codigo_ascii = ord(letra.lower())
        if codigo_ascii in [97, 101, 105, 111, 117]:
            cantidad += 1
    return cantidad

# b)
def ingreso_palabras():
    lista_palabras = []
    palabra = input("Ingrese una palabra o (ingrese \"fin\" para finalizar): ")
    while palabra != "fin":
        cantidad_vocales_palabra = cantidad_vocales(palabra)
        lista_palabras.append([palabra, cantidad_vocales_palabra])
        palabra = input("Ingrese una palabra o (ingrese \"fin\" para finalizar): ")
    return lista_palabras


# c)
def imprimir(palabras):
    for palabra in palabras:
        if(palabra[1]>3):
            print(palabra[0])

# d)
palabras = ingreso_palabras()

imprimir(palabras)



