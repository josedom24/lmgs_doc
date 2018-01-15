# Git y GitHub

Utilizaremos git para realizar el control de versiones de los proyectos que realicemos en la asignatura. Deberás ir realizando los proyectos de forma incremental, y registrar los cambios (commits) realizados.

Los cambios realizados en el código fuente del proyecto se guardan en el repositorio local y después se publicarán en GitHub, en un repositorio remoto propio. Allí se podrán consultar todos los cambios realizados, sus fechas, sus descripciones, y se podrán compartir con otros compañeros y el profesor.

Los repositorios subidos a la versión gratuita de GitHub son públicos y convierten la cuenta personal de GitHub en un perfecto escaparate y portafolio de proyectos desarrollados. Cada vez son más las empresas que piden un buen expediente en GitHub. La visibilidad y transparencia de GitHub lo convierten también en una herramienta fundamental para aprender. 

Un objetivo de la asignatura es participar en este movimiento de código abierto y colaborar con nuestros proyectos para que otros puedan aprender de ellos (y, al mismo tiempo, mejorar el portafolio y el curriculum personal de cara a futuros trabajos).

## Empecemos

1. Crea una cuenta en GitHub y envía un correo a pledin.jd@gmail.com con la dirección de tu página GitHub y tu nombre completo. La forma de acceder a los repositorios remotos de GitHub va a ser por SSH, por lo tanto debes copiar tu clave pública a GitHub, para ello:
	* Copia el contenido de tu fichero ~/.ssh/id_rsa.pub, para ello: añade una nueva clave SSH en el apartado "SSH keys" de tu perfil en GitHub y pega el contenido de tu clave pública.
	* Si no tienes ese fichero, puedes generar una nueva clave ssh pública: [http://librosweb.es/pro_git/capitulo_4/generando_tu_clave_publica_ssh.html](http://librosweb.es/pro_git/capitulo_4/generando_tu_clave_publica_ssh.html).

2. Crea en GitHub un repositorio con el nombre **prueba** (inicializa el repositorio con un fichero README) y la descripción **Repositorio de prueba**.
3. Instala git en tu ordenador.

		apt-get install git

4. Copia la url SSH del repositorio (no copies la URL https) y vamos a clonar el repositorio en nuestro ordenador.

		git clone git@github.com:josedom24/prueba.git

5. Entramos en el nuestro repositorio local y configuramos git:

		cd prueba
		git config --global user.name "Pepito Pérez"
		git config --global user.email pepito.perez@gmail.com
		git commit --amend --reset-author

	Comprueba que dentro del repositorio que hemos creado se encuentra el fichero README.md, en este fichero podemos poner la descripción del proyecto.

6. Vamos a crear un nuevo fichero, lo vamos a añadir a nuestro repositorio local y luego lo vamos a sincronizar con nuestro repositorio remoto de GitHub. Cada vez que hagamos una modificación en un fichero lo podemos señalar creando un commit. Los mensajes de los commits son fundamentales para explicar la evolución de un proyecto. Un commit debe ser un conjunto pequeño de cambios de los ficheros del proyecto con una cierta coherencia.

		echo "Esto es una prueba">ejemplo.txt
		git add ejemplo.txt
		git commit -m "He creado el fichero ejemplo.txt"
		git push

7. Si modificas un fichero en tu repositorio local, no tienes que volver a añadirlo a tu repositorio (**git add**). Pero tienes que usar la opción -a al hacer el commit.

		git commit -am "He modificado el fichero ejemplo.txt"
		git push

8. Si quieres cambiar el nombre de un fichero o directorio de tu repositorio:

		git mv ejemplo.txt ejemplo2.txt
		git commit -am "He cambiado el nombre del fichero"
		git push

9. Si quieres borrar un fichero de tu repositorio:

		git rm ejemplo2.txt
		git commit -am "He borrado el fichero ejemplo2"
		git push

10. Puedes clonar tu repositorio de GitHub en varios ordenadores (por ejemplo, si quieres trabajar en tu casa y en el instituto), por lo tanto antes de trabajar en un repositorio local tienes que sincronizar los posibles cambios que se hayan producido en el repositorio remoto, para ello:

		git pull

11. Para comprobar el estado de mi repositorio local:

		git status


Si te quieres hacerte un experto de [Pro Git, el libro oficial de Git](http://librosweb.es/pro_git/)

