<p align="center">
<a href="https://www.linkedin.com/in/soriamaximilianorodrigo/" target="_blank" rel="noopener noreferrer">
<img width="100%" height="100%" src="../docs/img/fundamentos.png" alt="Fundamentos"></a></p>


# Práctica 4 - Sentencias condicionales


[📂 PDF PRACTICAS 4](docs/Practica%204.pdf)

[⬅️ Volver](../README.MD)

## Recordatorio

### Operador logico AND

| and  | True | False |       
|------|------|-------|
| True | True | False |       
| False| False| False |       


### Operador logico OR

| or   | True | False |
|------|------|-------|
|True  | True | True  |
|False | True | False |

### Negaciones de operaciones

|not True | false |
|--|-------|
|not False  | true  |


### PARTE I: Aspectos Conceptuales

#### a) ¿Qué son las sentencias condicionales? ¿Para qué se utilizan?

### Respuesta
> Las sentencias condicionales son estructuras de control en programación que permiten ejecutar cierto bloque de código si una condición especificada es verdadera. Se utilizan para tomar decisiones dentro de un programa.

#### b) ¿Qué tipo de dato hay en la condición? ¿Como haría si se necesita evaluar mas de una condición?
### Respuesta
>La condición generalmente evalúa expresiones que resultan en valores booleanos (True o False). Para evaluar más de una condición, se utilizan operadores lógicos como `and` y `or`.

#### c) ¿Cómo se sabe que sentencias deben ejecutarse si la condición se cumple?
### Respuesta
>Si la condición se cumple (es verdadera), las sentencias dentro del bloque condicional se ejecutan. En caso contrario, se pueden proporcionar alternativas mediante las sentencias `elif` o `else`.

#### d)  Si utilizo una sentencia `if`,
- 🌕 ¿Cuántas sentencias elif puede tener? ¿Qué condiciones deben cumplir?
- 🌕 ¿Cuántas sentencias else puede tener?¿Se puede ubicar en cualquier sentencia `if` en cualquier lugar?

### Respuesta
>- Se puede tener múltiples sentencias `elif`, y se evalúan en orden hasta que una de ellas sea verdadera.
>- Se puede tener una única sentencia `else` opcional, que se ejecuta si ninguna de las condiciones anteriores es verdadera.

#### e) ¿Se puede tener dentro de una sentencia if, otra sentencia if? ¿Y dentro del else?

### Respuesta
>Sí, se puede tener dentro de una sentencia `if` otra sentencia `if`, y también se pueden anidar sentencias `if` dentro del bloque `else`.

## PARTE II: Ahora Practicamos



### Ejercicio 1: 
Escribir un programa que lee un número ingresado por el usuario en pantalla
y muestre si es positivo, negativo o cero

>### Respuesta
> [ejercicio1.py](practicas/01_practica.py)

### Ejercicio 2: 
Escribir un programa que me indique si un número es divisible por 6

>### Respuesta
> [ejercicio2.py](practicas/02_practica.py)

### Ejercicio 3: 
Escribir un programa que lea dos números “n” y “m” y determine si m es
divisible por n.

>### Respuesta
> [ejercicio3.py](practicas/03_practica.py)

### Ejercicio 4: 
Diseñar un programa que dado un número de 1 a 7 determine el día de la semana que representa.

>### Respuesta
> [ejercicio04.py](practicas/04_practica.py)

### Ejercicio 5: 

Dada la siguiente tabla

|Transporte |#Pasajeros|
|---|---|
|Bicicleta| 1|
|Moto |2|
|Auto |4|
|Camioneta |12|
|Colectivo |40|
|Avión |200|

Escribir un programa que dada la cantidad de personas a viajar, determine el
medio de transporte

>### Respuesta
> [ejercicio05.py](practicas/05_practica.py)

### Ejercicio 6: 
Desarrollar un programa en el ingrese un año de nacimiento y me indique si
la persona es bebé, menor, adolescente, adulto, veterano, abuelo

| Tipo                   | Edad       |
|------------------------|------------|
 | Bebé | < 2 años   |
 | Menor | > 2 y <=12 |
 | Adolescente | >12 y <=18 |
 | Adulto | >18 y <=45 |
| Veterano | >45 y <=60 |
| Abuelo                 | >60        |

>### Respuesta
> [ejercicio06.py](practicas/06_practica.py)


### Ejercicio 7: 
Dada la siguiente tabla

| Sexo      | Altura (cm) | - |
|-----------|-------------|---|
| Femenino  | < 145       | Petisa|
| Femenino  | >145 y <170 |Normal|
| Femenino  | >170        |Alta|
| Masculino | <160 cm     |Petiso|
| Masculino | >160 y <190 |Normal|
| Masculino |  > 190      |  Alto       |

Escriba un programa que, leyendo del teclado los valores de sexo y altura,
determine si es una persona petisa, normal o alta.

>### Respuesta
> [ejercicio07.py](practicas/07_practica.py)

Escriba un programa que, leyendo del teclado los valores de sexo y altura,
determine si es una persona petisa, normal o alta.

### Ejercicio 8: 
Diseña un programa que, dado un número entero, determine si éste es el
doble de un número impar. (Ejemplo: 14 es el doble de 7, que es impar.)

>### Respuesta
> [ejercicio08.py](practicas/08_practica.py)
 
### Ejercicio 9: 
Diseñar un programa que dado un carácter imprima en pantalla si es una
letra, un dígito, un carácter especial u otro tipo de carácter.

>### Respuesta
> [ejercicio09.py](practicas/09_practica.py)

### Ejercicio 10: 

Dadas 3 longitudes, decir mediante un mensaje si se forma o no un
triángulo (cada lado tiene que ser menor que la suma de los otros dos)

>### Respuesta
> [ejercicio10.py](practicas/10_practica.py)


### Ejercicio 11: 
Diseña un programa Python que lea un carácter cualquiera desde el
teclado, y muestre el mensaje @Es una MAYÚSCULA cuando el carácter sea una letra
mayúscula y @Es una MINÚSCULA cuando sea una minúscula. En cualquier otro caso, no
mostrará mensaje alguno. (Considera únicamente letras del alfabeto)
Pista: aunque parezca una obviedad, recuerda que una letra es minúscula si está entre la
’a’ y la ’z’, y mayúscula si está entre la ’A’ y la ’Z’.

>### Respuesta
> [ejercicio11.py](practicas/11_practica.py)


### Ejercicio 12: 
Escribir un programa que dado un año determine si es bisiesto o no. Un
año es bisiesto si es múltiplo de 4 (por ejemplo 1984). Los años múltiplos de 100 no son
bisiestos, salvo si ellos son también múltiplos de 400 (2000 es bisiesto, pero 1800 no lo
es).

>### Respuesta
> [ejercicio12.py](practicas/12_practica.py)


### Ejercicio 13: 
Dado la duración (en segundos) de una llamada telefónica, calcular su
costo, de la siguiente manera: El primer minuto $1,10, luego $0,25 cada fracción de 15
segundos (un cuarto de minuto).

>### Respuesta
> [ejercicio13.py](practicas/13_practica.py)

### Ejercicio 14: 
Calcular el número de pulsaciones que una persona debe tener por cada 10
segundos de ejercicio aeróbico; la fórmula que se aplica cuando el sexo es femenino es:
(220-edad)/10; si el sexo es masculino es: (210-edad)/10.

>### Respuesta
> [ejercicio14.py](practicas/14_practica.py)


## Ejercicios a entregar

De los ejercicios realizados anteriormente se solicita la entrega de los siguientes:

***Ejercicio 2:*** Escribir un programa que me indique si un número es divisible por 6


***Ejercicio 6:*** Desarrollar un programa en el ingrese un año de nacimiento y me indique si
la persona es bebé, menor, adolescente, adulto, veterano, abuelo.

|Tipo| Edad|
|--|--|
|Bebé| < 2 años|
|Menor| > 2 y <=12|
|Adolescente| >12 y <=18|
|Adulto |>18 y <=45|
|Veterano |>45 y <=60|
|Abuelo| >60|
