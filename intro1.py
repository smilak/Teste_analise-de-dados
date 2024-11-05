import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
filmes=pd.read_csv('ml-latest/movies.csv')
notas = pd.read_csv('ratings.csv')
tmdb = pd.read_csv("tmdb_5000_movies.csv")
'''
#a=notas.query("movieId==1").rating.mean()#referenciar uma tabela com a outra e term ma media
#b=notas.query("movieId==2").rating.mean()
#c=notas.groupby('movieId').mean()['rating']#agrupara os dados
#c.plot(kind='hist')
#sns.boxplot(notas.rating)
#plt.show()
#foi contado o elementos, separarado em tabela, mudando index para a contagem da maq
contagem_linguas= tmdb['original_language'].value_counts().to_frame().reset_index()
contagem_linguas.columns = ['original_language', 'total']
#sns.barplot(x='original_language',y='total',data=contagem_linguas)#gerando grafico
#sns.catplot(x='original_language', kind='count', data=tmdb )#gerar grafico
#plt.pie(contagem_linguas['total'], labels=contagem_linguas['original_language'])#grafico tipo de pizza
#criando valores para mostrar em um grafico

total_geral=total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral-total_de_ingles
#tranformando em data frame
dados = {
    'lingua':['ingles', 'outros'],
    'total':[total_de_ingles, total_do_resto]
}
dado=pd.DataFrame.from_dict(dados)#tranformando dicionario em data frame
sns.barplot(x='lingua',y='total', data=dado)
#plt.show()
total_por_lingua=tmdb['original_language'].value_counts()
filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x='original_language', kind="count", data=filmes_sem_lingua_original_em_ingles, aspect=2,palette='GnBu_d', order=total_por_lingua.index)
plt.show()'''
notas_do_toy_story = notas.query('movieId==1')
notas_do_jumanji = notas.query('movieId==2')
print(len(notas_do_toy_story),len(notas_do_jumanji))
print(notas_do_toy_story.rating.mean())
print(notas_do_jumanji.rating.mean())
