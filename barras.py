import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 5 substitui essa, pois aqui estou criando dados fictícios
# Define um dicionário com os dados das classes de veículo, pois não estou usando nenhum arquivo CSV
data = {
    'class': ['compact', 'midsize', 'suv', 'midsize', 'compact', 'suv', 'suv', 'compact'],
}

# Caso você já tenha a variável de frequência calculada pode pular para a linha 25
# Cria um DataFrame chamado 'mpg' com os dados fornecidos
mpg = pd.DataFrame(data)

# Conta o número de ocorrências de cada classe de veículo e armazena em 'class_counts'
class_counts = mpg['class'].value_counts().reset_index()

# Renomeia as colunas para 'class' e 'count'
class_counts.columns = ['class', 'count']

# Ordena as contagens pelo número de ocorrências
# Se a sua variável frequência já estiver calculada:
# data = data.sort_values(by='frequencia')
class_counts = class_counts.sort_values(by='count')

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
# class é a variável x e count é a variável y
plt.bar(class_counts['class'], class_counts['count'], color='#6E9AF8')
plt.title('Distribuição das classes de veículo')
plt.xlabel('Classe')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.show()
