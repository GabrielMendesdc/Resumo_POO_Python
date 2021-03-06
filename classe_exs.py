lista_de_nomes_usados = ['Bradesco']

class Banco:
    def __init__(self, nome):

        # O Underscore indica que o atributo apenas deve ser usado por subclasses, e não fora da classe
        # Se fosse __nome pra acessar seria self._Banco__nome
        self._nome = nome

        # Criei esse atributo pra associar outra classe a ele e testar associação de classes
        self.empresas_terceirizadas = []
        self._clientes = []

        # Usei o global pra substituir um banco de dados, uma informação externa a classe pra testar o comportamento
        global lista_de_nomes_usados  
        lista_de_nomes_usados.append(self._nome)

    @property
    def nome(self):
        # Método Getter Chamado
        return self._nome

    @nome.setter
    def nome(self, novonome):
        global lista_de_nomes_usados
        if novonome not in  lista_de_nomes_usados:
            self._nome = novonome
        else: 
            print(f'Já Existe o nome {novonome}')

    def contrata(self, empresa):
        self.empresas_terceirizadas.append(empresa)
        #retorna a posição da classe na lista
        return self.empresas_terceirizadas.index(empresa)

    def abre_conta(self, cliente):
        print(self.nome, ' abriu uma conta para ', cliente._nome)
        self._clientes.append(cliente)

    def deposita(self, cliente, valor):
        indice = self._clientes.index(cliente)
        self._clientes[indice].entra_dinheiro(valor)


    # Deixei como comentário pra não sair no output mas serve pra ver quando as classe são destruídas
    # def __del__(self):
        # print(self.nome, 'foi apagado')

# Instanciando um Banco verdadeiro
santander = Banco('Santander')

# Testando o setter com um banco falso mudando o nome pra um verdadeiro (ja cadastrado)
st1 = Banco('SantoAndre1Clonado')
st1.nome = 'Santander'


class LimpezaTerceirizada():
    def __init__(self, empresa_contratante, preco):
        self.empresa_contratante = empresa_contratante
        self.preco = preco
    
    def limpa(self):
        print(f'Estamos limpando o {self.empresa_contratante} por R${self.preco},00')

    # Deixei como comentário pra não sair no output mas serve pra ver quando as classe são destruídas
    # def __del__(self):
        # print('limpeza foi apagado')

# Cria uma empresa de limpeza
limpa_tudo = LimpezaTerceirizada('Banco Santander' ,5050)

# Associa a nova empresa no banco criado antes
id = santander.contrata(limpa_tudo)

# Chama o módulo limpa dentro de limpeza terceirizada, associada na lista empresas_terceirizadas (um atributo do banco)
# Por chamar um método de uma classe através da outra é uma associação de classes, pois ambas são independentes
santander.empresas_terceirizadas[id].limpa()


# Exemplo de agregação: A classe Cliente pode existir totalmente sozinha, e a classe Banco também, mas 
# Várias funções de Banco necessitam de um Cliente, o que torna essa relação uma agregação

class Cliente:
    def __init__(self, nome, saldo=0):
        self._nome = nome
        self.__saldo = saldo
        self._extrato = []

    def confere(self):
        print(self._nome, 'Tem: R$', self._Cliente__saldo)

    def entra_dinheiro(self, valor):
        self._Cliente__saldo += valor
        self._extrato.append(valor)

    def extrato(self):
        print('Extrato: ', end='')
        for i in self._extrato:
            if i > 0:
                print(f'Depósito de {i}, ', end='')
            else:
                print(f'Saque de {i}, ' , end='')
        print(f'Saldo atual: {self._Cliente__saldo}')

    def gera_cartao(self, limite):
        self.cartao = CartaoDeCredito(self,limite)
        print(f'Cartao de crédito criado com sucesso para {self._nome} com R${limite},00 de limite')

    # Deixei como comentário pra não sair no output mas serve pra ver quando as classe são destruídas
    # def __del__(self):
        # print(f'cliente {self._nome} foi apagado')


# Criei essa classe cartão de crédito para demonstrar a relação de composição entre
# Classes, a instância cartao da classe CartaoDeCredito foi apagada antes mesmo do banco,
# Pois ela foi instanciada dentro de Banco logo ela compõe este


class CartaoDeCredito:
    def __init__(self, cliente, limite):
        self.cliente = cliente
        self._limite = limite

    def __del__(self):
        print('Cartão de crédito deletado')


joao = Cliente('João')
santander.abre_conta(joao)
joao.confere()
santander.deposita(joao, 5000)
santander.deposita(joao, -4999)
joao.gera_cartao(700)

# Quando apagamos a instancia de santander da memória,
# A limpeza_terceirizada e os cliente não foram apagados 
# Antes do programa ser executado, como ocorreu com santander
# del santander

joao.extrato()


# Agora vou testar como funciona herança simples e 
# Sobreescrição de métodos e atributo.

# Agencia recebeu todos os métodos e atributos de Banco
class Agencia(Banco):
    def contrata(self, cliente):
        print(cliente._nome, ' agora faz parte do quadro de funcionários ',self._nome)


santander_ag_0001 = Agencia('Santander_ag_0001')
santander_ag_0001.abre_conta(joao)
santander_ag_0001.contrata(joao)

# Testando se sobreescrever uma classe altera a original
limpa_nada = LimpezaTerceirizada('Banco Santander' , 50)
id2 = santander.contrata(limpa_nada)
santander.empresas_terceirizadas[id2].limpa()
# O método contrata() continua igual

