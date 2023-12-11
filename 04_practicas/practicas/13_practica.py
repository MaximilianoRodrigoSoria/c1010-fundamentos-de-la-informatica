def calcular_costo_llamada(duracion_segundos):
    costo_primer_minuto = 1.10
    costo_por_cuarto_minuto = 0.25

    if duracion_segundos <= 60:
        costo = costo_primer_minuto
    else:
        cantidad_cuartos = (duracion_segundos - 60) / 15
        costo = costo_primer_minuto + (cantidad_cuartos * costo_por_cuarto_minuto)

    return costo

# Solicitar la duración de la llamada en segundos al usuario
duracion_llamada = int(input("Ingrese la duración de la llamada en segundos: "))

# Calcular y mostrar el costo de la llamada
costo_llamada = calcular_costo_llamada(duracion_llamada)
print(f"El costo de la llamada es: ${costo_llamada:.2f}")
