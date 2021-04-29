class Humano:

    # función constructor
    def __init__(self,nombre, armadura, nivel, ataque, ojos = 2, piernas = 2, dientes = 32, salud = 100):
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


    def f_no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def f_atributos(self):
        print(mauro.nombre)
        print(mauro.salud) 
        print(mauro.armadura)
       

mauro = Humano(nombre = "Mauro", nivel=20, armadura=25, ataque=20)
