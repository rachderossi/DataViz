import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Define a URL do arquivo CSV contendo os dados de nomes de bebês
url = "https://github.com/hadley/data-baby-names/raw/master/baby-names.csv"

# Lê os dados do arquivo CSV e os carrega em um DataFrame chamado 'babynames'
babynames = pd.read_csv(url)

# Lista de nomes de interesse
names = ['Anna', 'Mary']

# Filtra os dados para incluir apenas os nomes 'Anna' e 'Mary'
filtered_data = babynames[babynames['name'].isin(names)]

# Lista de anos de interesse
selected_years = [1950, 1960, 1970, 1980]

# Filtra os dados para incluir apenas os anos de interesse
filtered_data = filtered_data[filtered_data['year'].isin(selected_years)]

# Cria uma tabela dinâmica dos percentuais de bebês com os nomes 'Anna' e 'Mary' ao longo dos anos
data = filtered_data.pivot_table(index='year', columns='name', values='percent', aggfunc='sum', fill_value=0)

# Criar o gráfico de barras agrupadas
data.plot(kind='bar', stacked=False, figsize=(12, 6))
plt.title('Percentual de bebês chamados Anna e Mary ao longo dos anos')
plt.xlabel('Anos')
plt.ylabel('Percentual de bebês')
plt.legend(title=None)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
