import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# carseats = pd.read_csv("caminho/para/seu/arquivo.csv")

# A linha 6 substitui essa, pois aqui estou utilizando dados de uma base de dados do Python
# Carrega o conjunto de dados 'Carseats' da biblioteca ISLR e carrega os dados
carseats = sm.datasets.get_rdataset('Carseats', 'ISLR').data

# Filtra os dados para incluir apenas os preços de carseat menores que 300
# Necessário apenas se quiser filtrar valores específicos
carseats_filtered = carseats[carseats['Price'] < 300]

# Criar o gráfico de histograma
plt.figure(figsize=(10, 6))
sns.histplot(data=carseats_filtered, x='Price', color='#6E9AF8', alpha=0.8, fill=True, label='Empresa')
sns.histplot(data=carseats_filtered, x='CompPrice', color='#009E73', alpha=0.8, fill=True, label='Concorrente')
plt.title('Distribuição conjunta dos preços dos concorrentes e da 
    empresa para assentos de carro em diferentes locais')
plt.xlabel('Preço (dólar)')
plt.ylabel('Frequência')
plt.legend(title=None)
plt.tight_layout()
plt.show()
