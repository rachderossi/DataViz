import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diamonds = sns.load_dataset('diamonds')

plt.figure(figsize=(10, 6))
sns.countplot(data=diamonds, x='cut', hue='color', palette='pastel', dodge=True)
plt.xlabel('Corte')
plt.ylabel('Frequência')
plt.title('Qualidade do corte de diamante de acordo com a cor')
plt.legend(title='Cor')
plt.show()
