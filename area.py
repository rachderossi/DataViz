import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Lê os dados do arquivo CSV de um URL e os carrega em um DataFrame chamado 'data'
data = pd.read_csv(
    "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", 
    delim_whitespace=True
)

# Se a sua variável ordenada for uma data no formato "yyyy-mm-dd" é possível converter para um formato de data
# Converte a coluna 'date' para o tipo datetime
# Isso é importante para que o gráfico reconheça as datas corretamente
data["date"] = pd.to_datetime(data["date"])

# Criar o gráfico de área
plt.figure(figsize=(10, 6))
# date é a variável x e value é a variável y
plt.fill_between(data['date'], data['value'], color="#69b3a2", alpha=0.5, zorder=1)
plt.title("Evolução do preço do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Preço (dólar)")
plt.show()
