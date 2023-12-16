numero = int(input("Ingrese un numero: "))
sumatoria = 0
# 0 no suma, por eso arranca en 1
# Se le suma 1 al numero para que se contemple en numero dentro de sumatoria
for i in range(1, numero + 1):
   sumatoria = sumatoria + i

print(f"La sumatoria del numer {numero} es {sumatoria}")


