class BaseDeDados:
    def __init__(self,id,nome,rg):

        self._id = id
        self._nome = nome
        self._rg = rg

        self.nome = {}
        self.rg = {}

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


bd = BaseDeDados()
bd.inserir(1, 'Rafael','10')
bd.inserir(2, 'João','20')
bd.inserir(3, 'Henrique','30')

bd.lista_clientes()

bd.deletar_cliente(2)

bd.lista_clientes()