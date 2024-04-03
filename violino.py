import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')

plt.figure(figsize=(10, 6))
sns.violinplot(data=mpg, x='origin', y='mpg')
plt.title("Consumo de combustível por origem de veículo")
plt.xlabel("Origem")
plt.ylabel("Milhas por galão")
plt.grid(True)
plt.show()
