import pandas as pd
import matplotlib.pyplot as plt

freq_class = mpg['class'].value_counts()

data_freq = pd.DataFrame({'class': freq_class.index, 'freq': freq_class.values})

data_freq = data_freq.sort_values(by='freq')

plt.figure(figsize=(10, 6))
plt.hlines(y=data_freq['class'], xmin=0, xmax=data_freq['freq'], color='black')
plt.plot(data_freq['freq'], data_freq['class'], 'o', color='#6E9AF8', markersize=8)
plt.xlabel('Frequência')
plt.ylabel('Classe')
plt.title('Distribuição de classes de veículos')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
