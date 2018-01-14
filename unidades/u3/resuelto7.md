# Solución boletín 5: Ejercicios de funciones

1. Escribir dos funciones que permitan calcular:

    * La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    * La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

		def calcular_segundos(horas,minutos,segundos):
			return horas*3600+minutos*60+segundos			

		def calcular_horas(segundos):
			horas = segundos // 3600
			segundos-=horas*3600
			minutos = segundos // 60
			segundos-=minutos*60
			return horas,minutos,segundos


2. Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:

    * Si recibe un argumento, supone que son segundos y convierte a horas, minutos y segundos.
    * Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.

	    def calcular(*args):
		if len(args)==1:
			return calcular_horas(args[0])
		elif len(args)==3:
			return calcular_segundos(*args)
		else:
			raise TypeError("Se espera 1 o 3 parámetros")

3. Queremos hacer una función que añada a una lista los contactos de una agenda. Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre, el campo del teléfono, aunque puede tener más campos. Los datos se irán pidiendo por teclado, se pedirá de antemanos cuantos contactos se van a guardar. Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el `*`. 

		def guardar_agenda(l_agenda,**kwargs):
			l_agenda.append(kwargs)
			return l_agenda			

		def main():
			agenda=[]
			cantidad = int(input("¿Cuántos contactos vas a introducir?"))
			for i in range(cantidad):
				contacto={}
				contacto["nombre"]=input("Indica el nombre:")
				contacto["telefono"]=input("Indica el teléfono:")
				campo=input("Introuzca otro campo:")
				while campo!="*":
					contacto[campo]=input("Introuzca valor:")
					campo=input("Introuzca otro campo:")
				agenda=guardar_agenda(agenda,**contacto)
			print(agenda)			

		if __name__ == '__main__':
			 main()

4. Amplía el programa anterior para hacer una función de búsqueda, que reciba un conjunto de parámetros keyword y devuelve los contactos (en una lista) que coincidan con los criterios de búsqueda.

		def buscar(l_agenda,**kwargs):
			lista_aciertos=[]
			for contacto in l_agenda:
				aciertos=0
				for campo,valor in kwargs.items():
					if campo in contacto and contacto[campo]==valor:
						aciertos+=1
				if aciertos==len(kwargs):
					lista_aciertos.append(contacto)
			return lista_aciertos			

		def main():
			...
			
			## Búsqueda
			filtro={}
			campo=input("Introduzca un campo para buscar:")
			while campo!="*":
				filtro[campo]=input("Introduzca valor a buscar:")
				campo=input("Introduzca otro campo a buscar:")
			print(buscar(agenda,**filtro))

5. Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista.

		def multiplicar(lista):
			if len(lista)==1:
				return lista[0]
			else:
				return lista.pop()*multiplicar(lista)			

		if __name__ == '__main__':
			print(multiplicar([3,4,5]))