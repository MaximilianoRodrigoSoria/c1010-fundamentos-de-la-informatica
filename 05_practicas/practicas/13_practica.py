localidades = []

codigo_postal = int(input("Ingrese el codigo postal: "))
while(codigo_postal != 0):
    localidad = input("Ingrese el nombre de la localidad: ")
    localidades.append([localidad, codigo_postal])
    codigo_postal = int(input("Ingrese el codigo postal: "))

print(localidades)
