# Trabajando con variables

Las variables en python no se declaran, se determina su tipo en tiempo de ejecución empleando una técnica que se lama **tipado dinámico**.

	
## Operadores de asignación

Me permiten asignar una valor a una variable, o mejor dicho: me permiten cambiar la referencia a un nuevo objeto.

El operador principal es `=`:

	>>> a = 7
	>>> a
	7

Podemos hacer diferentes operaciones con la variable y luego asignar, por ejemplo sumar y luego asignar.

	>>> a+=2
	>>> a
	9

Otros operadores de asignación: `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

## Asignación múltiple

En python se permiten asignaciones múltiples de esta manera:

	>>> a, b, c = 1, 2, "hola"