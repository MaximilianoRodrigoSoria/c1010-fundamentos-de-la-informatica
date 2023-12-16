patente = input("Ingrese la patente: ")
while(patente!= 'AAA'):

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    if(patente[0]=='R' or patente[0]=='S' or patente[0]=='T'):
        print(f"{nombre} {apellido} con patente {patente} no debe pagar impuesto")
    else:
        print(f"{nombre} {apellido} con patente {patente} debe pagar impuesto")

    patente = input("Ingrese la patente: ")