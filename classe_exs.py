lista_de_nomes_usados = ['Bradesco']

class Banco:
    def __init__(self, nome):
        # O Underscore indica que o atributo apenas deve ser
        # usado por subclasses, e não fora da classe
        # Se fosse __nome pra acessar seria self._Banco__nome
        self._nome = nome
        # Criei esse atributo pra associar outra classe a ele e testar associação de classes
        self.empresas_terceirizadas = []
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


# Instanciando um Banco
santander = Banco('Santander')

# Testando o setter
st1 = Banco('SantoAndre1')
st1.nome = 'Santander'


class Limpeza_terceirizada():
    def __init__(self, empresa_contratante, preco):
        self.empresa_contratante = empresa_contratante
        self.preco = preco
    
    def limpa(self):
        print(f'Estou limpando o {self.empresa_contratante} por {self.preco}')

# Cria uma empresa de limpeza
limpa_tudo = Limpeza_terceirizada('Banco Santander ag 0',5000)
# Associa a nova empresa no banco criado antes
id = santander.contrata(limpa_tudo)
# Chama o módulo limpa dentro de limpeza terceirizada, associada na lista empresas_terceirizadas (um atributo do banco)
# Por chamar um método de uma classe através da outra é uma associação de classes
santander.empresas_terceirizadas[id].limpa()