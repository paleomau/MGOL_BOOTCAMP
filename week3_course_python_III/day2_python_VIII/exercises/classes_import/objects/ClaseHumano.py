class Humano:

    # función constructor
    def __init__(self, ojos = 2, piernas = 2, dientes = 32, nombre, armadura, nivel, ataque, salud = 100):
        # nombre del atributo de la clase Humano <-- --> valor
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud

    def f_atacar(self, Orco):
        Orco.salud -= self.ataque - Orco.armadura


    def f_no_vivo():
        if self.salud <= 0:
            return True
        else:
            return False

    def f_atributos():
        pass

Mauro = Humano(nombre = "Ataulfo",)

Mauro.atributos()
print(Mauro.nombre)
print(Mauro.salud) 
print(Mauro.armadura) 