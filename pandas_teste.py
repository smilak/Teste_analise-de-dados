import pandas as pd
var = ['carro', 'sapato','chinelo']
#para saber onde esta o elemento
a=var.index('sapato')
print(a)
#puxar documento em cvs
data_set= pd.read_csv('db.csv', sep=';')
#saber o tipo da variável
tipo = data_set.dtypes
#descrever o conteúdo da variável
descricao=data_set[['Quilometragem', 'Valor']].describe()
#informação sobre a variável
informacao = data_set.info()
#print(tipo)
#print(data_set)
#print(descricao)
print(informacao)