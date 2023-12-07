#Error
tupla=(1,True,['a','b','c'], "hola")
tupla[1]=False
#OK
tupla=(1,True,['a','b','c'], "hola")
tupla[2][0]='b'
