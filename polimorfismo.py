'''
Polimorfismo é o princípio que permite que classes derivadas de uma
mesma superclasse tenham métodos iguais (de mesma assinatura (mesma quantidade e tipo de parâmetros))
mas apresentam comportamentos diferentes  -Luiz Otávio Miranda
'''

from abc import ABC, abstractclassmethod, abstractmethod

class PaisesFalantes(ABC):
    @abstractmethod
    def escreva(self, conteudo):
        pass

class Brasil(PaisesFalantes):
    def escreva(self, conteudo):
        print(f'Brasil diz: {conteudo}')
    

class Canada(PaisesFalantes):
    def escreva(self, conteudo):
        print(f'Canada diz: {conteudo}')

brasil = Brasil()
canada = Canada()
brasil.escreva(' Sou brasileiro com muito orgulho')
canada.escreva(" I'm a canadian citizen with proud")

# Ambas as classes tem o mesmo método e a mesma assinatura, mas se comportam diferente, isso é devido
# Ao uso de um método abstrato que se reescreve a cada nova subclasse. Polimorfismo