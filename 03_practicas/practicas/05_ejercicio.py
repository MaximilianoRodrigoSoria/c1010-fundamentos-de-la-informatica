def cuantos_dias(numero_mes):
    meses = [
        ["enero", 31],
        ["febrero", 28],
        ["marzo", 31],
        ["abril", 30],
        ["mayo", 31],
        ["junio", 30],
        ["julio", 31],
        ["agosto", 31],
        ["septiembre", 30],
        ["octubre", 31],
        ["noviembre", 30],
        ["diciembre", 31]
    ]
    # El numero del mes -1 ya que, por ejemplo: Enero es la posicion 0, al ingresar 1 le resta 1 y queda 0
    return meses[numero_mes - 1][1]

print(cuantos_dias(2))