import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Cria um dicionário com os dados das classes de veículo
data = {
    'class': ['compact', 'midsize', 'suv', 'midsize', 'compact', 'suv', 'suv', 'compact'],
}

# Cria um DataFrame a partir do dicionário
mpg = pd.DataFrame(data)

# Conta as ocorrências de cada classe de veículo e armazena em um novo DataFrame
class_counts = mpg['class'].value_counts().reset_index()

# Renomeia as colunas do novo DataFrame
class_counts.columns = ['class', 'freq']

# Ordena o DataFrame pela frequência em ordem ascendente
class_counts = class_counts.sort_values(by='freq')

# Cria o gráfico de pirulito
plt.figure(figsize=(10, 6))
plt.hlines(y=class_counts['class'], xmin=0, xmax=class_counts['freq'], color='black')
plt.plot(class_counts['freq'], class_counts['class'], 'o', color='#6E9AF8', markersize=8)
plt.xlabel('Frequência')
plt.ylabel('Classe')
plt.title('Distribuição das classes de veículo')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.show()
