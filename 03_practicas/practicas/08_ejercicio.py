def calculo_rebaja(precio_anterior, precio_rebajado):

    porcentaje_rebaja = ((precio_anterior - precio_rebajado) / precio_anterior) * 100
    return porcentaje_rebaja


print(f"El precio normal es 356 y el rebajado es de 50, su rebaja fue de {calculo_rebaja(356, 50):.2f}%")