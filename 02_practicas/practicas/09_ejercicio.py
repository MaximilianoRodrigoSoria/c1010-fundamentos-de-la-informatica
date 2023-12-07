alto = float(input("Ingrese el alto de la pileta en metros: "))
ancho = float(input("Ingrese el ancho de la pileta en metros: "))
largo = float(input("Ingrese el largo de la pileta en metros: "))

volumen = alto * ancho * largo

# Calcular la cantidad de litros (sabiendo que 1 metro cúbico es igual a 1000 litros)
litros = volumen * 1000

# Mostrar los resultados
print("El volumen de la pileta es: %.2f metros cúbicos."% volumen)
print("La cantidad de litros de agua que puede contener la pileta es: %2f litros."% litros)
