# Ejecución de programas interpretados

Lenguaje interpretado: Es el lenguaje cuyo código no necesita ser preprocesado mediante un compilador, eso significa que el ordenador es capaz de ejecutar la sucesión de instrucciones dadas por el programador sin necesidad de leer y traducir exhaustivamente todo el código.

## Bash

El lenguaje Bash nos permite escribir programas utilizando las instrucciones que usamos en el terminal de linux. Este lenguaje está pensado para hacer pequeños programas (scripts) que nos facilitan hacer alguna tarea. El lenguaje Bash es interpretado.

Veamos un ejemplo, crea un fichero ejemplo.sh con el siguiente contenido:

```bash
#!/bin/bash
a=$((RANDOM%100))
intentos=1
read -p "¿Que numero crees que es? " b
while [ $b -ne $a ]
do
        if [ $b -lt $a ]
        then
                echo "El numero que has introducido es menor"
        else
                echo "El numero que has introducido es mayor"
        fi
        read -p "Has fallado, introduce otro numero " b
        intentos=$((intentos+1))
done
echo "Has acertado"
echo "Has necesitado" $intentos "intentos"
```

Para ejecutarlo, le tenemos que dar permiso de ejecución:

```bash
# chmod 755 ejemplo.sh#
./ejemplo.sh
```

## Python

Python también es un lenguaje interpretado, veamos un ejemplo: crea un fichero ejemplo.py con el siguiente contenido:

```python
#!/usr/bin/env python
import random

a=random.randrange(0, 100)
intentos=1
b=int(input("Introduce un número:"))
while a!=b:
        if b>a:
                print("El número introducido es mayor")
        else:
                print("El número introducido es menor")
        intentos=intentos+1
        b=int(input("Introduce un número:"))
print("Has acertado en %d intentos." % intentos)
```

Para ejecutar el programa usamos el interprete python:
```bash
python3 ejemplo.py
```