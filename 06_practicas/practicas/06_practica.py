def vocal_o_consonante(palabras):
    cont = 0
    consonantes = "bcdfghjklmnpqrstvwxyz"
    vocales = "aeiou"
    opcion = input("Ingresar busqueda por vocales \"v\" o por consonantes \"c\"\": ")
    if(opcion=="v"):
        for palabra in palabras:
            if (palabra[0].lower() in vocales):
                cont += 1
        print(f"La cantidad de vocales es {cont}")
    else:
        if(opcion=="c"):
            for palabra in palabras:
                if(palabra[0].lower() in consonantes):
                    cont += 1
            print(f"La cantidad de consonantes es {cont}")
        else:
            print(f"La opcion {opcion} no es valida")


def calcular_oraciones(texto):
    cont = 0
    oraciones = texto.split('.')
    for oracion in oraciones:
        #Limpiar oraciones vacias
        if(oracion):
            cont+=1
    return cont


def buscar_palabra(texto, busqueda):
    palabras = texto.split(' ')
    cont = 0
    for palabra in palabras:
        if(busqueda==palabra):
            cont+=1
    return cont

def contar_palabras_mayusculas(texto):
    palabras = texto.split()
    cont = 0
    for palabra in palabras:
        if(palabra[0].isupper()):
            cont += 1
    return cont

def contar_numeros(texto):
    cont = 0
    for caracter in texto:
        if(caracter in ["0","1","2","3","4","5","6","7","8","9"]):
            cont += 1
    return cont



def vocal_y_consonante(texto):
    cont_vocales = 0
    cont_consonantes = 0
    consonantes = "bcdfghjklmnpqrstvwxyz"
    vocales = "aeiou"
    palabras = texto.split(" ")
    for palabra in palabras:
        if (palabra[0].lower() in vocales):
            cont_vocales += 1
    for palabra in palabras:
        if(palabra[0].lower() in consonantes):
            cont_consonantes += 1
    print(f"La cantidad de palabras que comienzan en vocales es {cont_vocales}")
    print(f"La cantidad de palabras que comienzan en consonantes es {cont_consonantes}")


def palabras_infinitivo(texto):
    palabras = texto.split()
    infinitivos = []
    for palabra in palabras:
        if (palabra.lower().endswith(("ar", "er", "ir"))):
            infinitivos.append(palabra)

    print("Palabras que terminan en infinitivo:")
    for infinitivo in infinitivos:
        print(infinitivo)

texto = input("Ingresar texto: ")
palabras = texto.split(" ")
cant_oraciones = calcular_oraciones(texto)

print(f"La longitud del texto es {len(texto)}")
print(f"La cantidad de horaciones es {cant_oraciones}")
print(f"La cantidad de numeros dentro de la frase es {contar_numeros(texto)}")
vocal_y_consonante(texto)
palabra = input("Ingrese una palabra a buscar: ")
print(f"Cantidad de palasbra {palabra} cantidad {buscar_palabra(texto,palabra)}")
vocal_o_consonante(palabras)
print(f"La cantidad de palabras que comienzan con masyusculas {contar_palabras_mayusculas(texto)}")
palabras_infinitivo(texto)
