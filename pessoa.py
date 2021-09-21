class Pessoa:
    # construtor
    def __init__(self, nome='', sexo='', idade=0, ativo=False):
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._ativo = ativo

    def getNome(self):
        return self._nome

    def setNome(self,valor):
        self._nome = valor

    def getSexo(self):
        return self._sexo

    def setSexo(self,valor):
        self._sexo = valor

    def getIdade(self):
        return self._idade

    def setIdade(self, valor):
        self._idade = valor

    def getAtivo(self):
        return self._ativo

    def setAtivo(self, valor):
        self._ativo = valor

    def ativarPessoa(self):
        self.ativo = True

    def desativarPessoa(self):
        self.ativo = False

    def verificaIdade(self):
        if (int(self._idade) >= 18):
            print('Maior de idade')
        else:
            print('Menor de idade')
