import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL dos dados dos nomes de bebês
url = "https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/babynames/yob{}.txt"

# Lista para armazenar os DataFrames de cada ano
dfs = []

# Anos que você deseja analisar
years = [1950, 1960, 1970, 1980, 1990, 2000]

# Ler os dados de cada ano e adicionar ao DataFrame
for year in years:
    df = pd.read_csv(url.format(year), names=['name', 'sex', 'n'])
    df['year'] = year
    dfs.append(df)

# Concatenar todos os DataFrames
data = pd.concat(dfs, ignore_index=True)

# Filtrar os nomes Anna e Mary para o sexo feminino
data = data[(data['name'].isin(['Anna', 'Mary'])) & (data['sex'] == 'F')]

# Plotar o gráfico
plt.figure(figsize=(10, 6))
sns.barplot(x='year', y='n', hue='name', data=data, palette={'Anna': '#6E9AF8', 'Mary': '#69b3a2'})
plt.title("Número de bebês chamados Anna e Mary ao longo dos anos")
plt.xlabel("Anos")
plt.ylabel("Número de bebês")
plt.legend(title=None)
plt.grid(axis='y')
plt.show()
