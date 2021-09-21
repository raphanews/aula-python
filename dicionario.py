meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
print(meu_dicionario)


meu_dicionario_2 = dict({1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'})
#print(type(meu_dicionario_2))

#get() Elementos pelo indice
print(meu_dicionario[2])
print(meu_dicionario.get(4))

'''
#len() Tamanho do dicionario
print(len(meu_dicionario))

#adicionando elementos no dicionario
meu_dicionario[5] = 'Joaquina'
print(meu_dicionario)

meu_dicionario.update({6: 'Pedro'})
print(meu_dicionario)

#removendo elementos do dicionario
#pop()
meu_dicionario.pop(2)
del meu_dicionario[1]
print(meu_dicionario)

#visualizando dados
for id, nome in meu_dicionario.items():
    print(str(id) +": "+str(nome))

'''