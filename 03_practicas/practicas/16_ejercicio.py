def precio_con_iva(precio_sin_iva):
    precio_con_iva = precio_sin_iva * 1.21
    return precio_con_iva

print(f"Para un valor de 1254, el precio con iva es {precio_con_iva(1254):.2f}")
