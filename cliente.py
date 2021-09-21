class Cliente:
    def __init__(self, nome='', rg='', endereco='', bairro='', cidade='', telefone='', email='', ativo=False):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.ativo = ativo

        self.nome = {}
        self.rg = {}

    def getNome(self):
        return self.nome

    def setNome(self, valor):
        self._nome = valor

    def getRg(self):
        return self.rg

    def setRg(self, valor):
        self._rg = valor

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, valor):
        self._endereco = valor

    def getBairro(self):
        return self.bairro

    def setBairro(self, valor):
        self._bairro = valor

    def getCidade(self):
        return self.cidade

    def setCidade(self, valor):
        self._cidade = valor

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, valor):
        self._telefone = valor

    def getEmail(self):
        return self.email

    def setEmail(self, valor):
        self._email = valor

    def desativarPessoa(self):
        self.ativo = False

    def inserir(self, id,nome,rg):
            self.nome.update({id: nome})
            self.rg.update({id: rg})


    def lista_clientes(self):
        for id,nome in self.nome.items():
            print('ID: ', id)
            print('Nome: ',nome)
            print('RG: ',self.rg.get(id))

    def deletar_cliente(self,id):
        del self.nome[id]
        del self.rg[id]