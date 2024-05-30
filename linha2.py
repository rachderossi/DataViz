import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# baby_names = pd.read_csv("caminho/para/seu/arquivo.csv")

# Define a URL do arquivo CSV contendo os dados de nomes de bebê
url = "https://github.com/hadley/data-baby-names/raw/master/baby-names.csv"

# Caso não seja necessário filtrar seus dados pule para a linha 24
# Lê os dados do arquivo CSV e os carrega em um DataFrame chamado 'baby_names'
baby_names = pd.read_csv(url)

# Define a lista de nomes a serem filtrados
names = ['Ashley', 'Patricia', 'Helen']

# Define o sexo dos nomes a serem filtrados
sex = 'girl'

# Filtra os dados para incluir apenas os nomes especificados e do sexo especificado
filtered_data = baby_names[(baby_names['name'].isin(names)) & (baby_names['sex'] == sex)]

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
for name, color in zip(names, ['#6E9AF8', '#009E73', '#FFA07A']): # É possível definir cores para cada grupo
    data = filtered_data[filtered_data['name'] == name]
    # year é a variável x e percent é a variável y
    plt.plot(data['year'], data['percent'], label=name, color=color)
plt.title('Popularidade dos nomes Ashley, Patrícia e Helen
                 nos EUA entre (1880-2020)')
plt.xlabel('Ano')
plt.ylabel('Percentual')
plt.legend(title='Name', loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
