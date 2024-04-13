import seaborn as sns
import matplotlib.pyplot as plt

mtcars = sns.load_dataset('mpg')

plt.figure(figsize=(10, 6))
sns.boxplot(x='cylinders', y='mpg', data=mtcars, hue='origin', palette=['#009E73', '#6E9AF8', '#FFA07A'])
plt.xlabel('Número de cilindros')
plt.ylabel('Milhas por galão')
plt.title('Consumo de combustível por cilindros e origem')
plt.legend(title=None)
plt.tight_layout()
plt.show()
