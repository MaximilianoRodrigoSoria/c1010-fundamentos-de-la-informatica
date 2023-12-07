pi = 3.14

diametro = float(input("Ingrese el diámetro del círculo: "))

radio = diametro / 2

area = pi * (radio ** 2)

perimetro = 2 * pi * radio

print(f"El área del círculo es %.2f cm" % area)
print(f"El perímetro del círculo es %.2f cm" % perimetro)
