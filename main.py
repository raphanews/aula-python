from conexao import criar_conexao,fechar_conexao

def inserir(con,codigo,nome):
    cursor = con.cursor()
    sql = "INSERT INTO Profissao (codigo, cargo) values (%s,%s)"
    valores = (codigo,nome)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def deletar(con,codigo):
    cursor = con.cursor()
    sql = "Delete from Profissao where codigo = {}".format(codigo)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar(con):
    cursor = con.cursor()
    sql = "Select * from Profissao"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    for linha in valores_lidos:
        print("Nome: ", linha[0])
        print("Cargo: ", linha[1])
    cursor.close()

def main():
    con = criar_conexao("10.5.0.5", "root", "pamonha", "empresa")

    opcao = input("Digite 1 para deletar e 2 para inserir: ")

    while opcao != 0:
        if opcao == "1":
            codigo = input("Digite o codigo: ")
            deletar(con,codigo)
        elif opcao == "2":
            codigo = input("Digite o codigo: ")
            cargo = input("Digite o cargo: ")
            inserir(con,codigo,cargo)

        opcao = input("Digite 1 para deletar e 2 para inserir: ")

    listar(con)
    fechar_conexao(con)

main()

