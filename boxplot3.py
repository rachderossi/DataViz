import seaborn as sns
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds = pd.read_csv("caminho/para/seu/arquivo.csv")

# Carrega o conjunto de dados 'mtcars' fornecido pela seaborn
mtcars = sns.load_dataset('mpg')

# Cria o gráfico dee boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='cylinders', y='mpg', data=mtcars, hue='origin', palette=['#009E73', '#6E9AF8', '#FFA07A'])
plt.title('Consumo de combustível por cilindros e origem')
plt.xlabel('Número de cilindros')
plt.ylabel('Milhas por galão')
plt.legend(title=None)
plt.tight_layout()
plt.show()
