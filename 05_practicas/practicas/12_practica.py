lista = [1, 14, 56, 43, 23, 46, 58, 123, 67]
#El maximo es el primer valor de la lista
maximo = lista[0]

for i in lista:
    # Si el valir i, es mayor a maximo se convierte en maximo
    if(i > maximo):
        maximo = i

print(f"El elemento de la lista con el valor maximo es {maximo}")