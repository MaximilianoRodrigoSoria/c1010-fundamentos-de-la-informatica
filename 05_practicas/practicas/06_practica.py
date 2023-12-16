cant_nombres_con_a = 0
nombre = input("Ingrese un nombre: ")
while(nombre!='zzz'):
    if(nombre[0]== 'A'):
        cant_nombres_con_a += 1
    nombre = input("Ingrese un nombre: ")

print(f"La cantidad de nombres que comienzan con la letra \"A\" es {cant_nombres_con_a}")