import pandas as pd
var = ['jetta','passat', 'gol', 'santana']
val = [1000,2000,3000,4000]
#juntar as listas
dados = list(zip(var,val))
#colocar as listas em um dicionario
dic = dict(zip(var,val))
print(dic)
#para procurar um elemento específico
a = 'jetta' in dic
#para saber quantos elemento tem no discinário
b = len(dic)
#para adicionar um elemento do dicionario
c = dic['megane'] = 30000
#para retirar um elemento do dicionario e tratar o erro 'chave nao encontrada' se náo tiver o elemnto que esta buscando para deletar
e=dic.pop('gol','chave nao encontrada')
#para atualizar e inserir dados
f=dic.update({'gol':3000, 'fusca':1550})
#para copiar o discionario criando outro para poder mexer  e nao alterar o real
g=dic.copy()
#limpar o discionario
h = g.clear()
#Qual o tipo de variavel
i = type(dic)
#como retornar só as chaves
j=dic.keys()
#como retornar só os valores usando keys
for key in dic.keys():
    print(dic[key])
#como retornar só os valores
l = dic.values()
#separa em tuplas dentro do dicionario
m= dic.items()
#desempacotamento de tuplas com metodo key e value
for key, value in dic.items():
    print(key,value)
#exemplo colocar uma condição para mostrar veiculos de valores maior
for key, value in dic.items():
    if (value>2850):
        print(f"os carros são: ", key)
 
print(dic)
print(m)