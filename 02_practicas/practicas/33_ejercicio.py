email = input("Ingrese su dirección de correo electrónico: ")

# Se puede usar una listata tambien
usuario, dominio = email.split('@')

print(f"Usuario: {usuario}")
print(f"Dominio: {dominio}")
