<p align="center">
<a href="https://www.linkedin.com/in/soriamaximilianorodrigo/" target="_blank" rel="noopener noreferrer">
<img width="100%" height="100%" src="../docs/img/fundamentos.png" alt="Fundamentos"></a></p>


# Práctica 2 - Variables y tipos de datos


[📂 PDF PRACTICAS 2](docs/Practica%202.pdf)

[📂 PPTs](docs/Power%20Point%202%20-Variables%20y%20Tipos%20de%20datos.pdf)

## PARTE I: Aspectos Conceptuales

### Ejercicio 1
¿Qué efecto hace la instrucción `input()`? Si necesitas ingresar un número entero desde el teclado, ¿cómo lo harías?


#### Respuesta

> La sentencia input() sirve para ingresar valores por teaclado
>
>Para ingresar un entero, puedo usar la sentencia int para convertir la cadena ingresada en el input()
```python 
numero_int = int(input("Ingrese un número entero: "))
```


### Ejercicio 2
Define la diferencia entre una lista y una tupla. ¿En qué casos utilizarías cada una?

#### Respuesta

>Las listas son mutables, lo que significa que puedes modificar, agregar o eliminar elementos después de su creación.
>Se define con corchetes [] y se utiliza cuando necesitas una colección de elementos que pueda cambiar durante la ejecución del programa.

> #### Ejemplo:
```python 
mi_lista = [1, 2, 3]
```

Las Tuplas son inmutables, lo que significa que no puedes modificar sus elementos después de la creación.
Se define con paréntesis () ye utiliza cuando necesitas una colección de elementos que no cambiarán y quieres garantizar que los datos permanezcan constantes.

> ##### Ejemplo: 

```python
mi_tupla = (1, 2, 3)
```


>Utilizaría una lista cuando necesite una colección de elementos que puedas modificar, agregar o eliminar durante la ejecución del programa.
>
>Utilizaría una tupla cuando necesite una colección inmutable, por ejemplo, para representar un conjunto de valores constantes o inmutables.



## PARTE II: Trabajamos sobre los tipos de datos

### Numéricos

#### Ejercicio 3
Pedir que se ingrese un número e imprimir el triple.

### Respuesta
> [ejercicio3.py](practicas/03_ejercicio.py)


#### Ejercicio 4
Pedir que se ingrese un número e imprimir la mitad.

### Respuesta
> [ejercicio4.py](practicas/04_ejercicio.py)

#### Ejercicio 5
Pedir que se ingrese 3 notas e imprimir el promedio.

### Respuesta
> [ejercicio5.py](practicas/05_ejercicio.py)

#### Ejercicio 6
Pedir base y altura de un triángulo y mostrar el área del mismo.

### Respuesta
> [ejercicio6.py](practicas/06_ejercicio.py)

#### Ejercicio 7
Pedir el diámetro de un círculo y calcular su área y perímetro.

### Respuesta
> [ejercicio7.py](practicas/07_ejercicio.py)

#### Ejercicio 8
Pedir 2 números y mostrar la división entre ellos y el resto.

### Respuesta
> [ejercicio8.py](practicas/08_ejercicio.py)

#### Ejercicio 9
Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad de litros que tiene.

### Respuesta
> [ejercicio9.py](practicas/09_ejercicio.py)

#### Ejercicio 10
Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar. (son de 60x60 cm)


### Respuesta
> [ejercicio10.py](practicas/10_ejercicio.py)

#### Ejercicio 11
Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar cuánto se gasta por cada producto y el total.

### Respuesta
> [ejercicio11.py](practicas/11_ejercicio.py)

#### Ejercicio 12
Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros), muestre el valor de su perímetro y el de su área.

### Respuesta
> [ejercicio12.py](practicas/12_ejercicio.py)

### Cadenas de texto

#### Ejercicio 13
Pedir que se ingrese un nombre e imprimir un saludo.

### Respuesta
> [ejercicio13.py](practicas/13_ejercicio.py)

#### Ejercicio 14
Pedir tres palabras y mostrar un texto con las iniciales de las tres.

### Respuesta
> [ejercicio14.py](practicas/14_ejercicio.py)

#### Ejercicio 15
Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir).

### Respuesta
> [ejercicio15.py](practicas/15_ejercicio.py)

#### Ejercicio 16
Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse. Mostrar el siguiente mensaje.
> “La solicitud de inscripción a la comisión {comision} solicitada por el
alumno {apellido}, {nombre>} está siendo procesada”

### Respuesta
> [ejercicio16.py](practicas/16_ejercicio.py)

#### Ejercicio 17
Pedir cuatro datos, quién, qué hizo, cuándo y cómo. Mostrar la siguiente noticia.
> “Última noticia!, la persona xx, en el dia xx, hizo xx, de la siguiente manera xx”

### Respuesta
> [ejercicio17.py](practicas/17_ejercicio.py)

#### Ejercicio 18
Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una clave con esos datos y mostrarla.

### Respuesta
> [ejercicio18.py](practicas/18_ejercicio.py)

#### Ejercicio 19
Mostrar 5 veces la cadena “Hola”.

### Respuesta
> [ejercicio19.py](practicas/19_ejercicio.py)

### Listas y tuplas

#### Ejercicio 20
Ejecutar los siguientes códigos. ¿Cuál es el resultado de las siguientes ejecuciones? Justificar.
- a) `tupla=(1,True,['a','b','c'], "hola")`
- b) `tupla=(1,True,['a','b','c'], "hola")`



### Respuesta
> [ejercicio20.py](practicas/20_ejercicio.py)
> 
> En el caso a) da error porque se intenta modificar un valor existente de la tupla.
> 
> En el caso b) se ejecuta correctamente ya que se agrega un elemento nuevo

#### Ejercicio 21
Dada la siguiente estructura: `lista=[1,True,['a','b','c'], "hola"]`. Ejecutar las siguientes sentencias y describir los resultados.
- a) `print (lista[2])`
- b) `print (lista [4])`
- c) `lista.append (False) print (lista)`

> a) Se imprime ['a','b','c']
> 
> b) Error, el indice 4 no existe
> 
> c) Imprime [1, True, ['a', 'b', 'c'], 'hola', False]

### Respuesta
> [ejercicio21.py](practicas/21_ejercicio.py)

#### Ejercicio 22
`lista=[1,True,['a','b','c'], "hola"]`. Ejecutar y describir los resultados.
- `del lista[2]`
- `print (lista)`

### Respuesta
> [ejercicio22.py](practicas/22_ejercicio.py)
> 
> ### Respuesta
> 
> Se imprime [1, True, 'hola']


#### Ejercicio 23
Dada la siguiente información, elija una estructura de datos que permita guardarla adecuadamente.

- Guerra del Peloponeso 431 a.C
- Revolución de Mayo 1810 d.C
- Llegada de los españoles a América 1492 d.C
- Comienzo de la construcción de la gran Muralla China 214 a.C

### Respuesta
> [ejercicio23.py](practicas/23_ejercicio.py)
>
> Se utilizaria una tupla ya que los datos ingresados no variarian

## PARTE III Datos, Variables y Tipos de Datos

### Ejercicio 24
Escriba un programa que reciba un nombre ingresado por el usuario e imprima en la pantalla un saludo.

¿Hizo uso de variables? ¿Cuáles?
¿Hizo uso de valores? ¿Cuáles?
¿Hizo uso de operadores? ¿Cuáles?
¿Qué sentencias utilizó?

### Respuesta
> [ejercicio24.py](practicas/24_ejercicio.py)
>
> Use la variable nombre y concatene con format f {}, las sentencias están en el archivo ejercicio24.py

### Ejercicio 25
Escriba un programa que reciba un nombre y una edad ingresados por el usuario e imprima en la pantalla un texto con la información ingresada por el usuario.

¿Hizo uso de variables? ¿Cuáles?
¿Hizo uso de valores? ¿Cuáles?
¿Hizo uso de operadores? ¿Cuáles?
¿Qué sentencias utilizó?


### Respuesta
> [ejercicio25.py](practicas/25_ejercicio.py)
>
> Use las variables nombre y edad, las sentencias están en el archivo ejercicio25.py

### Ejercicio 26
Ejecute el siguiente código e indique, en cada caso, con qué valor finaliza la variable `x`. Justifique su respuesta.

a)
```python 
x= 10
X= x**2
print (x)
# Resultado 100
```

b)
```python 
x=30
x= x % 4
print(x)
# Resultado 2
```

c)
```python 
a= "4"
b= "3"
x= a + b
print (x)
# Resultado 43
```
d)
```python 
a= "4"
b= 3
x= a * b
print (x)
# Resultado 444
```
e)
```python 
a= 4
b= 3
x= "a" * b
print(x)
# Resultado aaa
```


### Respuesta
> [ejercicio26.py](practicas/26_ejercicio.py)


### Ejercicio 27
Ejecute el siguiente código y diga qué hace y qué elementos de programación se utilizan: variables, valores, operadores y sentencias.
- a) `print ('hola')`
- b) `print (2)`
- c) `nombre=input('Ingrese un nombre') print (nombre)`
- d) `edad=input('Ingrese la edad') print (edad)`
- e) `print (2*3)`
- f) `print (4%2)`
- g) `num1=input('Ingrese un número') num2=input('Ingrese otro número') print (num1+num2)`
- h) `num1=int(input('Ingrese un número')) num2=int(input('Ingrese otro número')) print (num1+num2)`


### Respuesta
> [ejercicio27.py](practicas/27_ejercicio.py)

> a) Imprime Hola
> 
> b) Imprime 2
> 
> c) Imprime el nombre ingresado
> 
> d) Imprime la edad ingresada
> 
> e) Imprime 6
> 
> f) Imprime el resto de la division 0
> 
> g) Imprime 23, concatena las variables
> 
> h) imprime 6, suma los numeros


### Ejercicio 28
Asígnele a las variables `num1` y `num2` los distintos valores indicados en la tabla. Realice las siguientes cuentas con las operaciones indicadas almacenando el resultado en la variable `resul`.
En la tabla que aparece a continuación coloque los resultados obtenidos y justifíquelo.

| Valor de `num1` | Valor de `num2` | Operación | Valor de `resul` | Justificación |
| --- | --- | --- | --- | --- |
| 5 | 2 | `//` | 2 | La división entera de 5 entre 2 es 2 |
| 7.2 | 9.8 | `*` | 70.56 | La multiplicación de 7.2 por 9.8 es 70.56 |
| 7 | 3.1 | `-` | 3.9 | La resta de 7 menos 3.1 es 3.9 |
| 10.45 | 7 | `+` | 17.45 | La suma de 10.45 y 7 es 17.45 |
| “republica ” | “argentina” | `+` | “republica argentina” | La concatenación de las cadenas es “republica argentina” |



### Respuesta
> [ejercicio28.py](practicas/28_ejercicio.py)


## PARTE IV: Aplicando funciones y métodos a los tipos de datos

### Ejercicio 29
Si se tienen las variables `n1=124.25` y `n2= “33.40”`, realizar las conversiones necesarias para saber la división entera entre ellos y el resto.


### Respuesta
> [ejercicio29.py](practicas/29_ejercicio.py)



### Ejercicio 30
Pedir 5 palabras y mostrar la cantidad de letras que tienen en total.



### Respuesta
> [ejercicio30.py](practicas/3_ejercicio.py)


### Ejercicio 31
Pedir el CUIT que tiene la siguiente forma xx/dni/x. Extraer y mostrar el DNI.


### Respuesta
> [ejercicio31.py](practicas/31_ejercicio.py)


### Ejercicio 32
Mostrar el código ASCII de los caracteres “A”, “a” y “0”.



### Respuesta
> [ejercicio32.py](practicas/32_ejercicio.py)


### Ejercicio 33
Pedir la cuenta de correo al usuario y mostrar por separado su usuario y su dominio.


### Respuesta
> [ejercicio33.py](practicas/33_ejercicio.py)
