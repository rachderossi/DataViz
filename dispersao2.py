import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris = pd.read_csv("caminho/para/seu/arquivo.csv")

# Carrega o conjunto de dados 'iris' fornecido pela seaborn
iris = sns.load_dataset('iris')

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='Set1', s=100)
plt.title('Relação entre comprimento e largura das sépalas por espécie')
plt.xlabel('Comprimento')
plt.ylabel('Largura')
plt.legend(title='Espécies', loc='upper left')
plt.tight_layout()
plt.show()
