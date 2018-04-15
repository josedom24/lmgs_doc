# Proyecto 3ª evaluación: Utilización de API web

## Objetivo

El objetivo fundamental del proyecto es la realización de una página web alojada en Heroku y creada con el web framework python Flask, que utilizando algún servicio web proporcione una funcionalidad original.

## Proceso

El proceso de realización del proyecto tendrá las siguientes etapas:

* Estudio y búsqueda de uno o varios servicios web (API Restful). Se tendrá en cuenta que tipo de autentificación nos ofrece, así cómo el tipo de los datos que nos devuelve. 
* Una vez que se ha elegido la API con la que se va a trabajar, se entregará un "anteproyecto" explicando los objetivos y funcionalidades del proyecto. El profesor lo valorará y el alumno podrá empezar la implementación. 
* Codificación del proyecto: El alumno empezará a construir la página web alojada en Heroku. Al mismo tiempo todos los cambios que vaya realizando se registrarán en un repositorio GitHub.
* Una vez concluido el proyecto se mostrará su funcionamiento al profesor.

## Pre-evaluación del proyecto

Para hacer una estimación de la nota que puedes sacar en el proyecto se seguirán los siguientes criterios de evaluación:

* ¿Cuántas API web vas a usar en el proyecto? 
	* Sólo una, **1 punto**
	* Más de una, **2 puntos**
* ¿Qué métodos vas a usar en las llamada a la API?, es decir, ¿vas a consumir información del servicio web (métodos GET)?, o también, ¿vas a interactuar con el servicio web (métodos POST, PUT, DELETE,...)?
	* Sólo GET, **1 punto**
	* GET, POST, ..., **2 puntos**
* ¿Qué tipo de autentificación tiene la API utilizada?
	* Es libre, con usuario/contraseña o con API key, **1 punto**
	* Utiliza sistemas de autentificación 7 autorización como oauth1 o oauth2, **2 puntos**.
* ¿Cuantas cosas hace la aplicación?, podemos pensar cuantos @route va a tener nuestro programa Flask:
	* 4 o menos, **1 punto**
	* Más de 4, **2 puntos**
* ¿Tu página web tiene hoja de estilo y es válida?
	* Si, **1 punto**
	* No, **0 puntos**
* Crees que vas a utilizar algo adicional, para alcanzar el 10 (por ejemplo, utilizar una API de mapas, crear un servicio innovador,...) :
	* Si, **1 punto**
	* No, **0 puntos**


## ¿Qué debe entregar el alumno?

### Anteproyecto

Es el enunciado del proyecto que se debe entregar antes de comenzar la etapa de codificación se tendrán que indicar los siguientes apartados:

* Nombre del proyecto:
* Objetivos, descripción y funcionalidad del proyecto:
* URL del repositorio GitHub:
* URL de la página web:

* ¿Cuántas API web vas a usar en el proyecto?: 
	* URL de la API(s) utilizada(s):
	* Lenguaje(s) de marcas que utiliza(n) la(s) API:
	* ¿Qué tipo de autentificación tiene(n) la(s) API utilizada(s)?:
	* ¿Qué métodos vas a usar en las llamada a la API?, es decir, ¿vas a consumir información del servicio web (métodos GET)?, o también, ¿vas a interactuar con el servicio web (métodos POST, PUT, DELETE,...)?:

* ¿Cuantas cosas hace la aplicación?, podemos pensar cuantos @route va a tener nuestro programa Flask:
* ¿Vas a hacer una página web válida y con hoja de estilo?
* Comenta cualquier cosa que crees que puedes hacerte conseguir un 10 en el proyecto:

## ¿Qué debe enseñar al profesor el alumno?

* APIs: La documentación de las APIs elegidas para realizar el proyecto.
* PÁGINA WEB: Me tienes que enseñar el diseño de la página web, hoja de estilo, estructura, validación, ...
* FORMULARIO: Me tienes que enseñar el primer formulario que tenga tu página web.
* REQUEST: Me tienes que enseñar la primera petición que hagas en tu aplicación.
* PLANTILLA: Me tienes que enseñar la página web dinámica generada a partir de una plantilla a la cual le mandamos información obtenida de una petición al servidor web.

## Evaluación final

La evaluación final del proyecto se realizará teniendo en cuenta los siguientes aspectos:

* Puntuación técnica del proyecto (teniendo en cuenta la valoración del apartado **Pre-evaluación del proyecto**) (70%).
* Asistencia a clase y participación activa en el proyecto: Es importante hablar, preguntar, discutir con el profesor acerca de tu proyecto. Sería muy importante que desde el primer momento el profesor supiera que vas a hacer, que problemas tienes, por donde vas, ... En este punto también se tendrá en cuenta los puntos que hemos indicado que debes enseñar al profesor.(20%).
* Corrección del proyecto: Se valorará el repositorio GitHub entregado (debe tener un fichero `README.md` explicando de forma clara el contenido del repositorio), además la corrección se realizará de la aplicación web ejecutándose en Heroku.