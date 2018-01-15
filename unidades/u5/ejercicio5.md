# Inventar un lenguaje XML para almacenar los datos de préstamo de los libros de una biblioteca

Se quiere guardar en un fichero XML la información generada por los prestamos de libros en una biblioteca. Para ello ten en cuenta los siguientes aspectos:

* De cada libro guardamos varios datos: código ISBN, nombre, editorial, año de publicación, autor.
* De cada libro podemos tener uno o varios ejemplares. Cada ejemplar se diferencia de otro por un código numérico.
* Se prestan los ejemplares, y de cada prestamos hay que indicar el ejemplar del libro, el socio al que se ha prestado y la fecha de prestamo.
* Del socio hay que guadar DNI, nombre y dirección.