import matplotlib.pyplot as plt
import seaborn as sns

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# mpg = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 5 substitui essa, pois aqui estou utilizando dados de uma base de dados do Python
# Carrega o conjunto de dados 'mpg' fornecido pela seaborn
mpg = sns.load_dataset('mpg')

# Criar o gráfico de boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=mpg, x='origin', y='mpg')
plt.title("Consumo de combustível por origem de veículo")
plt.xlabel("Origem")
plt.ylabel("Milhas por galão")
plt.grid(True)
plt.show()
