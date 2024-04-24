import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# carseats = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 6 substitui essa, pois aqui estou utilizando dados de uma base de dados do Python
# Carrega o conjunto de dados 'Carseats' da biblioteca ISLR e carrega os dados
carseats = sm.datasets.get_rdataset('Carseats', 'ISLR').data

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=carseats, x='CompPrice', y='Price', color='#009E73', s=100, edgecolor='black')
plt.title('Relação entre o preço da mercadoria na empresa e no concorrente')
plt.xlabel('Preço no concorrente')
plt.ylabel('Preço na empresa')
plt.legend([], [], frameon=False) 
plt.tight_layout()
plt.show()
