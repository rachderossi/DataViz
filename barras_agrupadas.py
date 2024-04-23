import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data = pd.read_csv("caminho/para/seu/arquivo.csv")

# Carrega o conjunto de dados 'diamonds' fornecido pela seaborn
diamonds = sns.load_dataset('diamonds')

# Cria o gráfico de barras agrupadas
plt.figure(figsize=(10, 6))
sns.countplot(data=diamonds, x='cut', hue='color', palette='pastel', dodge=True)
plt.xlabel('Corte')
plt.ylabel('Frequência')
plt.title('Qualidade do corte de diamante de acordo com a cor')
plt.legend(title='Cor')
plt.show()
