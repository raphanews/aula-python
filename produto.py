class Produto:
    def __init__(self,nome='',preco=0):
        self._nome = nome
        self._preco = preco

    def desconto(self,percentual):
        self._preco = self._preco - (self._preco * (percentual/100))

    def get_nome(self):
       return self._nome

    def set_nome(self,valor):
        self._nome = valor

    def get_preco(self):
        return self._preco

    def set_preco(self, valor):
        self._preco = valor

p = Produto()

p.set_nome('Bicicleta')

print(p.get_nome())

