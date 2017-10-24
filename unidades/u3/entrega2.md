# Boletín Entrega 2: Ejercicios repetitivas

1. Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

	Notas:

	* Un número es divisible por otro cuando el resto de su división es cero (numero % divisor == 0).
    * Se puede hacer un programa más rápido, teniendo en cuenta que los divisores son siempre menores (o iguales) que la mitad del número. Es decir, no hace falta probar todos los números entre 1 y el propio número, sino únicamente hasta la mitad. Si se hace así, no hay que olvidarse de añadir el propio número a la lista de divisores.

	```bash
	DIVISORES
	Escriba un número mayor que cero: -5
	¡Le he pedido un número entero mayor que cero!
	```

	```bash
	DIVISORES
	Escriba un número entero mayor que cero: 200
	Los divisores de 200 son 1 2 4 5 8 10 20 25 40 50 100 200
	```

2. Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

	```bash
	MAYORES QUE EL PRIMERO
	¿Cuántos valores va a introducir? -1
	¡Imposible!
	```
	
	```bash
	MAYORES QUE EL PRIMERO
	¿Cuántos valores va a introducir? 4
	Escriba un número: 6
	Escriba un número más grande que 6: 10
	Escriba un número más grande que 6: 3
	¡3 no es mayor que 6!
	Escriba un número más grande que 6: 9
	Gracias por su colaboración
	```

3. Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo.

	```bash
	SUMA ENTRE VALORES
	Escriba un número entero: 7
	Escriba un número entero mayor que 7: 7
	¡Le he pedido un número entero mayor que 7!	
	```
	```bash
	SUMA ENTRE VALORES
	Escriba un número entero: 30
	Escriba un número entero mayor que 30: 32
	La suma desde 30 hasta 32 es 93	
	```

	Mejore el programa anterior haciendo que el programa escriba la suma realizada.

	```bash
	SUMA ENTRE VALORES
	Escriba un número entero: 10
	Escriba un número entero mayor que 10: 15
	La suma desde 10 hasta 15 es 75
	10 + 11 + 12 + 13 + 14 + 15 = 75
	```


4. Realizar un programa python que pida por teclado los extremos de un intervalo. Debemos comprobar que el extremo inferior sea menor que el superior, sino ocurre esto el programa terminará con un error. Se debe comprobar, además, que los dos extremos son positivos (mayor que 0), sino ocurre esto, el programa tarminará dando un mensaje de error.

 Una vez leído los extremos, se pedirán números positivos, finalizando cundo introduzcamos un 0. Al terminar el programa mostrará la siguiente información:

 * La cantidad de números introducidos que pertenecen estrictamente al intervalo. 
 * El máximo de los números introducidos que no pertenecen al intervalo. 
 * La media de los números que no pertenecen al intervalo. 
 * Si se ha introducido algún número igual a algunos de los dos intervalos. 

 Nota: Se puede mejorar el programa si al detectar que el limite inferior es mayor que el superior, intercambiar los valores.

	```bash
	Dime el límite inferior: 3
	Díme el límite superior: 10

	Escribe un número: 6
	Escriba un número: 2
	Escriba un número: 12
	Escriba un número: 3
	Escriba un número: 5
	Escriba un número: 0

	La cantidad de números dentro del intervalo es: 2
	El máximo de los números fuera del intervalo es: 12
	La media de los que no pertenecen al intervalo es: 5.666666
	Si se ha introducido un número igual a un límite del intervalo.
	```

5.

**Apartado 1**

Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.

Para generar números al azar puedes utilizar el siguiente código:

	```python
	from random import randint
	a = randint(2, 10)
	```

	```bash
	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	```	

	```bash
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!
	```

**Apartado 2**

Amplie el programa anterior haciendo que el programa pida primero al usuario cuántas multiplicaciones se van a plantear.

	```bash
	Número de preguntas: 0
	El número de preguntas debe ser al menos 1	
	```

	```bash
	Número de preguntas: 2	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	

	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!
	```

**Apartado 3**

Amplie el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa felicitará al usuario por el resultado.
Ayuda: La nota se calcula con la fórmula Nota=Correctas / Total * 10.

	```bash
	Número de preguntas: 2	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	

	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!	

	Ha contestado correctamente 1 pregunta
	Le corresponde una nota de 5.0	
	```
	```bash
	Número de preguntas: 3	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	

	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!	

	¿Cuánto es 2 x 3? 6
	¡Respuesta correcta!	

	Ha contestado correctamente 2 preguntas
	Le corresponde una nota de 6.7	
	```
	```bash
	Número de preguntas: 1	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	

	Ha contestado correctamente 1 pregunta
	Le corresponde una nota de 10.0
	¡Enhorabuena!
	```

NOTA: **Tienes que entregar sólo el código del apartado 3.**
