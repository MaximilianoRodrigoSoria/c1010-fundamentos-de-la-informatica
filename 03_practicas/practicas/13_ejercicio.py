def a_pagar(cantidad_personas, gasto_bebida, gasto_comida, alquiler_lugar):
    total_gastos = gasto_bebida + gasto_comida + alquiler_lugar
    monto_individual = total_gastos / cantidad_personas
    return monto_individual

print(f"Siendo 4 pesosnas con bebidas x 150, comida x200 y alquiler x5000 el gasto por persona es de {a_pagar(4, 150, 200, 500):.2f}")