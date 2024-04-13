import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=iris, x='sepal_length', hue='species', fill=True, alpha=0.5)
plt.xlabel('Comprimento da sépala')
plt.ylabel('Densidade')
plt.title('Distribuição do comprimento da sépala por espécie de flor')
plt.tight_layout()
plt.show()
