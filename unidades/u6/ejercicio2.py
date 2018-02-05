from lxml import etree

### Ejercicio 1
def usuarios(arbol):
	lista=[]
	usuarios=arbol.findall("user")
	for user in usuarios:
		lista.append(user.find("firstname").text+" "+user.find("lastname").text)
	return lista

### Ejercicio2
def avatar(arbol):
	lista=[]
	usuarios=arbol.findall("user")
	for user in usuarios:
		if user.find("picture").text=="1":
			lista.append(user.find("firstname").text+" "+user.find("lastname").text)
	return lista

### Ejercicio3
def acceso_desde_fuera(arbol):
	lista=[]
	usuarios=arbol.findall("user")
	for user in usuarios:
		if user.find("lastip").text[:6]!="172.22":
			lista.append(user.find("email").text)
	return lista


### Ejercicio4
def buscar(cadena,arbol):
	lista=[]
	usuarios=arbol.findall("user")
	for user in usuarios:
		if user.find("firstname").text.startswith(cadena):
			lista.append(user.find("firstname").text+" "+user.find("lastname").text)
	return lista


### Ejercicio 5
### Voy a hacer un diccionario, cada elemento del diccionario tendrá como clave el nombre de la localidad y como valor 
### tendrá una lista con los usuarios

def lista_por_localidad(arbol):
	dic_usuarios={}
	# Lo primero es crear una lista con las localidades:
	lista_localidades=[]
	usuarios=arbol.findall("user")
	for user in usuarios:
		if user.find("city").text not in lista_localidades:
			lista_localidades.append(user.find("city").text)
	# Ahora recorre la lista_localidaes y me quedo con los usuarios de esa localidad
	for loc in lista_localidades:
		# Voy creando el diccionario, creo un elemento con la key igual a la localidad y como valor una lista vacia
		dic_usuarios[loc]=[]
		for user in usuarios:
			if user.find("city").text==loc:
				dic_usuarios[loc].append(user.find("firstname").text+" "+user.find("lastname").text)
	return dic_usuarios

### Ejercicio 6
def ultimo_acceso(arbol):
	lista=[]
	ultimos_accesos=arbol.findall("user/lastaccess")
	lua=[]
	for ua in ultimos_accesos:
		lua.append(int(ua.text))
	lua.sort(reverse=True)
	for ua in lua:
		usuarios=arbol.findall("user")
		for user in usuarios:
			if int(user.find("lastaccess").text)==ua:
				lista.append(user.find("firstname").text+" "+user.find("lastname").text)	
	return lista		

arbol = etree.parse('users.xml')

### Ejercicio 1
print(usuarios(arbol))

### Ejercicio 2
print(avatar(arbol))

### Ejercicio 3
print(acceso_desde_fuera(arbol))

### Ejercicio 4
cad=input("Dame el nombre:")
print(buscar(cad,arbol))

### Ejercicio 5
dic=lista_por_localidad(arbol)
for key,value in dic.items():
	print(key)
	print("="*len(key))
	for user in value:
		print(user)

### Ejercicio 6
print(ultimo_acceso(arbol))
