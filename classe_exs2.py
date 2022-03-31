# Heranças múltiplas

class Armadura():
    def defender(self):
        print('defesa')

class Espada():
    def atacar(self):
        print('ataque')

class Guerreiro(Armadura, Espada):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("sou o guerreiro ", self.nome)
        # Super chamar as classes superiores na hierarquia
        super().defender()
        super().atacar()

    def defender(self):
        print(self.nome, 'Defenderá voce')

    def atacar(self):
        print(self.nome, "Esmagará voce")


jorge = Guerreiro('Jorge')
jorge.falar()
jorge.defender()
jorge.atacar()