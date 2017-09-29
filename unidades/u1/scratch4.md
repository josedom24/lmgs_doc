# Ejercicio 4 Scratch

Utilizando la aplicación scratch (directamente del sitio web o instalándola en tu equipo) desarrolla tu primer juego paso a paso:

1. Haz que un personaje (sprite1) se mueva de forma indefinida de derecha a izquierda de la pantalla, manteniendo su posición vertical lo más arriba posible y rebotando con las paredes laterales
2. Modifica el disfraz de sprite1 para que cambie a cada paso y dé la sensación de que camina, corre o vuela (dependiendo del personaje elegido)
3. Crea un segundo objeto (sprite2) que se moverá sólo en posición horizontal, pero en este caso se controlará su movimiento con las teclas flecha izquierda y flecha derecha
4. Crea un tercer objeto (sprite3) como una pelota o similar que utilizaremos para que sprite2 la lance e intente alcanzar a sprite1. Este objeto se moverá junto sprite2 hasta que se pulse la barra espaciadora (disparo), momento en el que se moverá en vertical hasta alcanzar el borde superior. Una vez que alcance el borde superior desaparece y vuelve a aparecer junto a sprite2
5.Cuando sprite3 (la pelota) toque a sprite1, desaparecen ambos
6. Crea un contador que cuente el número de aciertos (veces que sprite3 toca a sprite1)
7. Crea varias fases del juego de acuerdo a la siguientes reglas:
	* Si sprite2 consigue alcanzar a sprite1 3 veces, se pasa a la siguiente fase
    * Al pasar de fase, la velocidad de sprite1 aumenta
    * Si sprite2 utiliza más de 6 disparos en una fase el juego termina, mostrando a pantalla completa el texto "GAME OVER"
