from abc import ABC, abstractmethod
# Abc significa Abstract Base Classes

# Classes abstratas são classes usadas para construir outras classes,
# Mas não devem ser instanciadas

# Essa Classe não pode se instanciada por ser abstrata
# TypeError: Can't instantiate abstract class Personagem with abstract method bater
class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome

    # Esse decorador obriga as classes 'filhas' a definirem esse método,
    # Geralmente usado pra classes filhas terem que definir cada uma
    # Seu próprio corpo de método mas mantendo o nome do método
    @abstractmethod
    def bater(self):
        pass


class Guerreiro(Personagem):
    def bater(self):
        print('espadada')


Guerreiro('Jorge').bater()
Personagem('Jorjito')