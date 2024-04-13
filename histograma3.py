import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

plt.figure(figsize=(10, 6))
sns.histplot(data=iris, x='petal_length', hue='species', binwidth=0.2, alpha=0.5, multiple='stack', palette='Set1')
plt.xlabel('Comprimento da pétala')
plt.ylabel('Frequência')
plt.title('Distribuição do comprimento da pétala por espécie de flor')
plt.tight_layout()
plt.show()
