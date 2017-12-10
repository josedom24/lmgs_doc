# Boletín Entrega 6: Ejercicios diccionarios, ficheros, ...

### Ejercicio 1

Realiza el ejercicio 6 del boletín 6. Amplia la funcionalidad del ejercicio 6 del boletín 6, además de decirte si el número de cuenta es válido, te tiene que mostrar el nombre de la identidad bancaria que leerá del fichero [bancos.txt](doc/bancos.txt). (2 puntos)

### Ejercicio 2

Implementa un sistema completo de validación de usuarios en una máquina con Debian, que tiene las siguientes características:

* El nombre de usuario y las contraseñas se almacenan en el fichero `/etc/shadow`, al que tiene acceso sólo el usuario root.
* Las contraseñas se almacenan como un hash AES512 con sal

Ayuda:

Supongamos que tenemos en nuestro sistema el usuario `prueba` con contraseña `asdasd`, una línea correspondiente a este usuario en el fichero `/etc/shadow` sería:

	prueba:$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxulWX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.:15059:0:99999:7::::

* La sal de una contraseña cifrada se indica en linux por los 12 primeros caracteres del hash de la contraseña, en el caso anterior la sal sería **$6$/nNkCgcv$**.
* La función `crypt` del módulo `crypt` permite formar los hashes con sal utilizados por linux, de la siguiente manera:

    ```python
    >>> from crypt import crypt
	>>> crypt('asdasd','$6$/nNkCgcv$')
	'$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxul\WX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.'
    ```

donde `asdasd` es la contraseña en claro.

### Ejercicio 3

Utilizando el ejercicio anterior, crea una aplicación simple de craqueo de contraseñas utilizando los ficheros que puedes encontrar en el [repositorio](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

### Ejercicio 4

Utilizando el fichero [notas.csv](../../doc/notas.csv), realiza un programa en python que lea los datos de ese fichero y construya la siguiente estructura: 

    alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
                    {"nombre":"Rafaela", ... },...]

Crea un programa que muestre un menú y puedas elegir una de estas opciones:
    
* Muestra el listado de los alumnos con la nota media que han sacado. Utiliza una función para realizar el cálculo de la nota media.
* Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en esa asignatura.
* Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
* Pide un curso, y crea un fichero *nombredelcurso*.txt con los alumnos y la nota media.

### Ejercicio 5

Descarga el fichero [zips.json](docs/zips.json) del sitio de mongodb. Se trata de un listado de los códigos postales de EEUU en formato JSON (lo que Python denomina diccionarios y listas). Realiza los siguientes ejercicios

* Cuenta el número de códigos postales que aparecen
* Cuenta el número de códigos postales de cada estado
* Obtén la URL del mapa de OpenStreetMap de la ciudad de "Akaska" en el estado de Dakota del Sur (SD). Nota: Las coordenadas que aparecen en el fichero zips.json vienen en formato [longitud,latitud] y la url genérica que utiliza OpenStreetMap es:

        http://www.openstreetmap.org/#map=zoom/latitud/longitud

Por ejemplo:

[http://www.openstreetmap.org/#map=19/37.27058/-5.91958](http://www.openstreetmap.org/#map=19/37.27058/-5.91958) para ver con un zoom de nivel 19 la ubicación con latitud 37.27058 y longitud -5.91958

### Ejercicio 6

Modifica el programa anterior para que ahora se pida por teclado la ciudad y el estado que se quiere localizar en OpenStreetMap. El programa te pide una ciudad, si existe te devuelve la URL.

### Ejercicio 7

[Web scraping](https://es.wikipedia.org/wiki/Web_scraping) es una técnica utilizada mediante programas de software para extraer información de sitios web. Por ejemplo, con el siguiente código podemos leer el HTML de una página web.

    from urllib.request import urlopen
    response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
    lineas=response.readlines()

En el ejemplo anterior, la página nos da información meteorológica de Dos Hermanas. Haz un programa que te muestre la temperatura, presión y humedad actual de Dos Hermanas.