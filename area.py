import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Lê os dados do arquivo CSV de um URL e os carrega em um DataFrame chamado 'data'
data = pd.read_csv(
    "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", 
    delim_whitespace=True
)

# Converte a coluna 'date' para o tipo datetime
data["date"] = pd.to_datetime(data["date"])

# Extrai as colunas 'date' e 'value' do DataFrame 'data'
date = data["date"]
value = data["value"]

# Cria o gráfico de área
plt.figure(figsize=(10, 6))
plt.fill_between(data['date'], data['value'], color="#69b3a2", alpha=0.5, zorder=1)
plt.title("Evolução do preço do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Preço Bitcoin ($)")
plt.show()
