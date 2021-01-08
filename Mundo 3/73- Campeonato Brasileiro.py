tupla = ('Santos','Corinthians','São Paulo','Palmeiras','Grêmio','Internacional',
         'Sport','Bahia','Athletico MG','Flamengo','Vasco','Botafogo','Chapecoense',
         'Curitiba', 'Fluminense', 'Paisandu', 'Ponte Preta', 'Portuguesa', 'Ituano','Cruzeiro'
         )
print('Os cinco primeiro do brasileirão são: ', tupla[0:5])
print('Os quatro ultimos da tabela são: ', tupla[16:20])
print('Ordem alfabética dos times do Brasileirão: ', sorted(tupla))
print('O Chapecoense está classificado em',tupla.index('Chapecoense')+1,'ª da Tabela')
