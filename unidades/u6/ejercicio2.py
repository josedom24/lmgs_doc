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