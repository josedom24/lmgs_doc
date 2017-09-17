# Compilación y ejecución de un lenguaje compilado: C

Todas las distribuciones GNU/Linux incluyen alguna versión del GNU Project C and C++ Compiler (gcc), vamos a utilizarlo.

1. Crea el fichero `helloworld.c` con el siguiente contenido:

	```c
	#include <stdio.h>
	int main(void) 
	{ 
           printf("Hello world!\n"); 
           return 0; 
	} 
	```

2. Compílalo con gcc:

   ```bash
   gcc helloworld.c
   ```

3. Ejecuta la aplicación:

	```bash
	./a.out
	```

4. Verifica que `a.out` es un fichero binario para linux 64-bit:

	```bash
	file a.out
	```

5. Realmente la compilación incluye varios pasos, el más importante de ellos es la creación de un fichero objeto intermedio, vamos a repetir el proceso en dos pasos:

	```bash
	gcc -c helloworld.c 
	```

	que genera el fichero `helloworld.o`, del tipo:

	```bash
    helloworld.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
    ```

	Para enlazarlo y producir el fichero de salida a.out:

	```bash
    gcc -Wl helloworld.o
    ```

¿Qué sentido tiene compilar por partes? Cuando el código es grande no hay un solo fichero fuente sino muchos, compilar individualmente estos "módulos" permite, por ejemplo, ahorrar mucho tiempo en la modificación y compilación de un solo componente.

## Compilación y ejecución de C en Windows

Los sistemas Windows no incluyen inicialmente ningún compilador de C, pero hay muchos compiladores que funcionan en sistemas Windows, en particular dev-c++

1. Copia el fichero binario `a.out` compilado en GNU/Linux con gcc en la partición Windows y reinicia el equipo con este sistema
2. Ejecuta la aplicación `a.out` en Windows, ¿qué ocurre?
3. Instala el IDE dev-c++ en windows
4. Crea un fichero `hola.c` con el programa hola mundo, compílalo y ejecútalo
5. ¿Entiendes que teniendo el mismo código fuente los binarios son diferentes?

## Bibliotecas estáticas o dinámicas

Un conjunto de ficheros objeto que se enlazan con la parte principal de un programa para producir un binario o ejecutable reciben el nombre de biblioteca (library en inglés). Si el enlace se realiza durante la compilación, las bibliotecas se denominan estáticas o de enlace estático, mientras que si el enlace se realiza durante la ejecución las bibliotecas se denominan dinámicas o de enlace dinámico.

La principal ventaja de la compilación con bibliotecas de enlace dinámico es que el tamaño de los ficheros binarios de las aplicaciones es mucho menor y se optimiza el uso de la memoria porque una biblioteca dinámica puede ser utilizada por diferentes aplicaciones.

En sistemas windows las bibliotecas dinámicas se distribuyen en ficheros con extensión `.dll` (dynamic link library) y en sistemas GNU/Linux lo hacen en los paquetes `lib*` que incluyen ficheros con extensión `.so` (shared object).



