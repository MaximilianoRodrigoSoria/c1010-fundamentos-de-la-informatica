nombre_p1 = input("Ingresar nombre del producto: ")
precio_p1 = float(input("Ingresar precio del producto: "))
cantidad_p1 = float(input("Ingresar cantidad del producto: "))

nombre_p2 = input("Ingresar nombre del producto: ")
precio_p2 = float(input("Ingresar precio del producto: "))
cantidad_p2 = float(input("Ingresar cantidad del producto: "))

nombre_p3 = input("Ingresar nombre del producto: ")
precio_p3 = float(input("Ingresar precio del producto: "))
cantidad_p3 = float(input("Ingresar cantidad del producto: "))

nombre_p4 = input("Ingresar nombre del producto: ")
precio_p4 = float(input("Ingresar precio del producto: "))
cantidad_p4 = float(input("Ingresar cantidad del producto: "))

total_p1 = precio_p1 * cantidad_p1
total_p2 = precio_p2 * cantidad_p2
total_p3 = precio_p3 * cantidad_p3
total_p4 = precio_p4 * cantidad_p4

print(f"El producto {nombre_p1} tiene un precio de {precio_p1:.2f} y se compró un total de {cantidad_p1:.0f} artículos por {total_p1:.2f}")
print(f"El producto {nombre_p2} tiene un precio de {precio_p2:.2f} y se compró un total de {cantidad_p2:.0f} artículos por {total_p2:.2f}")
print(f"El producto {nombre_p3} tiene un precio de {precio_p3:.2f} y se compró un total de {cantidad_p3:.0f} artículos por {total_p3:.2f}")
print(f"El producto {nombre_p4} tiene un precio de {precio_p4:.2f} y se compró un total de {cantidad_p4:.0f} artículos por {total_p4:.2f}")

