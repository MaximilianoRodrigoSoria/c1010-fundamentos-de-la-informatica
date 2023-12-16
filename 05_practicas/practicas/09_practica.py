cod_postal = int(input("Ingrese el codigo postal de su localidad: "))
while(cod_postal!=0):
    if(cod_postal == 1888):
        print(f"La localidad con el codigo postal {cod_postal} es \"y de Florencia Verela, el el Noba y te re suena!!!\"")
    else:
        if (cod_postal == 1900):
            print(f"La localidad con el codigo postal {cod_postal} es La Plata")
        else:
            print(f"La localidad con el codigo postal {cod_postal} es otra")

    cod_postal = int(input("\nIngrese el codigo postal de su localidad: "))
