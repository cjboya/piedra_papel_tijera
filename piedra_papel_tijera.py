"""

Desafío Python en 10 minutos! 

Crear una rutina para jugar al famoso juego piedra, papel o tijera, pero contra la computadora.
¡No te olvides que gana el que llega a 3 puntos!

Ayuda : usar el módulo random para sacar valores aleatorios ;)

Resolverlo como más te guste, usando lo que conoces. >> No hay una única solución <<.

Te dejamos una posible resolución.

Mucha Suerte :) 

Piedra , Papel o Tijera .... 

"""

import random


############ Funciones ################


def validar(valor):
    """
    La funcion validar acepta y verifica 
    unicamente enteros entre 1, 2 o 3
    Retorna el valor ya convertido a entero.
    """
    while True:
        try:
            valor = int(valor)
            if 1 <= valor <= 3:
                return valor
            else:
                print("¡Valores entre 1 y 3 solamente!")
        except ValueError:
            print("Error, no es un número.")
            print("Sólo números según las opciones")
        valor = input("Vuelva a ingresar un valor: ")


############ Rutina ################
# Diccionario con claves 1,2,3 y valores Piedra, Papel y Tijera
posibilidades = {1: "Piedra", 2: "Papel", 3: "Tijera"}


# Variables
jugador = 0  # aciertos jugador
computadora = 0  # aciertos computadora
contador = 1  # contador de vueltas, no necesario para resolver


# Bucle infinito que terminamos con un break más adelante

while True:
    # Menú
    print("Oportunidad n°", contador)
    print("1-> Piedra")
    print("2-> Papel")
    print("3-> Tijera")
    opcion = input("Ingrese una opción: ")  # opción jugador
    opcion = validar(opcion)  # validar opción
    aleatorio = random.randint(1, 3)  # jugada computadora
    # Posibilidades pueden ser 6 diferentes y 3 empates
    if opcion == 1 and aleatorio == 2:
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Punto para la computadora!")
        computadora += 1
        contador += 1
    elif opcion == 1 and aleatorio == 3:
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Punto para el jugador!")
        jugador += 1
        contador += 1
    elif opcion == 2 and aleatorio == 1:
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Punto para el jugador!")
        jugador += 1
        contador += 1
    elif opcion == 2 and aleatorio == 3:
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Punto para la computadora!")
        computadora += 1
        contador += 1
    elif opcion == 3 and aleatorio == 1:
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Punto para la computadora!")
        computadora += 1
        contador += 1
    elif opcion == 3 and aleatorio == 2:
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Punto para el jugador!")
        jugador += 1
        contador += 1
    else:
        # No olvidar de controlar los tiros con empates, no suman puntos
        print("La computadora eligió:", posibilidades[aleatorio])
        print("Vos eligiste:", posibilidades[opcion])
        print("¡Empate!, no suma puntos")

    if computadora == 3 or jugador == 3:
        # No olvidar de controlar los tiros sin empates, para terminar la partida si llegan a 3 aciertos
        print("-------------------------")
        print("¡Fin del juego!")
        break
    print("\n")  # salto de linea opcional para limpiar pantalla


###### informamos quien fue el ganador ########

print("-------------------------")

if jugador > computadora:
    print("Ganó jugador")
else:
    print("Ganó la computadora")


print("-------------------------")

print("Marcador final:")
print("La computadora obtuvo", computadora, "aciertos")
print("El jugador obtuvo", jugador, "aciertos")

print("-------------------------")

input("Toque Enter Para Finalizar...")
