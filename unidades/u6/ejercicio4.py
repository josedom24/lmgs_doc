from lxml import etree

# Ejercicio 1

def calles(arbol):
	lista=[]
	for a in arbol.findall("way"):
		tags=a.findall("tag")
		band=False
		for tag in tags:
			
			if tag.attrib["k"]=="highway":
				band=True
		if band:
			for tag in tags:
				if tag.attrib["k"]=="name":
					lista.append(tag.attrib["v"])
	return lista

# Ejercicio 2
for node in nodes:
    ...:     if node.attrib["uid"]=="384182" and len(node.findall("tag"))>0:
    ...:         print(node.attrib["id"])


arbol = etree.parse('utrera.xml')

## Ejercicio1
print(calles(arbol))

