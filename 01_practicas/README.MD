# Fundamentos de Informática

---

# Práctica 1


## PARTE I: Aspectos Conceptuales

#### Ejercicio 1: 

¿Qué diferencias hay entre un lenguaje de máquina y uno de alto nivel?

#### Respuesta

>##### Lenguaje de Máquina:
> Es el conjunto de instrucciones directamente ejecutables por la CPU y es representado en código binario (0 y 1).
> Este es más específico para la arquitectura de la máquina pero es mas difícil de entender y escribir para los humanos.

> #### Los lenguajes de Alto Nivel, como Python, .NET, Java, etc.
> Son lenguajes más cercanos al lenguaje humano y para estos son abstractos y fácil de entender.
> Para poder trabajar con los mismos se necesita un compilador o intérprete para convertirse en código de máquina ejecutable.


#### Ejercicio 2: 
¿Qué ventajas tiene programar en un lenguaje de alto nivel? ¿Y desventajas?

#### Respuesta

> Las ventajas que tenemos al programar en lenguaje de programación de alto nivel son:
>
> - Mayor legibilidad y comprensión.
> - Portabilidad entre plataformas.
> - Desarrollo más rápido.
> - Abstracción de detalles de hardware.


>  ***y sus desventajas:***
>
> - Puede ser menos eficiente en términos de rendimiento.
> - Dependencia del compilador o intérprete.
> - Mayor consumo de recursos.

#### Ejercicio 3: 
Necesito ejecutar un programa que me permite hacer gráficos estadísticos.
 - (a) Si el programa está escrito en lenguaje C++ (Lenguaje compilado), ¿necesito el
compilador de C++?
 - (b) Si el programa está escrito en lenguaje Python (lenguaje interpretado), ¿necesito el
intérprete de Python?


#### Respuesta

>- (a) Lenguaje C++ (Compilado):
   >  Sí, necesitas el compilador de C++ para convertir el código fuente en un ejecutable que pueda ser ejecutado en tu máquina.
>
>
>- (b) Lenguaje Python (Interpretado):
   >  Sí, necesitas el intérprete de Python para ejecutar el código directamente, ya que Python es un lenguaje interpretado.

#### Ejercicio 4: 
 Según tu opinión, ¿qué ventajas tiene trabajar con software libre?

#### Respuesta
>El ***Software libre*** tiene como ventajar la libertad para estudiar, modificar y distribuir el software.
>Posee una comunidad colaborativa y transparente. Por lo general el costo de su implementación es cero o muy bajo.
>Y se posee un menor riesgo de dependencia de proveedores.

#### Ejercicio 5:
¿Qué es un IDE? 


#### Respuesta
>Un IDE es un software que proporciona herramientas y servicios integrados para facilitar el desarrollo de software.
>Incluye un editor de código, herramientas de compilación, depuración y a menudo características específicas del lenguaje.
>Ejemplos incluyen Eclipse, IntelliJ IDEA, Visual Studio, Geany.

---


### PARTE II: Instalando

>Instalación de las herramientas necesarias para trabajar. Si bien en las máquinas del gabinete están
>instaladas todas las herramientas necesarias para trabajar. Vamos a indicar cómo instalar las mismas en
>otros equipos (para que puedan contar con estas herramientas en otros ámbitos).

### Ejercicio 6: 
>Desde http://www.python.org, descargue la versión de Python acorde al sistema operativo
>de su equipo.
### Ejercicio 7: 
>Desde http://www.geany.org/ descargue el IDE Geany.
### Ejercicio 8: 
>¿Puede ejecutar Python desde cualquier directorio de su máquina? ¿Cómo verifica esto? Si
>no puede hacerlo, actualice lo necesario para que sea posible.

---


### PARTE III: Primeros pasos con

###Python

Desde el intérprete de Python

### Ejercicio 9: 
Indique qué versión es la que tiene instalada en su máquina

##### Respuesta 
> Python version 3

### Ejercicio 10: 
Ejecute las siguientes instrucciones:

1. print (“hola Fundamentos”)
2. print (2 + 3)
3. print (“2” + ”3”)
4. print (2* (3+5))
5. print (2 * 3 + 5)
6. print (3 * ”Hola”)
7. print (“Hola” * 3)
8. PRINT (“hola”)
9. print (hola)

- a) Compare los resultados obtenidos de 2 y 3, de 4 y 5, de 6 y 7.
- b) Qué pasó en las consignas 8 y 9?


##### Respuesta
Python version 3

> a. 
> - En 2) suma los números y en 3) sumas las cadenas
> - En 4) imprime 16 y en 5) imprime 11
> - En 6) y 7) imprime Hola tres veces

> b.
> En 8) PRINT no es una sentencia válida
> En 9) hola es una variable, la cual no está definida y por eso da error.



### Ejercicio 11: 
Ejecute las siguientes instrucciones:

10. “hola Fundamentos”
11.  2+3
    
a) ¿Pudo hacerlo?

b) Compare con 1 y 2 del ejercicio anterior.

#### Respuesta

> Si pude hacerlo, son iguales las ejecuciones

### Ejercicio 12: 
Ejecute las instrucciones guardadas en el archivo anterior ( [programa.py](programa.py) ) desde la
    consola. (Para esto, ubicado en la carpeta creada anteriormente y donde guardó el archivo -por ejemplo
    practica Fundamentos- ejecute el comando python programa.py). Explique por qué debe anteponer el
    comando python.

#### Respuesta
> Se antepone el comando python para poder ejecutar el programa.py llamando al interprete


## Desde Geany

### Ejercicio 13: 
Genere un nuevo archivo y tipee las siguientes instrucciones:
    print “Hola”
    print “ Vamos a trabajar un rato con Geany”

- a) Intente ejecutar este código. ¿Pudo hacerlo?
- b) Guarde el archivo con el nombre primer_programa.py (Cree primero una carpeta en su disco donde
guardará los programas Python, por ejemplo: practica_Fundamentos)
- c) ¿Puede ver algún cambio en el código de su programa?
- d) Ahora intente ejecutar el código. ¿Pudo hacerlo?

#### Respuesta
> a. Si pude hacerlo
> 
> b. - [primer programa](primer_programa.py) 
>
> c. No es igual
> 
> d. Si, anteponiendo python y el nombre del archivo.py


###PARTE IV: para debatir entre todos

Entre todos, den las razones y justificaciones para defender esto:

- a) Python es multiplataforma
- b) Se puede ejecutar el mismo programa .py tanto en Windows como en Linux
- c) Python tiene tipado dinámico
- d) Python es software libre
- e) Python es un lenguaje de alto nivel


#### Respuesta


> a. Python es multiplataforma:
>
> Python está diseñado para ser ejecutado en diferentes plataformas sin necesidad de realizar cambios significativos en el código fuente.
> Puede ejecutarse en sistemas operativos como Windows, Linux y macOS, lo que facilita la portabilidad de las aplicaciones.
>
> b. Se puede ejecutar el mismo programa .py tanto en Windows como en Linux:
> 
>Python utiliza un enfoque de interpretación que permite la ejecución del mismo código fuente en diferentes sistemas operativos sin necesidad de recompilación.
>Los programas Python son independientes del sistema operativo subyacente, siempre que las dependencias externas estén disponibles en ambas plataformas.
>
>c) Python tiene tipado dinámico:
> 
> El tipado dinámico en Python permite asignar tipos a las variables durante la ejecución del programa, facilitando la flexibilidad y la escritura de código más conciso.
>Permite una mayor agilidad en el desarrollo al no requerir declaraciones de tipo explícitas, lo que simplifica la escritura de código y acelera el proceso de desarrollo.
>
>d) Python es software libre:
> Python se distribuye bajo la Licencia Python, que es una licencia de software libre y de código abierto.
Esto significa que los usuarios tienen la libertad de usar, modificar y distribuir el software de acuerdo con los términos de la licencia, promoviendo la colaboración y la transparencia.
>
>e) Python es un lenguaje de alto nivel:
>
>Python proporciona abstracciones de alto nivel que permiten a los desarrolladores expresar conceptos en menos líneas de código, lo que facilita la lectura y mantenimiento del código.
Abstracciones de alto nivel, como la gestión automática de memoria y la manipulación de listas, diccionarios y otros tipos de datos complejos, simplifican el desarrollo de software.
Estas razones y justificaciones resaltan las ventajas y características distintivas de Python en términos de portabilidad, tipado dinámico, licencia de software libre y nivel de abstracción. Estos aspectos hacen que Python sea una opción atractiva para diversos proyectos y comunidades de desarrollo.
