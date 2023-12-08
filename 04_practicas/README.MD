<p align="center">
<a href="https://www.linkedin.com/in/soriamaximilianorodrigo/" target="_blank" rel="noopener noreferrer">
<img width="100%" height="100%" src="../docs/img/fundamentos.png" alt="Fundamentos"></a></p>


# Práctica 4 - Sentencias condicionales


[📂 PDF PRACTICAS 4](docs/Practica%204.pdf)


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

### PARTE II: Ahora Practicamos



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


