import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

carseats = sm.datasets.get_rdataset('Carseats', 'ISLR').data

plt.figure(figsize=(10, 6))
sns.scatterplot(data=carseats, x='CompPrice', y='Price', color='#009E73', s=100, edgecolor='black')
plt.title('Relação entre o preço da mercadoria na empresa e no concorrente')
plt.xlabel('Preço no concorrente')
plt.ylabel('Preço na empresa')
plt.legend([], [], frameon=False) 
plt.tight_layout()
plt.show()
