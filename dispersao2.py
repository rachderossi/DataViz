import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='Set1', s=100)
plt.title('Relação entre comprimento e largura das sépalas por espécie')
plt.xlabel('Comprimento')
plt.ylabel('Largura')
plt.legend(title='Espécies', loc='upper left')
plt.tight_layout()
plt.show()
