from lxml import etree


#Ejercicio 1
def calles(arbol):
	lista=[]
	for calle in arbol.findall("way"):
		tags=calle.findall("tag")
		for tag in tags:
			if tag.attrib["k"]=="highway":
					lista.append(calle.attrib["id"])
	return lista


# Ejercicio 2

def calles_con_nombre(arbol):
	lista=[]
	for calle in arbol.findall("way"):
		tags=calle.findall("tag")
		band=False
		for tag in tags:
			
			if tag.attrib["k"]=="highway":
				band=True
		if band:
			for tag in tags:
				if tag.attrib["k"]=="name":
					lista.append(tag.attrib["v"])
	return lista

# Ejercicio 3

def nodos(arbol):
	lista=[]
	nodes=arbol.findall("node")
	for node in nodes:
		if node.attrib["uid"]=="384182" and len(node.findall("tag"))>0:
			lista.append(node.attrib["id"])
	return lista

def supermecados(arbol):
	cont=0
	tags=arbol.findall("way/tag")
	for tag in tags:
		if tag.attrib["k"]=="shop" and tag.attrib["v"]=="supermarket":
			cont+=1
	return cont

arbol = etree.parse('utrera.xml')

## Ejercicio1
print(calles(arbol))

## Ejercicio2
print(calles_con_nombre(arbol))

## Ejercicio3
print(nodos(arbol))

## Ejercicio4
print(supermecados(arbol))
