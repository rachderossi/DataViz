import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame de exemplo similar ao 'mpg'
data = {
    'class': ['compact', 'midsize', 'suv', 'midsize', 'compact', 'suv', 'suv', 'compact'],
}
mpg = pd.DataFrame(data)

# Contando as ocorrências de cada classe
class_counts = mpg['class'].value_counts().reset_index()
class_counts.columns = ['class', 'count']

class_counts = class_counts.sort_values(by='count')

plt.figure(figsize=(10, 6))
plt.bar(class_counts['class'], class_counts['count'], color='#6E9AF8')
plt.ylabel('Frequência')
plt.xlabel('Classe')
plt.title('Distribuição das classes de veículo')
plt.xticks(rotation=45)
plt.show()
