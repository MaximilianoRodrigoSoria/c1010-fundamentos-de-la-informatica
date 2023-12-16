dni_menores = 0
dni = int(input("Ingrese un DNI: "))
while(dni!=999):
    if(dni < 20000000):
        dni_menores += 1
    dni = int(input("Ingrese un DNI: "))

print(f"\nLa cantidad de DNI menosres a 20000000 es de {dni_menores}")