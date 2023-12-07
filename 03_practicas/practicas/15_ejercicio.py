def calculo_dosis(dias_tratamiento, veces_por_dia, comprimidos_por_envase):
    dosis_total = dias_tratamiento * veces_por_dia
    suficiente = dosis_total <= comprimidos_por_envase
    return suficiente

print(f"Con un tratamiento de 10 dias de 2 veces por dias y 4 comprimidos por envase el tratamiento es suficiente? {calculo_dosis(10, 2, 4)}")