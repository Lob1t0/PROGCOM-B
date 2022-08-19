import random
opciones=["piedra","papel","tijera"]


while True:
    jugador=input("Elije entre: piedra,papel,tijera: ")
    if jugador not in opciones:
        print("\nOpcion no valida, elije otra vez")
        continue
    computadora=random.choice(opciones)
    print(f"\nLa eleccion de la computadora fue: {computadora}")
    if jugador==computadora:
        print(f"\nHa sido un empate, ambos eligieron {jugador}")
    elif jugador=="piedra" and computadora=="tijera":
        print(f"\nHas ganado, {jugador} ganas en contra de {computadora}")
    elif jugador=="tijera" and computadora=="papel":
        print(f"\nHas ganado, {jugador} ganas en contra de {computadora}")
    elif jugador=="papel" and computadora=="piedra":
        print(f"\nHas ganado, {jugador} ganas en contra de {computadora}")
    else:
        print(f"Perdiste, {jugador} pierde contra {computadora} ")
    print(">>>>>Fin del juego<<<<<")