# Pedir al usuario que ingrese el CUIT
cuit = input("Ingrese el CUIT con el formato xx/dni/x: ")

# Dividir el CUIT en partes usando '/'
partes = cuit.split('/')

# Extraer y mostrar el DNI (segundo elemento en la lista)
dni = partes[1]
print(f"El DNI extraído del CUIT es: {dni}")
