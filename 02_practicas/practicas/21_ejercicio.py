lista=[1,True,['a','b','c'], "hola"]

# Imprime ['a', 'b', 'c']
print (lista[2])

#Eror el indice 4 no existe
print (lista [4])

#Imprime [1, True, ['a', 'b', 'c'], 'hola', False]
lista.append(False)
print (lista)