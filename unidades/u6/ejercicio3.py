from lxml import etree

# Ejercicio 1

def latitudylongitud(arbol):
	latitud=arbol.find("localizacion/latitud").text
	longitud=arbol.find("localizacion/longitud").text
	return latitud,longitud

# Ejercicio 2

def actual(arbol):
	temp=arbol.find("condiciones_actuales/temperatura").text
	viento=arbol.find("condiciones_actuales/viento").text+" "+arbol.find("condiciones_actuales/viento").attrib["direccion"]
	humedad=arbol.find("condiciones_actuales/humedad").text
	return temp,viento,humedad

# Ejercicio 3
# Voy a crear un diccionario: key la fecha, y valor: temperatura máxima y mínima en una tubla
def pronostico(arbol):
	pro={}
	pronostico=arbol.findall("pronostico_dias/dia")
	for dia in pronostico:
		pro[dia.attrib["fecha"]]=(dia.find("maxima").text,dia.find("minima").text)

	return pro

# Ejercicio 4
def buscar(fecha,hora,arbol):
	pronostico=arbol.findall("pronostico_horas/hora")
	for pro in pronostico:
		if pro.attrib["id"]==hora and pro.attrib["fecha"]==fecha:
			temp=pro.find("temperatura").text
			viento=pro.find("viento").text+" "+pro.find("viento").attrib["direccion"]
			humedad=pro.find("humedad").text
			return temp,viento,humedad
	return None

arbol = etree.parse('sevilla.xml')

### Ejercicio 1
lat,lon=latitudylongitud(arbol)
print("Latitud: %s"%lat)
print("Longitud: %s"%lon)

### Ejercicio2
t,v,h=actual(arbol)
print("Temperatura: %s"%t)
print("Viento: %s"%v)
print("Humedad: %s"%h)

### Ejercicio3
pronostico=pronostico(arbol)
for fecha,temp in pronostico.items():
	print(fecha)
	print(temp[0])
	print(temp[1])

### Ejercicio4
t,v,h=buscar("2016-02-27","13:00:00",arbol)
print("Temperatura: %s"%t)
print("Viento: %s"%v)
print("Humedad: %s"%h)
