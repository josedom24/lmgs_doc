from lxml import etree


def lista_provincias(arbol):
# Buscamos subelementos dentro de él
# Para cada elemento se definen 3 propiedades fundamentales:
# elemento.tag, elemento.text y elemento.attrib
# Obtenemos una lista donde cada elemento es una provincia
	lista=[]
	nombres = arbol.findall('provincia/nombre')	
	for nombre in nombres:
		lista.append(nombre.text)
	return lista

def lista_poblaciones(arbol):
	lista=[]
	provincias = arbol.findall('provincia')
	for provincia in provincias:
		localidades = provincia.findall('localidades/localidad')
		for localidad in localidades:
			lista.append(localidad.text)
	return lista

def lista_provincias_total_poblaciones(arbol):
	lista=[]
	provincias = arbol.findall('provincia')
	# Recorremos la lista de provincias
	for provincia in provincias:
	# Obtenemos el nombre de la provincia
		nombre = provincia.find('nombre')
		# Para cada provincia almacenamos los elementos <localidad > en una lista
		localidades = provincia.findall('localidades/localidad')
		# Imprimimos el nombre de la provincia y la longitud de la
		# lista localidades que es igual al número de localidades
		lista.append((nombre.text, len(localidades)))
	return lista


def poblaciones(prov,arbol):
	lista=[]
	provincias = arbol.findall('provincia')
	# Pedimos al usuario el nombre de la provincia:
	# Recorremos la lista de provincias
	for provincia in provincias:
		# Obtenemos el nombre de la provincia
		nombre = provincia.find('nombre')
		
		if nombre.text == prov:
		# Almacenamos los elementos <localidad > en una lista
			localidades = provincia.findall('localidades/localidad')
			print(localidades)
			for localidad in localidades:
				lista.append(localidad.text)
			break
	return lista


# Creamos el objeto arbol desde el fichero XML
# Este objeto es de tipo ElementTree
arbol = etree.parse('provinciasypoblaciones.xml')


#Ejercicio 1
for nombre in lista_provincias(arbol):
	print (nombre)

#Ejercicio 2
for nombre in lista_poblaciones(arbol):
	print (nombre)

# Ejercicio 3

for nombre ,total in lista_provincias_total_poblaciones(arbol):
	print (nombre,total)

# Ejercicio 4
for nombre in poblaciones("Sevilla",arbol):
	print (nombre)

