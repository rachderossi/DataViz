import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# carseats = pd.read_csv("caminho/para/seu/arquivo.csv")

# Carrega o conjunto de dados 'Carseats' da biblioteca ISLR e carrega os dados
carseats = sm.datasets.get_rdataset('Carseats', 'ISLR').data

# Filtra os dados para incluir apenas os preços de carseat menores que 300
carseats_filtered = carseats[carseats['Price'] < 300]

# Criar o gráfico de histograma
plt.figure(figsize=(10, 6))
sns.histplot(data=carseats_filtered, x='Price', color='#6E9AF8', alpha=0.8, fill=True, label='Preço')
sns.histplot(data=carseats_filtered, x='CompPrice', color='#009E73', alpha=0.8, fill=True, label='Renda')
plt.title('Distribuição de preço e renda')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.legend(title=None)
plt.tight_layout()
plt.show()
