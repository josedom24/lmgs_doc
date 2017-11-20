# Boletín 6: Ejercicios variados

1. Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:

	* Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido. En la quiniela se indican 15 partidos. Ejemplo: 
	``equipos = [["Sevilla","Betis"],["Madrid","Barcelona"],...]``
	* Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista), en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo. Ejemplo: 
	``resultados=[[3,0],[0,0],...]``

	El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

2. La letra del DNI se calcula a partir de su número. Para ello se divide el número entre 23 y el resto (que tiene que ser un número entre 0 y 22 se sustituye por la letra
correspondiente de la siguiente tabla:

		0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
		T R W A G M Y F P D X  B  N  J  Z  S  Q  V  H  L  C  K  E

	Escribe un programa que te pida un número de DNI y una letra y te diga si es correcto o no.

3. El módulo `random` incluye la función `random()` que genera un número seudo-aleatorio entre 0 y 1:
	
		>>> from random import random
		>>> random()
		0.51605767814317494

	Crea un programa que pida al usuario un número n y genere una lista con n elementos con valores aleatorios y muestre como salida:

	* La lista de los n números aletaorios con una precisión de 3 decimales.
	* La suma de todos los elementos con una precisión de 2 decimales.

	Nota: Los valores deben redondearse a la precisión solicitada, no truncarse.

	Ejemplo

		Dame un numero: 4
		La lista de 4 numeros aleatorios es: (0.123, 0.432, 0.335, 0.456)
		La suma de estos 4 elementos es: 1.3

4. Escribe un programa que pida al usuario su fecha de nacimiento y le responda el día de la semana correspondiente (para ello debes utilizar la función adecuada del módulo calendar). Ejemplo:

	Introduce tu fecha de nacimiento (DD-MM-YYYY): 29-02-1992
	Naciste en sabado

5. Una dirección 6to4 es una dirección IPv6 reservada para equipos que tienen actualmente una dirección IPv4 pública. Un ejemplo de dirección 6to4 sería:

		2002:503b:198:0:219:66ff:fea8:db3

	El campo 2002: es fijo y el bloque importante para esta discusión es el que determina la parte de red de la dirección, es decir, los campos `503b:198` que son la representación hexadecimal de la dirección IPv4 correspondiente:

		80.59.1.152 = 0x50.0x3b.0x1.0x98 = 503b:198

	el resto de campos se corresponden con la dirección de subred y la dirección de host, y no son relevantes para este ejercicio.

	Escribe un programa que pida una dirección IPv4 pública y nos dé la parte de red correspondiente de la dirección 6to4 asociada:

	Ejemplo:

		Dame una dirección IPv4 publica: 85.135.34.12
		La parte de red 6to4 correspondiente es: 2002:5587:220

6. El Código Cuenta Cliente (CCC) es el código que identifica en España las cuentas corrientes de los clientes de bancos. El CCC tiene 20 dígitos en formato AAA-BBBB-CC-
DDDDDDDDDD.

	* AAAA son cuatro dígitos que identifican la entidad bancaria.
	* BBBB son cuatro dígitos que identifican la oficina.
	* CC se denomina dígito de control (DC).
	* DDDDDDDDDD son 10 dígitos de la cuenta del cliente en el banco.

	Según la Wikipedia:
	Los dígitos situados en las posiciones novena y décima se generan a partir de los demás dígitos del CCC, permitiendo comprobar la validez del mismo
y reducir la posibilidad de errores de manipulación. El primero de ellos valida conjuntamente los códigos de entidad y de oficina; el segundo, valida el número de cuenta.
	Cada uno de los dígitos del DC se calcula utilizando el mismo algoritmo, para lo que se complementa con dos ceros a la izquierda la entidad y oficina.

	La siguiente función en Python calcula el DC correspondiente para una lista de 10 número enteros:

		def calcula_dc(lista):
		"""Calcula el dígito de control de una CCC.
		Recibe una lista con 10 numeros enteros y devuelve el DC
		correspondiente"""
		pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
		aux = []
		for i in range(10):
			aux.append(lista[i]*pesos[i])
		resto = 11 - sum(aux) %11
		if resto == 10:
			return 1
		elif resto == 11:
			return 0
		else:
			return resto

	Por ejemplo:
		>>> lista = [1, 6, 7, 0, 0, 0, 0, 3, 3, 2]
		>>> calcula_dc(lista)
		5

	Escribe un programa que pida al usuario un CCC en el formato arriba indicado y compruebe su validez.

7. Escribe un programa para jugar al ahorcado.

	* Un jugador introduce una palabra secreta y otro jugador tratará de adivinarla.
	* La pantalla se limpia y aparece la horca vacía, el número de intentos y la palabra a acertar, donde cada letra se sustituye por un asterisco.

		```
		EL JUEGO DEL AHORCADO

		  +---+
		  |	  |
		  	  |
		  	  |
		  	  |
		  	  |
		  ======

		Palabra a acertar :********
		Fallos : 0
		Letras utilizadas :

		Introduce una letra ( '*' para resolver ):
		```
	Reglas del juego:

	* El jugador puede cometer como máximo 6 fallos. Por cada fallo aparecerá un elemento más en la horca: cabeza, tronco, brazo izquierdo, brazo derecho,
pierna izquierda y pierna derecha.
	* Cada letra acertada aparecerá en la lista de letras utilizadas y se sustituirá en la posición que corresponda en la palabra a acertar.
	* Una letra ya utilizada contará siempre como fallo (Esté o no en la palabra a acertar)
	* No se permite el uso de vocales
	* El jugador puede intentar resolver la palabra a acertar en cualquier momento tecleando la tecla `*`, tras lo cual se solicitará la palabra.
	* El juego termina cuando el número de fallos es igual a 6 o cuando el jugador acierta la palabra, solicitando la resolución de la misma.
	* Cualquier otro carácter que se introduzca: numero o signo de puntuación, contará como fallo.
	* En un momento cualquiera el programa mostrará:

		```
		EL JUEGO DEL AHORCADO

		   +---+
		   |   |
		   o   |
		  /|   |
		       |
		       |
		   ======

		Palabra a acertar :y**t*p***t*
		Fallos : 3
		Letras utilizadas : y n m p t b 

		Introduce una letra ( '*' para resolver ):
		```

	* Se obtendrá mayor puntuación en el ejercicio si se estructura adecuadamente el código mediante el uso de funciones.
	* Para que no se desplacen los caracteres a posiciones no deseadas, utiliza el triple apóstrofe con el print, por ejemplo:

		```
		>>> print('''
		  +---+
		  |	  |
		  o	  |
		 /|	  |
		  	  |
		  	  |
		  ======
		''')
		```

	* Para limpiar la pantalla se puede utilizar (en GNU/Linux):
		
		import os
		os.system ('clear')



