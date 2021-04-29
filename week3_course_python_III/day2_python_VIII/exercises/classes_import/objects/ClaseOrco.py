class Orco:

    # función constructor
    def __init__(self, nombre, armadura, nivel, ataque, ojos = 2, piernas = 2, dientes = 56, salud = 100):
        # nombre del atributo de la clase Humano <-- --> valor
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud

    def f_atacar(self, Humano):
        Humano.salud -= self.ataque - Humano.armadura


    def f_no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def f_atributos(self):
        print(maurOrco.nombre)
        print(maurOrco.salud) 
        print(maurOrco.armadura)

maurOrco = Orco(nombre = "MaurOrco", nivel=15, armadura=35, ataque=15)