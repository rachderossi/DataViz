import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds = pd.read_csv("caminho/para/seu/arquivo.csv")

# Carrega o conjunto de dados 'diamonds' fornecido pela seaborn
diamonds = sns.load_dataset('diamonds')

# Criar o gráfico de barras agrupadas
plt.figure(figsize=(10, 6))
# hue é a variável que agrupa os dados
sns.countplot(data=diamonds, x='cut', hue='color', palette='pastel', dodge=True)
plt.title('Qualidade do corte de diamante de acordo com a cor')
plt.xlabel('Corte')
plt.ylabel('Frequência')
plt.legend(title='Cor')
plt.show()
