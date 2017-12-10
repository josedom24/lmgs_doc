# Boletín Entrega 6: Ejercicios diccionarios, ficheros, ...

1. Realiza el ejercicio 6 del boletín 6. Amplia la funcionalidad del ejercicio 6 del boletín 6, además de decirte si el número de cuenta es válido, te tiene que mostrar el nombre de la identidad bancaría que leerá del fichero (bancos.txt)[doc/bancos.txt]. (2 puntos)

3. Utilizando el ejercicio anterior, crea una aplicación simple de craqueo de contraseñas utilizando los ficheros que puedes encontrar en el repositorio `https://github.com/danielmiessler/SecLists/tree/master/Passwords`.

4. Utilizando el fichero [notas.csv](doc/notas.csv), realiza un programa en python que lea los datos de ese fichero y construya la siguiente estructura: 

        alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
                    {"nombre":"Rafaela", ... },...]

    Crea un programa que te de muestre un menú y puedas elegir una de estas opciones:
    
    * Muestra el listado de los alumnos con la nota media que han sacado. Utiliza una función para realizar el cálculo de la nota media.
    * Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en esa asignatura.
    * Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
    * Pide un curso, y crea un fichero *nombredelcurso*.txt con los alumnos y la nota media.

5. Descarga el fichero [zips.json](docs/zips.json) del sitio de mongodb. Se trata de un listado de los códigos postales de EEUU en formato JSON (lo que Python denomina diccionarios y listas). Realiza los siguientes ejercicios

    * Cuenta el número de códigos postales que aparecen
    * Cuenta el número de códigos postales de cada estado
    * Obtén la URL del mapa de OpenStreetMap de la ciudad de "Akaska" en el estado de Dakota del Sur (SD). Nota: Las coordenadas que aparecen en el fichero zips.json vienen en formato [longitud,latitud] y la url genérica que utiliza OpenStreetMap es:

            http://www.openstreetmap.org/#map=zoom/latitud/longitud

    Por ejemplo:

    [http://www.openstreetmap.org/#map=19/37.27058/-5.91958](http://www.openstreetmap.org/#map=19/37.27058/-5.91958) para ver con un zoom de nivel 19 la ubicación con latitud 37.27058 y longitud -5.91958

6. Modifica el programa anterior para que ahora se pida por teclado la ciudad y el estado que se quiere localizar en OpenStreetMap. El programa te pide una ciudad, si existe te devuelve la URL.

7. [Web scraping](https://es.wikipedia.org/wiki/Web_scraping) es una técnica utilizada mediante programas de software para extraer información de sitios web. Por ejemplo, con el siguiente código podemos leer el HTML de una página web.

        import urllib2
        response = urllib2.urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
        lineas=response.readlines()

En el ejemplo anterior, la página nos da información meteorológica de Dos Hermanas. Haz un programa que te muestre la temperatura, presión y humedad actual de Dos Hermanas.