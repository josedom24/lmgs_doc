# Solución boletín 5: Ejercicios cadenas

1. Crear un programa que lea por teclado una cadena, y muestre la siguiente información:

	* Imprima los dos primeros caracteres.
    * Imprima los tres últimos caracteres.
    * Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
    * Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
    * Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer.

    	cad=input("Cadena:")
		print(cad[:2])
		print(cad[-2:])
		print(cad[::2])
		print(cad[::-1])
		print(cad+cad[::-1])

2. Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

		cad=input("Cadena:")
		caracter=input("Caracter:")
		print(cad.replace("",caracter)[1:-1])

3. Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los espacios por el carácter. Ej: mi archivo de texto.txt y \_ debería devolver mi\_archivo\_de\_texto.txt

		cad=input("Cadena:")
		caracter=input("Caracter:")
		print(cad.replace(" ",caracter))

4. Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería devolver su clave es: XXXX

		cad=input("Cadena:")
		caracter=input("Caracter:")
		for i in range(0,9):
			cad=cad.replace(str(i),caracter)
		print(cad)

5. Crear un programa que lea por teclado una cadena y un carácter, e inserte el caracter cada 3 dígitos en la cadena. Ej. 2552552550 y . debería devolver 255.255.255.0

		cad=input("Número:")
		car=input("Caracter:")
		cont=0
		cad2=""
		for c in cad:
		    if cont!=0 and cont%3==0:
		        cad2=cad2+car
		    cad2=cad2+c
		    cont=cont+1
		print(cad2)

6.  Escribir una función que reciba una cadena que contiene un número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver 1.234.567.890.

		num=int(input("Número:"))
		cad=str(num)
		cad2=""
		cont=1
		for caracter in cad[::-1]:
			cad2=caracter+cad2
			if cont%3==0:
				cad2="."+cad2
			cont=cont+1
		print(cad2)

7. Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

	* La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
	* Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
	* Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.

			cad=input("Cadena:")			

			# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
			lista=cad.split(" ")
			for palabra in lista:
				print(palabra[0],)
			print("")
			# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
			for palabra in lista:
				print(palabra.capitalize(),)
			print(""			)

			# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
			for palabra in lista:
				if palabra.startswith("a") or palabra.startswith("A"):
					print(palabra,)

8.  Escribir funciones que dadas dos cadenas de caracteres:

    * Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
    * Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe kde y gnome debe devolver gnome.

    		cad1=input("Cadena 1:")
		    cad2=input("Cadena 2:")	
			

		    if cad1.find(cad2)>-1:
		    	print("cad2 es subcadena de cad1")
		    else:
		    	print("cad2 no es subcadena de cad1"		)

		    if cad1<cad2:
		    	print(cad1)
		    else:
		    	print(cad2)

9. Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.

		cad1=input("Numero binario:")		

		cont=0
		decimal=0
		for num in cad1[::-1]:
			if num=="1":
				decimal=decimal+(2**cont)
			cont=cont+1
		print(decimal)
