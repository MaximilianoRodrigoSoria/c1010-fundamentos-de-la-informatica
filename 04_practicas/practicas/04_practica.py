numero_dia = int(input("Ingrese un número del 1 al 7: "))
if 1 <= numero_dia <= 7:
    dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    print(f"Corresponde al día {dias_semana[numero_dia-1]}.")
else:
    print("Número no válido. Ingrese un número del 1 al 7.")