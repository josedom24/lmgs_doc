# Trabajando con YAML desde python3: pyyaml.yaml

## Instalación

En debian/Ubuntu instalamos el gestor de paquetes python pip:

	apt-get install python3-pip

E instalamos el páquete:

	pip install PyYAML

## Leer un fichero YAML

Si tenemos el fichero books.yaml:

	---
	bookstore: 
  		book: 
	    - title: 
	        _lang: "en"
	        __text: "Everyday Italian"
	      author: "Giada De Laurentiis"
	      year: "2005"
	      price: "30.00"
	      _category: "COOKING"
	    
	    - title: 
	        _lang: "en"
	        __text: "Harry Potter"
	      author: "J K. Rowling"
	      year: "2005"
	      price: "29.99"
	      _category: "CHILDREN"
	    
	    - title: 
	        _lang: "en"
	        __text: "XQuery Kick Start"
	      author: 
	        - "James McGovern"
	        - "Per Bothner"
	        - "Kurt Cagle"
	        - "James Linn"
	        - "Vaidyanathan Nagarajan"
	      year: "2003"
	      price: "49.99"
	      _category: "WEB"
	    
	    - title: 
	        _lang: "en"
	        __text: "Learning XML"
	      author: "Erik T. Ray"
	      year: "2003"
	      price: "39.95"
	      _category: "WEB"

Podríamos hacer un programa como este:

	import yaml   
	with open("books.yaml") as fichero:
		doc=yaml.load(fichero)

	>>> type(doc)
	dict

## Obteniendo información

### Cantidad de libros

	>>> len(doc["bookstore"]["book"])
	4

### Títulos de los libros

	for libro in doc["bookstore"]["book"]:
   		print(libro["title"]["__text"])

### Autores de los libros

	for libro in doc["bookstore"]["book"]:
        if isinstance(libro["author"],list):
            for autor in libro["author"]:
                print(autor)
        else:
            print(libro["author"])
