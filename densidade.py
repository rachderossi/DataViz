import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Define a URL do arquivo CSV contendo os dados de preços de aluguel
url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv"

# Lê os dados do arquivo CSV e os carrega em um DataFrame chamado 'data'
data = pd.read_csv(url)

# Filtra os dados para incluir apenas os preços de aluguel menores que 300
# necessário apenas se quiser filtrar valores específicos
data_filtered = data[data['price'] < 300]

# Criar o gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data_filtered['price'], fill=True, color='#69b3a2', alpha=0.8)
plt.title("Distribuição de preços de aluguel")
plt.xlabel("Preço")
plt.ylabel("Densidade")
plt.grid(True)
plt.show()
