# Ejercicio: Mapa de Utrera

Utiliza el fichero [Utrera.xml](https://github.com/josedom24/lmgs_doc/raw/master/unidades/u6/doc/utrera.xml.zip), realiza varias funciones python que devuelvan la siguiente información:

* Calles de Utrera (elementos "way" con un elemento hijo "tag" que tenga el atributo k="highway").Mostrar el `id`.
* Calles de Utrera con nombre (elementos "way" con un elemento hijo "tag" que tenga el atributo `k="highway"` y el atributo `k="name"`). Mostrar el nombre.
* Nodos de Utrera (mostrar el `id` editados por el usuario "384182" y que tienen algún elemento hijo `tag`.
* Número de supermecados de Utrera (hay que buscar elementos del tipo `<tag k="shop" v="supermarket"/>`).


Realiza los mismos ejercicios utilizando expresiones XPath.