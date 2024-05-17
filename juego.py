from personaje import Personaje

def main():
    print("¡Bienvenido a Gran Fantasía!")
    nombre_personaje = input("Por favor indique nombre de su personaje:\n")
    
    jugador = Personaje(nombre_personaje)
    print(jugador.get_estado())
    
    orco = Personaje("Orco")
    probabilidad = jugador.probabilidad_ganar(orco)
    
    print("¡Oh no!, ¡Ha aparecido un Orco!")
    opcion = Personaje.opcion_juego(probabilidad)
    
    while opcion == 1:
        resultado = Personaje.enfrentar(probabilidad)
        if resultado:
            print("¡Le has ganado al orco, felicidades!")
            print("¡Recibirás 50 puntos de experiencia!")
            jugador.set_estado(50)
            orco.set_estado(-30)
        else:
            print("¡Oh no! ¡El orco te ha ganado!")
            print("¡Has perdido 30 puntos de experiencia!")
            jugador.set_estado(-30)
            orco.set_estado(50)
        
        print(jugador.get_estado())
        print(orco.get_estado())
        
        probabilidad = jugador.probabilidad_ganar(orco)
        opcion = Personaje.opcion_juego(probabilidad)
    
    if opcion == 2:
        print("¡Has huido! El orco ha quedado atrás.")

if __name__ == "__main__":
    main()
