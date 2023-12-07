nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dia_nacimiento = input("Ingrese el día de su nacimiento (en números): ")
mes_nacimiento = input("Ingrese el mes de su nacimiento (en números): ")
ano_nacimiento = input("Ingrese el año de su nacimiento: ")

clave = nombre[:3].lower() + apellido[:3].lower() + dia_nacimiento + mes_nacimiento + ano_nacimiento[-2:]

print(f"\nSu clave generada es: {clave}")

