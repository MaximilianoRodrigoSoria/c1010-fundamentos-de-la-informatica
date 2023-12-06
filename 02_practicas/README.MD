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

#### Ejercicio 4
Pedir que se ingrese un número e imprimir la mitad.

#### Ejercicio 5
Pedir que se ingrese 3 notas e imprimir el promedio.

#### Ejercicio 6
Pedir base y altura de un triángulo y mostrar el área del mismo.

#### Ejercicio 7
Pedir el diámetro de un círculo y calcular su área y perímetro.

#### Ejercicio 8
Pedir 2 números y mostrar la división entre ellos y el resto.

#### Ejercicio 9
Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad de litros que tiene.

#### Ejercicio 10
Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar.

#### Ejercicio 11
Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar cuánto se gasta por cada producto y el total.

#### Ejercicio 12
Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros), muestre el valor de su perímetro y el de su área.

### Cadenas de texto

#### Ejercicio 13
Pedir que se ingrese un nombre e imprimir un saludo.

#### Ejercicio 14
Pedir tres palabras y mostrar un texto con las iniciales de las tres.

#### Ejercicio 15
Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir).

#### Ejercicio 16
Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse. Mostrar el siguiente mensaje.

#### Ejercicio 17
Pedir cuatro datos, quién, qué hizo, cuándo y cómo. Mostrar la siguiente noticia.

#### Ejercicio 18
Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una clave con esos datos y mostrarla.

#### Ejercicio 19
Mostrar 5 veces la cadena “Hola”.

### Listas y tuplas

#### Ejercicio 20
Ejecutar los siguientes códigos. ¿Cuál es el resultado de las siguientes ejecuciones? Justificar.
- a) `tupla=(1,True,['a','b','c'], "hola")`
- b) `tupla=(1,True,['a','b','c'], "hola")`

#### Ejercicio 21
Dada la siguiente estructura: `lista=[1,True,['a','b','c'], "hola"]`. Ejecutar las siguientes sentencias y describir los resultados.
- a) `print (lista[2])`
- b) `print (lista [4])`
- c) `lista.append (False) print (lista)`

#### Ejercicio 22
`lista=[1,True,['a','b','c'], "hola"]`. Ejecutar y describir los resultados.
- `del lista[2]`
- `print (lista)`

#### Ejercicio 23
Dada la siguiente información, elija una estructura de datos que permita guardarla adecuadamente.

- Guerra del Peloponeso 431 a.C
- Revolución de Mayo 1810 d.C
- Llegada de los españoles a América 1492 d.C
- Comienzo de la construcción de la gran Muralla China 214 a.C

## PARTE III Datos, Variables y Tipos de Datos

### Ejercicio 24
Escriba un programa que reciba un nombre ingresado por el usuario e imprima en la pantalla un saludo.

### Ejercicio 25
Escriba un programa que reciba un nombre y una edad ingresado por el usuario e imprima en la pantalla un texto con la información ingresada por el usuario.

### Ejercicio 26
Ejecute el siguiente código e indique, en cada caso, con qué valor finaliza la variable `x`. Justifique su respuesta.
- a) `x= 10 X= x**2 print (x)`
- b) `x=30 # x= x % 4 print (x)`
- c) `a= “4” b= “3” x= a + b

print (x)`
- d) `a= “4” b= 3 x= a * b print (x)`
- e) `a= 4 b= 3 x= “a” * b print (x)`

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

## PARTE IV: Aplicando funciones y métodos a los tipos de datos

### Ejercicio 29
Si se tienen las variables `n1=124.25` y `n2= “33.40”`, realizar las conversiones necesarias para saber la división entera entre ellos y el resto.

### Ejercicio 30
Pedir 5 palabras y mostrar la cantidad de letras que tienen en total.

### Ejercicio 31
Pedir el CUIT que tiene la siguiente forma xx/dni/x. Extraer y mostrar el DNI.

### Ejercicio 32
Mostrar el código ASCII de los caracteres “A”, “a” y “0”.

### Ejercicio 33
Pedir la cuenta de correo al usuario y mostrar por separado su usuario y su dominio.
