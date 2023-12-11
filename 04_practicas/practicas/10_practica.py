def es_triangulo(lado1, lado2, lado3):
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
        return True
    else:
        return False

# Solicitar las longitudes de los lados al usuario
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Determinar si se forma un triángulo
if es_triangulo(lado1, lado2, lado3):
    print("Con estas longitudes, se forma un triángulo.")
else:
    print("Con estas longitudes, no se forma un triángulo.")
