def calculo_nuevo_precio(precio_anterior, porcentaje_aumento):
    nuevo_precio = precio_anterior * (1 + porcentaje_aumento / 100)
    return nuevo_precio

print(f"El precio normal es 1000 y el procentaje de aumento es de 50, su rebaja fue de {calculo_nuevo_precio(1000, 50):.2f}")