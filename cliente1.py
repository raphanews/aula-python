class Cliente1:

    def __init__(self, nome="", RG="", endereco="", bairro="", cidade="", telefone="", email="",ativo='Ativo',id=''):
        self._nome= nome
        self._RG= RG
        self._endereco= endereco
        self._bairro= bairro
        self._cidade= cidade
        self._telefone= telefone
        self._email= email
        self._ativo =ativo
        self._id = id
        self._nome = {}
        self._RG = {}
        self._endereco = {}
        self._bairro = {}
        self._cidade = {}
        self._telefone = {}
        self._email = []
        self._ativo = {}

    def entrada(self):
        print("==============================================")
        print("\Cadastro de Cliente/")
        id = input("Digite ID do Cliente: ")
        nome = input("Digite o Nome do Cliente: ")
        RG = input("Digite o RG do Cliente: ")
        endereco = input("Digite o Endereço do Cliente: ")
        bairro = input("Digite o Bairro do Cliente: ")
        cidade = input("Digite a Cidade do Cliente: ")
        telefone = input("Digite o Telefone do Cliente: ")
        email = input("Digite o Email do Cliente: ")
        """
        print("Maximo de 3 Cadastros")
        print("Se Você Estiver Cazendo o Primeiro Cadasrtros")
        op = int(input("de Cliente Digite 1 se for o Segundo Digite 2 e Fassa isso em Sequência: ")
        """

        self._nome = nome
        self._RG = RG
        self._endereco = endereco
        self._bairro = bairro
        self._cidade = cidade
        self._telefone = telefone
        self._email = email
        print("==============================")
        print("Cadastro Realizado!")
        print("Nome: ", nome)
        print("RG: ", RG)
        print("Endereço: ", endereco)
        print("Bairro: ", bairro)
        print("Cidade: ", cidade)
        print("Telefone: ", telefone)
        print("Email: ", email)



    def inserir(self):

        self._nome.update({id: self._nome})
        self._RG.update({id: self._RG})
        self._endereco.update({id: self._endereco})
        self._bairro.update({id: self._bairro})
        self._cidade.update({id: self._cidade})
        self._telefone.update({id: self._telefone})
        self._email.update({id: self._email})
        self._ativo.update({id: self._ativo})

    def deletar(self, id):
        del self._nome[id]
        del self._RG[id]
        del self._endereco[id]
        del self._bairro[id]
        del self._cidade[id]
        del self._telefone[id]
        del self._email[id]
        del self._ativo[id]

    def desativar(self):
        self._ativo = False


    def listar(self):
        for id,nome in self._id.itens()
            print("ID:", id)
            print("Nome:", self._nome.get(id))
            print("RG:", RG)
            print('Endereco:', endereco)
            print("Bairro: ",bairro)
            print("Cidade:", cidade)
            print("Telefone", telefone)
            print("email", email)
            print("Status:", ativo)














