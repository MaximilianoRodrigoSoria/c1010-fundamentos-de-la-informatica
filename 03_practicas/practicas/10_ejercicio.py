def calculo_transporte(salita1, salita2, salita3, asientos_por_micro):
    total_personas = (salita1+3) + (salita2+3) + (salita3+3)
    total_micros = total_personas/asientos_por_micro
    """
    rest0 = total_personas % asientos_por_micro
    if(resto > 0)
       { total_micros = total_micros + 1 }
    """
    return total_micros

print(f"Salita 1 = 50, Salita 2 = 20, Salita 3 = 30 y asientos por micros 50,  micros necesarios {calculo_transporte(50, 20, 30, 50):.0f}")