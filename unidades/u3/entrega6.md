# Boletín Entrega 6: Ejercicios diccionarios, ficheros, ...

1. Realiza el ejercicio 6 del boletín 6. Amplia la funcionalidad del ejercicio 6 del boletín 6, además de decirte si el número de cuenta es válido, te tiene que mostrar el nombre de la identidad bancaría que leerá del fichero (bancos.txt)[doc/bancos.txt]. (2 puntos)

2. Implementa un sistema completo de validación de usuarios en una máquina con Debian, que tiene las siguientes características:
	* El nombre de usuario y las contraseñas se almacenan en el fichero `/etc/shadow`, al que tiene acceso sólo el usuario root.
	* Las contraseñas se almacenan como un hash AES512 con sal

	Ayuda:
	Supongamos que tenemos en nuestro sistema el usuario `prueba` con contraseña `asdasd`, una línea correspondiente a este usuario en el fichero `/etc/shadow` sería:

		prueba:$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxulWX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.:15059:0:99999:7::::

	* La sal de una contraseña cifrada se indica en linux por los 12 primeros caracteres del hash de la contraseña, en el caso anterior la sal sería `$6$/nNkCgcv$`.
	* La función `crypt` del módulo `crypt` permite formar los hashes con sal utilizados por linux, de la siguiente manera:

		>>> from crypt import crypt
		>>> crypt('asdasd','$6$/nNkCgcv$')
		'$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxul\WX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.'

	donde `asdasd` es la contraseña en claro.

