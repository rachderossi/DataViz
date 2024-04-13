import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset('diamonds')

plt.figure(figsize=(10, 6))
sns.boxplot(x='cut', y='price', data=diamonds, hue='color', palette='Set1')
plt.xlabel('Corte')
plt.ylabel('Preço')
plt.title('Distribuição do preço dos diamantes por corte')
plt.show()
