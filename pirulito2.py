import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Lê os dados do arquivo CSV fornecido pela URL e os carrega em um DataFrame chamado 'data'
data = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/7_OneCatOneNum.csv")

# Remove as linhas com valores ausentes na coluna 'Value' e ordena o DataFrame pelos valores de 'Value' 
# em ordem ascendente, em seguida, seleciona as 20 maiores linhas
data_filtered = data.dropna(subset=['Value']).sort_values('Value').tail(20)

# Cria o gráfico de pirulito
plt.figure(figsize=(10, 6))
plt.hlines(y=data_filtered['Country'], xmin=0, xmax=data_filtered['Value'], color='grey')
plt.plot(data_filtered['Value'], data_filtered['Country'], 'o', color='#69b3a2', markersize=8)
plt.title("Quantidade de armas exportadas pelos 20 maiores exportadores em 2017")
plt.xlabel("Quantidade de armas")
plt.ylabel("Países")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
