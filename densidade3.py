import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 5 substitui essa, pois aqui estou utilizando dados de uma base de dados do Python
# Carrega o conjunto de dados 'iris' fornecido pela seaborn
iris = sns.load_dataset('iris')

# Criar o gráfico de densidade
plt.figure(figsize=(10, 6))
# hue é a variável que agrupa os dados
sns.kdeplot(data=iris, x='sepal_length', hue='species', fill=True, alpha=0.5)
plt.title('Distribuição do comprimento da sépala por espécie de flor')
plt.xlabel('Comprimento da sépala')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()
