import random

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def get_estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def set_estado(self, experiencia_recibida):
        nueva_experiencia = self.experiencia + experiencia_recibida
        while nueva_experiencia >= 100:
            self.nivel += 1
            nueva_experiencia -= 100
        while nueva_experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            nueva_experiencia += 100
        if nueva_experiencia < 0:
            nueva_experiencia = 0
        self.experiencia = nueva_experiencia

    def __lt__(self, otro):
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        return self.nivel > otro.nivel

    def probabilidad_ganar(self, otro):
        if self < otro:
            return 0.33
        elif self > otro:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def enfrentar(probabilidad):
        return random.uniform(0, 1) <= probabilidad

    @staticmethod
    def opcion_juego(probabilidad):
        print(f"Con tu nivel actual, tienes {probabilidad * 100:.1f}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        while True:
            try:
                opcion = int(input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"))
                if opcion in [1, 2]:
                    return opcion
                else:
                    print("Opción inválida. Por favor ingrese 1 para Atacar o 2 para Huir.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número (1 o 2).")
