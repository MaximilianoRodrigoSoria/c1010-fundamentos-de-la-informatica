def area_circulo(radio):
    pi = 3.14
    area = pi * radio**2
    return area

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area



print(f"Un circulo con radio 6  tiene un area de {area_circulo(6)} ")
print(f"Un rectangulo con una base de  6 y una altura de 10 tiene un area de {area_rectangulo(6,10)} ")
print(f"Un triangulo con una base de  6 y una altura de 10 tiene un area de {area_triangulo(6,10)} ")