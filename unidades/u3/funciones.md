# Ejercicio de funciones

Queremos hacer una librería con funciones que nos ayuden a trabajar con fechas. Crea un fichero `fechas.py` con las siguientes funciones, debes pensar el número de parametros que reciben y que valor devuelven:

* `es_bisiesto`: Función que recibe un año y te devuelve si el año es bisesto o no.
* `dias_del_mes`: Función que recibe un mes y un año, y te devuelve el número de días que tiene dicho mes en ese año. 
* `calcular_dia_juliano`: Función que recibe una fecha (un día, un mes y un año) y devuelve el día juliano (cantidad de días que han pasado desde el 1 de enero).

A partir de estas funciones realiza, en otro fichero, un programa. Para poder realizar el programa tenemos que importar las funciones que vamos a utilizar, para ello:
	
	from fechas import calcular_dia_juliano

El programa haría lo siguiente:

Se piede por teclado una fecha (una cadena de caracteres con formato dd/mm/aaaa), y se muestra por pantalla el día juliano al que corresponde.

¿Se te ocurre hacer alguna otra función a aprtir del código que hemos desarrollado?