import pandas as pd

tabela = {'Alunos': ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4'],
              'nota_1':[7, 3, 9, 10],
              'nota_2':[7, 10, 4, 6],
              'faltas':[1,7, 2, 9]}
tabelaDF = pd.DataFrame(tabela) 
tabelaDF['Média'] = (tabelaDF ['nota_1'] + tabelaDF ['nota_2']) /2
tabelaDF.loc[tabelaDF['Média'] >= 7, 'Situacao'] = 'Aprovado'
tabelaDF.loc[tabelaDF['Média'] < 7, 'Situacao'] = 'Reprovado'
tabelaDF.loc[tabelaDF['faltas'] >5, 'Situacao'] = 'Reprovado'
maior_falta= tabelaDF['faltas'].max()
media_geral= tabelaDF['Média'].mean()
maior_media = tabelaDF['Média'].max()
print('O maior número de faltas foi: ',maior_falta)
print('A média geral dos alunos foi: ',media_geral)
print('A maior média foi: ',maior_media)
tabelaDF
