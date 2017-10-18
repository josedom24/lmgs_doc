# Estructura de control: Repetitivas

## while

La estructura `while` nos permite repetir un bloque de instrucciones mientras al evaluar una expresión lógica nos devuelve True. Puede tener una estructura `else` que se ejecutará al terminar el bucle.

*Ejemplo*

	año = 2001 
	while año <= 2017: 
    	print ("Informes del Año", año) 
    	año += 1
    else:
    	print ("Hemos terminado")

## for

La estructura `for` nos permite iterar los elementos de una secuencia (lista, rango, tupla, diccionario, cadena de caracteres,...). Puede tener una estructura `else` que se ejecutará al terminar el bucle.

*Ejemplo*

	for i in range(1,10):
        print (i)
	else:
        print ("Hemos terminado")

## Instrucciones break y continue 

### break

Termina la ejecución del bucle, además no ejecuta el bloque de instrucciones indicado por la parte `else`.

### continue
	
Deja de ejecutar las restantes instrucciones del bucle y vuelve a iterar.


