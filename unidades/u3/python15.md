# Tipo de datos secuencia: Listas

Las listas (`list`) me permiten guardar un conjunto de datos que se pueden repetir y que pueden ser de distintos tipos. 

## Construcción de una lista 

Para crear una lista puedo usar varias formas:

* Con los caracteres `[` y `]`:

		>>> lista1 = []
		>>> lista2 = ["a",1,True]

* Utilizando el constructor `list`, que toma como parámetro un dato de algún tipo secuencia.

		>>> lista3 = list()
		>>> lista4 = list("hola")
		>>> lista4
		['h', 'o', 'l', 'a']

## Operaciones básicas con listas

Vamos a ver distintos ejemplos partiendo de una lista, que es una secuencia mutable.

	lista = [1,2,3,4,5,6]

* Las secuencias se pueden recorrer.

	>>> for num in lista:
	...   print(num,end="")
	123456

* Operadores de pertenencia: Se puede comprobar si un elemento pertenece o no a una secuencia con los operadores `in` y `not in`.

	>>> 2 in lista
	True
	>>> 8 not in lista
	True

* Concatenación: `+`: El operador `+` me permite unir datos de tipos listas.

	>>> lista + [7,8,9]
	[1, 2, 3, 4, 5, 6, 7, 8, 9]

* Repetición: `*`: El operador `*` me permite repetir un dato de un tipo lista.

	>>> lista * 2
	[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

* Indexación: Cada elemento tiene un índice, empezamos a contar por el elemento en el índice 0. Si intento acceder a un índice que corresponda a un elemento que no existe obtenemos una excepción `IndexError`.

		>>> lista1[6]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module
		IndexError: list index out of range	

	Se pueden utilizar índices negativos:

		>>> lista[-1]
		6

* Slice: Veamos como se puede utilizar

	* `lista[start:end]` 	  # Elementos desde la posición start hasta end-1
	* `lista[start:]`    	  # Elementos desde la posición start hasta el final
	* `lista[:end]`      	  # Elementos desde el principio hata la posición end-1
	* `lista[:]` 		 	  # Todos Los elementos	    
	* `lista[start:end:step]` # Igual que el anterior pero dando step saltos.
 		
 	Se pueden utilizar también índices negativos, por ejemplo: `lista[::-1]`

 		>>> lista[2:4]
		[3, 4]
		>>> lista[1:4:2]
		[2, 4]

## Funciones predefinidas que trabajan con listas

	>>> lista1 = [20,40,10,40,50]
	>>> len(lista1)
	5
	>>> max(lista1)
	50
	>>> min(lista1)
	10
	>>> sum(lista1)
	150
	>>> sorted(lista1)
	[10, 20, 30, 40, 50]
	>>> sorted(lista1,reverse=True)
	[50, 40, 30, 20, 10]


## Listas multidimensionales

A la hora de definir las listas hemos indicado que podemos guardar en ellas datos de cualquier tipo, y evidentemente podemos guardar listas dentro de listas. 

	>>> tabla = [[1,2,3],[4,5,6],[7,8,9]]
	>>> tabla[1][1]
	5

	>>> for fila in tabla:
	...   for elem in fila:
	...      print(elem,end="")
	...   print()
	 
	123
	456
	789

## Recorriendo varias secuencias. Función zip()

Con la instrucción `for` podemos ejecutar más de una secuencia, utilizando la función `zip`. Esta función crea una secuencia donde cada elemento es una tupla de los elementos de cada secuencia que toma cómo parámetro.

*Ejemplo*

	>>> list(zip(range(1,4),["ana","juan","pepe"]))
	[(1, 'ana'), (2, 'juan'), (3, 'pepe')]

Para recorrerla:

	>>> for x,y in zip(range(1,4),["ana","juan","pepe"]):
	...     print(x,y)	
	1 ana
	2 juan
	3 pepe
