import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 5 substitui essa, pois aqui estou utilizando dados de uma base de dados do Python
# Carrega o conjunto de dados 'iris' fornecido pela seaborn
iris = sns.load_dataset('iris')

# Criar o gráfico de histograma
plt.figure(figsize=(10, 6))
# hue é a variável que agrupa os dados
sns.histplot(data=iris, x='petal_length', hue='species', binwidth=0.2, alpha=0.5, multiple='stack', palette='Set1')
plt.xlabel('Comprimento da pétala')
plt.ylabel('Frequência')
plt.title('Distribuição do comprimento da pétala por espécie de flor')
plt.tight_layout()
plt.show()
