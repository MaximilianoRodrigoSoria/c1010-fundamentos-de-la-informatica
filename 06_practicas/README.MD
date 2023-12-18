<p align="center">
<a href="https://www.linkedin.com/in/soriamaximilianorodrigo/" target="_blank" rel="noopener noreferrer">
<img width="100%" height="100%" src="../docs/img/fundamentos.png" alt="Fundamentos"></a></p>


# Práctica 6 - Estructuras de control - ***REPASO***


[📂 PDF PRACTICAS 6](docs/Practica%206%20Repaso-%20Ejercicios%20avanzados%20NO%20ENTREGA%20OBLIGATORIA.pdf)

[⬅️ Volver](../README.MD)


## Introducción:

Esta práctica está orientada a profundizar las capacidades desarrolladas durante el  curso, estos ejercicios se asimilan a los usados por la cátedra durante las evaluaciones.

Resolver estos ejercicios permitirá al alumno ejercitar todos los conceptos aprendidos durante el cuatrimestre y llegar al día de la evaluación con un nivel de
preparación más avanzado.

Al momento de resolver esta práctica es indispensable que el alumno aplique los siguientes conceptos:
- Modularización y definición adecuada de argumentos
- Estructuras de control
- Pasaje de parámetros
- Condicionales simples y compuestos

### Ejercicio 1:
* a. Defina una función que reciba como argumento una cadena de texto y retorne un
valor entero indicando la cantidad de vocales que contiene la cadena Ejemplo:
>“agua” -> 3, “pepe” ->2

* b. Defina una función que genere una lista de palabras hasta que se ingrese la
palabra “fin” la cual NO debe ser almacenada en la lista, por cada palabra,
también se guardara la cantidad de vocales que contiene la misma, para esto
deberá utilizar la función definida en el punto 1) a, al finalizar la función deberá
retornar la lista generada.
   1. La lista resultado deberá tener una estructura similar a:


> [[“uno”,2],[ “pepe”,2],[”agua!”,3],…etc]

* c. Defina una función que reciba como argumento la lista generada en el punto 1.b) e
imprimir las palabras que tienen mas de 3 vocales.

* d. escriba el código del programa que integra las 3 funciones antes definidas.

>### Respuesta
> [ejercicio01.py](practicas/01_practica.py)

### Ejercicio 2:

Resuelva modularizando

* a. Realice un programa para manejar equipos de fútbol, Armar una lista que tenga información sobre los equipos de fútbol. Para cada equipo deberán tener: el nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor.

* b. Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los equipos que están en la primera y última posición de la lista.

* c. Imprimir el nombre del equipo Campeón de la lista generada en el punto a), el equipo campeón es aquel que sumo más puntos

>### Respuesta
> [ejercicio02.py](practicas/02_practica.py)

### Ejercicio 3:
Implemente los siguientes puntos:

a. Realice una función que procesa la información de alumnos de la UNAJ. De cada alumno se conoce legajo, nombre, apellido, contraseña. El procesamiento termina
cuando se ingresa el número de legajo 0. La función deberá retornar una lista con la información procesada.

b. Realice una función llamada imprimir_alumno que recibe como parámetro una lista con los datos de un alumno (Legajo, nombre, apellido, contraseña), los datos del alumno serán mostrados por pantalla con la forma:
>Legajo:XXXX
> 
>Nombre:XXXX
> 
>Apellido:XXXX
> 
>Contraseña:XXXXX

c. Realice una función llamada legajo_menor que recibe como parámetro una lista de alumnos, de cada alumno se conoce la información (legajo, nombre, apellido,
contraseña), la función debe buscar cuál es el alumno con el menor legajo dentro de la lista y retornarlo.

d. Realice una función llamada nombre_mas_largo que recibe como parámetro una lista de alumnos. La función debe buscar cuál es el alumno con el nombre más
largo dentro de la lista y retornarlo.

e. Realice una función llamada controlar_clave que recibe como parámetro un alumno,(legajo, nombre, apellido, contraseña). La función debe controlar si la
contraseña es mayor a 6 caracteres y termina con un número, deberá imprimir un mensaje especificando el error cometido en caso de no cumplir las condiciones o
bien imprimir los datos del alumno si la clave cumple con todas las condiciones.

f. Realice una función llamada verificar_claves que recibe como parámetro una lista  de alumnos, la función deberá controlar por cada alumno si la contraseña que usa
cumple con: ser mayor a 6 caracteres y terminar con un número.

Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir del menú, el resto de las opciones permiten:

- imprimir los datos de todos los alumnos con el formato pedido en el punto a)
- imprimir los datos del alumno que tiene el legajo más chico.
- imprimir los datos del alumno que tiene el nombre más largo.
- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número.


>### Respuesta
> [ejercicio03.py](practicas/03_practica.py)

### Ejercicio 4:

Se desea realizar un programa para una universidad. El mismo deberá permitir guardar la información de todos los cursos que se dictan en la misma. La cantidad de cursos
existentes es ingresado por el usuario del sistema. De cada curso se debe conocer:

Nombre, Cantidad de Clases, Día de Dictado, Hora de Comienzo, Duración en minutos.

**Importante: si la duración del curso es mayor a 360 minutos, NO se debe guardar la información del mismo.**

#### El programa debe permitir

* a. Imprimir todos los cursos que tengan más de 5 clases

* b. Imprimir los cursos que se dictan en un día de la semana indicado por el usuario.

* c. Imprimir el curso más intensivo (definido por la cantidad de clases y la duración de cada clase)

* d. Imprimir los datos en que se dicta un curso indicado por el usuario.

* e. Imprima todos los cursos que comienzan con una letra indicada por el usuario.

El programa escrito deberá mostrar un menú para que el usuario elija la opción deseada.
Importante: el sistema termina cuando el usuario elige la opción “salir”.

>### Respuesta
> [ejercicio04.py](practicas/04_practica.py)

### Ejercicio 5:

Nos contratan para realizar un sistema para un kiosco. De cada artículo se conoce
código, nombre, una descripción, el precio de venta, el nombre del proveedor y si es
necesaria la refrigeración del artículo (pudiendo ser R=requiere frío o N=no requiere frío).

* a) Realice una función que cree una lista con información de artículos de kiosco. La
carga de artículos finaliza cuando se ingresa un artículo cuyo código = “999” y que
a la vez no requiera frío.
* b) Realice una función que cree una lista con los datos del stock, donde de cada
articulo se conoce el código y la cantidad existente.
* c) Se requiere imprimir los datos de todos los artículos que necesitan refrigeración o
los artículos que no la necesitan, dependiendo del valor ingresado por el usuario
(R=requiere frío o N=no requiere frío).
* d) Se necesita imprimir la cantidad de artículos que necesitan refrigeración y la
cantidad de artículos que no la necesitan.

* e) Se requiere imprimir los datos de los artículos cuyo stock es 0, de la siguiente
manera: Código, nombre del artículo, y nombre del proveedor.
* f) Realice una función que utilizando la lista de productos creada en a) y en b) genere
una nueva lista con la información completa de los artículos que no requieren frío,
indicando además la cantidad existente.
Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir
del menú, el resto de las opciones permiten:

- imprimir los datos de los artículos que necesitan o no refrigeración, dependiendo
del valor ingresado por el usuario
- imprimir la cantidad de artículos que precisan refrigeración
- imprimir la cantidad de artículos que no requieren refrigeración
- imprimir los datos de los artículos cuyo stock es 0
- imprimir la información completa de los artículos que no requieren frío

>### Respuesta
> [ejercicio05.py](practicas/05_practica.py)


### Ejercicio 6:
Nos contratan para realizar un sistema para una editorial. Se recibe un texto y se desea obtener la
siguiente información:
- La longitud total del texto.
- La cantidad de palabras componen el texto.
- La cantidad de oraciones que componen el texto.
- La cantidad de palabras que comienzan con vocal o con consonante, dependiendo del
valor ingresado por el usuario.
- Buscar una palabra ingresada por el usuario y retornar la cantidad de veces que se
encuentra en el texto.
- La cantidad de palabras que comienzan con mayúscula.
- La cantidad de caracteres que son números.
- La cantidad de palabras que comienzan con vocal y la cantidad de palabras que
comienzan con consonante.
- Imprimir todas las palabras que terminan en infinitivo (terminadas en ar er o ir).


>### Respuesta
> [ejercicio06.py](practicas/06_practica.py)