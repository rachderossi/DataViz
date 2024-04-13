import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'name': ['Anna', 'Mary', 'Peter', 'John', 'Anna', 'Mary', 'Peter', 'John', 'Anna', 'Mary', 'Peter', 'John', 'Anna', 'Mary'],
    'year': [1950, 1950, 1950, 1950, 1960, 1960, 1960, 1960, 1970, 1970, 1970, 1970, 1980, 1980],
    'Contagem': [100, 120, 80, 90, 110, 130, 70, 95, 105, 125, 85, 100, 95, 105]
}

babynames = pd.DataFrame(dados)

data = babynames[(babynames['name'].isin(['Anna', 'Mary']))]

# Filtrando os anos específicos
anos_selecionados = [1950, 1960, 1970, 1980]
data = data[data['year'].isin(anos_selecionados)]

# Agregando a contagem de frequência para cada nome e ano
data = data.pivot_table(index='year', columns='name', values='Contagem', aggfunc='sum', fill_value=0)

data.plot(kind='bar', stacked=False, figsize=(12, 6))
plt.xlabel('Anos')
plt.ylabel('Número de bebês')
plt.title('Número de bebês chamados Anna e Mary ao longo dos anos')
plt.legend(title=None)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
