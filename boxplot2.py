import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds = pd.read_csv("caminho/para/seu/arquivo.csv")

# Carrega o conjunto de dados 'diamonds' fornecido pela seaborn
diamonds = sns.load_dataset('diamonds')

# Cria o gráfico de boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='cut', y='price', data=diamonds, hue='color', palette='Set1')
plt.title('Distribuição do preço dos diamantes por corte')
plt.xlabel('Corte')
plt.ylabel('Preço')
plt.show()
