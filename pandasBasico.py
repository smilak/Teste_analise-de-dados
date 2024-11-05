import pandas as pd

var0 = {'jetta': 1000, 'passat': 2000, 'santana': 4000, 'megane': 30000, 'gol': 3000, 'fusca': 1550}
var1=[{'nome':'jetta', 'motor':'2,0', 'ano':2021, 'combustivel':'gas'},\
    {'nome':'jetta variant', 'motor':'2,0', 'ano':2022, 'combustivel':'gas'},
    {'nome':'Golf', 'motor':'2,0 turbo', 'ano':2023, 'combustivel':'gas'}]

#Series
#criar uma series
a= pd.Series(var1)
#Criar DataFrame
b= pd.DataFrame(var1)
#buscar documento csv, sep para mostrar tipo de saparação, index_col colocar como inicio a coluna 0 e não numeração
data=pd.read_csv("db.csv",sep=';', index_col=0)
data1=data.head()
#selecionar colunas, o nome dos carros ficaram por causa do index_col=0 que cria um rótulo
c=data['Valor']#retorna Series
d= data[['Valor']]#retorna DataFrame
#selecionar linhas
e=data[0:3] #seleciona as linhas que quer mostrar
f=data.loc['Passat']#busca dados da linha a partira do rótulo (Series)
g=data.loc[['Passat','DS5']]#busca dados da linha a partira do rótulo (DataFrame)
h=data.loc[['Passat','DS5'],['Motor', 'Valor']]#Separar linha e valores
i=data.loc[:,['Motor', 'Valor']]#quando quiser todas as linhas mas só alguns rótulos
j=data.iloc[1:4,[0,5,2]]#separa pelo indice numerico das linhas
#query (consulta)= fazer uma seleção dentro das tabelas
l=data.Motor=="Motor Diesel" #separa em modo boolean uma busca
m=data[l]#mostra dentro da tabela apenas essa busca
n = data[(data.Motor=="Motor Diesel")&(data.Zero_km==True)]#buscar dois detalhes de busca junto
o=data.query("Motor=='Motor Diesel' and Zero_km ==True")#fazendo a busca usando método query
#Criar uma coluna com valor médio de km
for index, row in data.iterrows():
    if(2019 - row['Ano'] != 0):
        data.loc[index, 'Km_media']=row["Quilometragem"]/(2019 - row["Ano"])
    else:
        data.loc[index, "Km_media"] ='Carro Zero'
#tratar dados
data11=pd.read_csv('db.csv', sep=';', index_col=0)
p=data11.info()#ver detalhes anormais nas tabelas (nesse caso como coluna quilometragem)
k=data.Quilometragem.isna()#mostrar qual esta com anomalia
q=data11[data11.Quilometragem.isna()]#mostrar todos separados em uma tabela
r=data11.fillna(0)
s=data11.query("Zero_km == True")
#eliminar linha apartir do dado escolhido como errado
t=data11.dropna(subset=["Quilometragem"], inplace=True)

print(data11)


