from lxml import etree

### Ejercicio 1
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

### Ejercicio 2
def lista_poblaciones(arbol):
	lista=[]
	provincias = arbol.findall('provincia')
	for provincia in provincias:
		localidades = provincia.findall('localidades/localidad')
		for localidad in localidades:
			lista.append(localidad.text)
	return lista

### Ejercicio 3
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

### Ejercicio 4
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

### Ejercicio 5
def provincia(nombre_localidad,arbol):
	localidades=arbol.findall('provincia/localidades/localidad')
	for localidad in localidades:
		if localidad.text==nombre_localidad:
			for padre in localidad.iterancestors():
				if padre.tag=="provincia":
					return padre.find("nombre").text

### Ejercicio 6
def provincias_por_identificador(lista_id,arbol):
	lista=[]
	provincias= arbol.findall('provincia')
	for provincia in provincias:
		if provincia.attrib["id"] in lista_id:
			nombre=provincia.find("nombre").text
			localidades=provincia.findall("localidades/localidad")
			lista_localidades=[]
			for localidad in localidades:
				lista_localidades.append(localidad.text)
			lista.append((nombre,lista_localidades))
	return lista

### Ejercicio 7
def localidades_grandes(prov,arbol):
	lista=[]
	provincias= arbol.findall('provincia')
	for provincia in provincias:
		nombre = provincia.find('nombre')
		if nombre.text == prov:
			localidades = provincia.findall('localidades/localidad')
			for localidad in localidades:
				if localidad.attrib["c"]=="1":
					lista.append(localidad.text)
			break
	return(lista)

### Ejercicio 8
def localidad_grande(nombre_localidad,arbol):
	localidades=arbol.findall('provincia/localidades/localidad')
	for localidad in localidades:
		if localidad.text==nombre_localidad and localidad.attrib["c"]=="1":
			for padre in localidad.iterancestors():
				if padre.tag=="provincia":
					return padre.find("nombre").text
	return None

# Creamos el objeto arbol desde el fichero XML
# Este objeto es de tipo ElementTree
arbol = etree.parse('provinciasypoblaciones.xml')


#Ejercicio 1
for nombre in lista_provincias(arbol):
	print (nombre)

##Ejercicio 2
for nombre in lista_poblaciones(arbol):
	print (nombre)

## Ejercicio 3#
for nombre ,total in lista_provincias_total_poblaciones(arbol):
	print (nombre,total)

## Ejercicio 4
for nombre in poblaciones("Dos Hermanas",arbol):
	print (nombre)

# Ejercicio 5
print(provincia("Utrera",arbol))

# Ejercicio 6
print(provincias_por_identificador(["01","02"],arbol))

# Ejercicio 7
print(localidades_grandes("Sevilla",arbol))

# Ejercicio 8
print(localidad_grande("Sevilla",arbol))
