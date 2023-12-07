def convertir_a_dolar(monto_pesos, precio_dolar):

    tasa_cambio_dolar = precio_dolar
    monto_dolar = monto_pesos / tasa_cambio_dolar
    return monto_dolar


print(f"Para 1000 pesos puede comprar {convertir_a_dolar(1000, 2000)} dolares")