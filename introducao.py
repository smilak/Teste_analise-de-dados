import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
notas = pd.read_csv('ratings.csv')
a=notas.shape#tamanho da tabela
b=notas.columns=['usuarioId','filmeId', 'nota', 'momento']#mudar o nome das colunas
c= notas.nota.unique()#mostrar as diversidades da coluna
d=notas['nota'].value_counts()#conta e fornece a quantidade de cada opção
e=notas.nota.plot()#mostrar em um grafico tudo
f=notas.nota.plot(kind='hist')#motrar no grafico selecionado
g=sns.boxplot(notas.nota)
print(g)