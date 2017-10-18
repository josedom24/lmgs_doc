# Boletín Entrega 1: Ejercicios alternativas

1. Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no. Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero.

	```bash
	DIVISOR DE NÚMEROS
	Escriba el dividendo: 14
	Escriba el divisor: 5
	La división no es exacta. Cociente: 2 Resto: 4	
	```	

	```bash
	DIVISOR DE NÚMEROS
	Escriba el dividendo: 20
	Escriba el divisor: 4
	La división es exacta. Cociente: 5
	```

2. Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

	```bash
	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2020
	Para llegar al año 2020 faltan 5 años.
	```
	```bash
	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 1997
	Desde el año 1997 han pasado 18 años.
	```
	```bash
	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2015
	¡Son el mismo año!
	```

3. Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

	```bash
	COMPARADOR DE TRES NÚMEROS
	Escriba un número: 6
	Escriba otro número: 6
	Escriba otro número más: 6
	Ha escrito tres veces el mismo número.
	```
	```bash
	COMPARADOR DE TRES NÚMEROS
	Escriba un número: 6
	Escriba otro número: 6.5
	Escriba otro número más: 6
	Ha escrito uno de los números dos veces.
	```
	```bash
	COMPARADOR DE TRES NÚMEROS
	Escriba un número: 4
	Escriba otro número: 5
	Escriba otro número más: 6
	Los tres números que ha escrito son distintos.
	```

4. Escriba un programa que pida los coeficientes de una ecuación de primer grado (``a x + b = 0``) y escriba la solución. Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es ``x = -b / a`` Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones):

	```bash
	ECUACIÓN A X + B = 0
	Escriba el valor del coeficiente a: 0
	Escriba el valor del coeficiente b: 3
	La ecuación no tiene solución.
	```
	```bash
	ECUACIÓN A X + B = 0
	Escriba el valor del coeficiente a: 4.2
	Escriba el valor del coeficiente b: 21
	La ecuación tiene una solución: -5.0
	```
	```bash
	ECUACIÓN A X + B = 0
	Escriba el valor del coeficiente a: 0
	Escriba el valor del coeficiente b: 0
	Todos los números son solución.
	```

5. Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).

La dificultad del ejercicio se puede reducir o aumentar según la forma de presentar el resultado:

* Sin separador entre unidades: 2 km 400 m 5 cm
* Separando con comas las unidades: 2 km, 400 m, 5 cm
* Separando con comas y con la conjunción 'y' en la última unidad: 2 km, 400 m y 5 cm

	```bash
	CONVERTIDOR DE CM A KM, M Y CM
	Escriba una distancia en centímetros: 100
	100 centímetros son 1 m.
	```
	```bash
	CONVERTIDOR DE CM A KM, M Y CM
	Escriba una distancia en centímetros: 43210
	43210 centímetros son 432 m, 10 cm.
	```
	```bash
	CONVERTIDOR DE CM A KM, M Y CM
	Escriba una distancia en centímetros: 240005
	240005 centímetros son 2 km, 400 m, 5 cm.
	```
	```bash
	CONVERTIDOR DE CM A KM, M Y CM
	Escriba una distancia en centímetros: 67
	67 centímetros son 67 cm.
	```
	```bash
	CONVERTIDOR DE CM A KM, M Y CM
	Escriba una distancia en centímetros: 300004
	300004 centímetros son 3 km, 4 cm.
	```
