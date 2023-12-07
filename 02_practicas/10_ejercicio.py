ancho_terreno = float(input("Ingrese el ancho del terreno en metros: "))
largo_terreno = float(input("Ingrese el largo del terreno en metros: "))


area_terreno = ancho_terreno * largo_terreno

# Dimensiones de un panel de pasto en metros
ancho_panel = 0.6  # 60 cm convertidos a metros
largo_panel = 0.6  # 60 cm convertidos a metros

# Calcular el área de un panel de pasto
area_panel = ancho_panel * largo_panel

# Calcular la cantidad de paneles de pasto necesarios
cantidad_paneles = area_terreno / area_panel


print("El área total del terreno es: %.2f metros cuadrados." % ancho_terreno)
print("Se necesitan %.0f paneles de pasto (60x60 cm) para cubrir el terreno." % cantidad_paneles)
