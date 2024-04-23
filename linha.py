import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Lê os dados do arquivo CSV fornecido pela URL e os carrega em um DataFrame chamado 'data'
data = pd.read_csv(
    "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", 
    delim_whitespace=True
)

# Converte a coluna 'date' para o formato de data e hora
data["date"] = pd.to_datetime(data["date"])

# Extrai as colunas 'date' e 'value' do DataFrame para facilitar a visualização
date = data["date"]
value = data["value"]

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(date, value, color="#69b3a2", alpha=0.5, zorder=1)
plt.title("Evolução do preço do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Preço Bitcoin ($)")
plt.grid(True)
plt.show()
