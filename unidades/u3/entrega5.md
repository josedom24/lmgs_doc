# Boletín Entrega 5: Final 1ª Evaluación

1. **(3 puntos)**: Escribe un programa python que pida una fecha (pedir día, mes y año separadas por `/`). El programa tiene que indicar si la fecha es correcta o no (teniendo en cuanta los años bisiestos). Si la fecha es correcta debe imprimer el día juliano. El día juliano es el número de días que han pasado desde el 1 de enero.

	Ejemplo:

		Fecha: 29/2/2015
		Fecha incorrecta

		Fecha: 29/2/2016
		Día Juliano: 60

		Fecha: 13/5/2017
		Día Juliano: 133

2. **(3 puntos)** Escribir un programa en python que vaya leyendo cadenas por teclado y la vaya guardando en una lista. Se terminará de pedir palabras cuando se introduzca un "\*". A continuación mostrará la siguiente información:

	* Mostrará la lista ordenada alfabéticamente.
	* Se mostrará las cadenas que tengan más de 5 caracteres.
	* ¿Cuantas cadenas empiezan por una vocal?
	* ¿Se ha introducido alguna cadena con un espacio?
	* Para terminar se pedirá otra cadena por teclado y se mostrarán todas las cadenas de la lista que comiencen por dicha cadena.

3. **(3 puntos)** Escribir un programa en python que calcule la raíz cuadrada: ax^2+bx+c=0. Para ello debemos introducir por teclado el coeficiente a,b y c. Puede ocurrir las siguientes cosas:
	* Si a=0, es una ecuación de primer grado x=-c/b
	* Si b^2-4ac<0: Se da un mensaje: "raíces complejas"

4. **(4 puntos)** Vamos a realizar un programa para llevar el control de almacén, para ello vamos a guardar cada artículo en una lista llamada "almacen". De cada producto hay que pedir el código, el nombre, la cantidad y el precio, estos datos se guardarán en una lista, y esta a su vez se guardará en la lista "almacen". Se pedirán datos por teclado hasta que se meta cómo código de artículo el 0.

	Veamos un ejemplo de la lista almacen:
		
		[[1, "Escoba", 30, 10.5 ], [2, "Fregona", 5, 12.23]]

	Cuando terminemos de rellenar la lista, se mostrará la siguiente información:

		* El código, nombre y precio con IVA (21 %) del cada artículo.
		* El código y nombre de artículo cuya cantidad sea menor de 10.
		* El programa te pedirá por teclado un código y te mostrará el nombre del artículo.


5. **(7 puntos)** Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado. La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles.

	Por ejemplo:

		Cantidad total: 7,17 €
		Cantidad entregada: 100 €
		Cantidad a devolver: 92,83 €

		1  billete de 50 €
		2 billete de 20 €
		1 monedas de 2 €
		1 monda de 50 c
		1 moneda de 20 c
		1 moneda de 10 c
		1 moneda de 2 c
		1 moneda 1 c


