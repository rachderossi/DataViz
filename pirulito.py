import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame de exemplo similar ao 'mpg'
data = {
    'class': ['compact', 'midsize', 'suv', 'midsize', 'compact', 'suv', 'suv', 'compact'],
}
mpg = pd.DataFrame(data)

# Contando as ocorrências de cada classe
class_counts = mpg['class'].value_counts().reset_index()
class_counts.columns = ['class', 'freq']

# Ordenando o DataFrame pela frequência em ordem ascendente
class_counts = class_counts.sort_values(by='freq')

plt.figure(figsize=(10, 6))
plt.hlines(y=class_counts['class'], xmin=0, xmax=class_counts['freq'], color='black')
plt.plot(class_counts['freq'], class_counts['class'], 'o', color='#6E9AF8', markersize=8)
plt.xlabel('Frequência')
plt.ylabel('Classe')
plt.title('Distribuição das classes de veículo')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.show()
