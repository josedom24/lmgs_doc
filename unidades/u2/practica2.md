# Compilación e interpretación de un programa Java

## Instalación y utilización de JRE

Java Runtime Environment (JRE) son el conjunto de aplicaciones que se instalan en un equipo para que puedan ejecutarse en él aplicaciones java. Los dos componentes principales de un JRE son:

* Java Virtual Machine: Aplicación que ejecuta el código java en bytecode y que está adaptada a la plataforma sobre la que opera.
* Bibliotecas Java

Existen diferentes implantaciones de JRE, siendo la última versión estable la 1.8, conocida como Java 8. Actualmente el propietario de Java es la empresa Oracle y ha modificado la antigua licencia libre de Java, por lo que ya no es posible que se distribuya legalmente en las distribuciones de software libre. Nosotros optaremos por utilizar OpenJDK, que es una implementación libre de Java.

Instalación de openjdk jre 8 en Debian Jessie:
* Busca el paquete openjdk-8-jre
* Si no lo tienes instalado en tu equipo, instálalo
* Como hay varios paquetes alternativos que implementan jre, hay que elegir el que queremos utilizar en nuestro equipo, para ello hay que hacer:

	```bash
	update-alternatives --config java
	```

y elegir la opción de openjdk8.

Instalación de sun jre 8 en Windows:

* Comprueba si tienes instalada la versión 8 de JRE en tu equipo, si no es así, entra en el sitio de [descargas](http://www.oracle.com/technetwork/java/javase/downloads/index.html), descárgate la versión de JRE para Windows e instálala.
* Ejecución de la misma aplicación en las dos plataformas
* Entra en el sitio http://www.jedit.org y descárgate la versión multiplataforma de este editor, no la de linux ni windows.
* Comprueba que puedes ejecutar esa misma aplicación en las dos plataformas.
