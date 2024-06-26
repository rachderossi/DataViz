import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 5 substitui essa, pois aqui estou utilizando dados de uma base de dados do Python
# Carrega o conjunto de dados 'diamonds' fornecido pela seaborn
diamonds = sns.load_dataset('diamonds')

# Criar o gráfico de boxplot
plt.figure(figsize=(10, 6))
# hue é a variável que agrupa os dados
sns.boxplot(data=diamonds, x='cut', y='price', hue='color', palette='Set1')
plt.title('Distribuição do preço dos diamantes por corte')
plt.xlabel('Corte')
plt.ylabel('Preço (dólar)')
plt.show()
