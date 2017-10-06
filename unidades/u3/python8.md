# Datos

## Literales, variables y expresiones

### Literales

Los literales nos permiten representar valores. Estos valores pueden ser de diferentes tipos, de esta manera tenemos diferentes tipos de literales:

**Literales numéricos**

* Para representar números enteros utilizamos cifras enteras (Ejemplos: 3, 12, -23). Si queremos representarlos de forma binaria comenzaremos por la secuencia `0b` (Ejemplos: 0b10101, 0b1100). La representación octal la hacemos comenzando por `0o` (Ejemplos: 0o377, 0o7) y por último, la representación hexadecimal se comienza por `0x` (Ejemplos: 0xdeadbeef, 0xfff).

* Para los números reales utilizamos un punto para separar la parte entera de la decimal (12.3, 45.6). Podemos indicar que la parte decimal es 0, por ejemplo 10., o la parte entera es 0, por ejemplo .001.


**Literales cadenas**

Nos permiten representar cadenas de caracteres. Para delimitar las cadenas podemos usar el carácter ' o el carácter ". También podemos utilizar la combinación ''' cuando la cadena ocupa más de una línea. Ejemplos.

	'hola que tal!'
	"Muy bien"
	'''Podemos \n
	ir al cine'''

Con el carácter \, podemos escapar algunos caracteres, veamos algunos ejemplos:

	\n 	ASCII Linefeed (LF) 	 
	\t 	ASCII Horizontal Tab (TAB) 	 
	

### Variables

Una variables es un identificador que referencia a un valor. Estudiaremos más adelante que python utiliza tipado dinámico, por lo tanto no se usa el concepto de variable como almacén de información. Para que una variable referencie a un valor se utiliza el operador de asignación `=`.

El nombre de una variable, ha de empezar por una letra o por el carácter guión bajo, seguido de letras, números o guiones bajos. No hay que declarar la variable antes de usarla, el tipo de la variable será el mismo que el del valor al que hace referencia. Por lo tanto su tipo puede cambiar en cualquier momento:

	>>> var = 5
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>

Hay que tener en cuanta que python distingue entre mayúsculas y minúsculas en el nombre de una variable, pero se recomienda usar sólo minúsculas.

#### Definición, borrado y ámbito de variables

Como hemos comentado anteriormente para crear una variable simplemente tenemos que utilizar un operador de asignación, el más utilizado `=` para que referencia un valor. Si queremos borrar la variable utilizamos la instrucción `del`. Por ejemplo:

	>>> a = 5
	>>> a
	5
	>>> del a
	>>> a
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined

Podemos tener también variables que no tengan asignado ningún tipo de datos:

	>>> a = None
	>>> type(a)
	<class 'NoneType'>

El ámbito de una variable se refiere a la zona del programa donde se ha definido y existe esa variable. Como primera aproximación las variables creadas dentro de funciones o clases tienen un ámbito local, es decir no existen fuera de la función o clase. Concretaremos cuando estudiamos estos aspectos más profundamente.


### Expresiones

Una expresión es una combinación de variables, literales, operadores, funciones y expresiones, que tras su evaluación o cálculo nos devuelven un valor de un determinado tipo. 

Veamos ejemplos de expresiones:

	a + 7
	(a ** 2) + b


### Operadores. Precedencia de operadores en python

Los operadores que podemos utilizar se clasifican según el tipo de datos:

* Operadores aritméticos (`+ - * ** / // %`)
* Operadores de cadenas (`+ *`)
* Operadores de asignación (`= -= *= /= //= %=`)
* Operadores de comparación (`< > <= >= == !=`)
* Operadores lógicos (`and, or, not`)

La procedencia de operadores es la siguiente:

1. Los paréntesis rompen la procedencia.
2. La potencia (**)
3. Operadores unarios (+ -)
4. Multiplicar, dividir, módulo y división entera (* /% // )
5. Suma y resta (+ -)
6. Operadores de comparación (<= < > >=)
7. Operadores de igualdad (<> == !=)
8. Operadores de asignación (= %= /= //= -= += *= **=)
9. Operadores lógicos (not, or, and)

