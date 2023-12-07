def calculo_litros(alto, ancho, profundidad):
    litros = alto * ancho * profundidad * 1000
    return litros


print(f"Piscina de 12 x 5 x 2 tiene {calculo_litros(12, 5, 2):.2f} litros")
