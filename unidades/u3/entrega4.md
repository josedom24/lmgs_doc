# Boletín Entrega 4: Ejercicios cadenas de caracteres

1. Realiza un programa que pida un cadena. A continuación debe pedir otra cadena. El programa debe buscar la segunda cadena en la primera (ignorando mayúsculas o minúsculas) y podrá responder una de las siguientes opciones:
	
	* La segunda cadena es una subcadena de la primera
	* La segunda cadena no es una subcadena de la primera

	Ejemplo:

		Cadena 1: Java es un lenguaje de programación
		Cadena 2: LENGUAJE
		Respuesta:
		La segunda cadena es una subcadena de la primera

2. Escribir un programa python que dado una palabra diga si es un palíndromo. Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: *reconocer*

	Modifica el programa para que compruebe si una frase es palíndroma. Ejemplo: *Yo hago yoga hoy*

3. Escribe una programa que pida una cadena de caracteres y diga si *no* tiene caracteres repetidos.

4. Tenemos la siguiente variable definida en nuestro programa:

	temperaturas='''
		Utrera,29,12
		Dos Hermanas,32,14
		Sevilla,30,15
		Alcalá de Guadaíra,31,14
		'''

	En esa cadena se definen nombres de poblaciones y las temperaturas máximas y mínimas de dichas poblaciones durante un día.

	Realiza un programa que muestre el nombre de las poblaciones y la temperatura media. Además el programa te debe pedir el nombre de una población y nos debe dar la temperatura máxima y mínima (si la población no funciona se debe dar une error.)

	Ayuda: Puede venir muy bien utilizar el método `split` de cadenas.

5. Juego Mastermind. El juego consiste en que el ordenador piensa en 4 dígitos no repetidos (se guardan en una cadena de caracteres). Luego se va pidiendo al usuario número de 4 dígitos para acertar el que ha generado de forma aleatoria. La respuesta del programa será la siguiente:

	* Si acertamos un dígito y está en la misma posición contará un acierto
	* Si acertamos un dígito pero no está en la mismo posición contará una coincidencia.

	Cuando acertemos el número nos dirá en los intentos que lo hemos adivinado.

	Ejemplo:

		Bienvenido/a al Mastermind!
		Tenes que adivinar un numero de 4 cifras distintas
		Que código propones?: 1234
		Tu propuesta ( 1234 ) tiene 0 aciertos y  1 coincidencias.
		Propone otro código: 5678
		Tu propuesta ( 5678 ) tiene 0 aciertos y  1 coincidencias.
		Propone otro código: 1590
		Tu propuesta ( 1590 ) tiene 1 aciertos y  1 coincidencias.
		Propone otro código: 2960
		Tu propuesta ( 2960 ) tiene 2 aciertos y  1 coincidencias.
		Propone otro código: 0963
		Tu propuesta ( 0963 ) tiene 1 aciertos y  2 coincidencias.
		Propone otro código: 9460
		u propuesta ( 9460 ) tiene 1 aciertos y  3 coincidencias.
		Propone otro código: 6940
		Felicitaciones! Adivinaste el código en 7 intentos.