import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# df = pd.read_csv("caminho/para/seu/arquivo.csv")

# Define a URL do arquivo CSV contendo os dados dos carros
url = 'https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/mtcars.csv'

# Lê os dados do arquivo CSV e os carrega em um DataFrame chamado 'df'
df = pd.read_csv(url)

# Define a coluna 'model' como índice do DataFrame
df = df.set_index('model')

# Define uma paleta de cores personalizada com base no número de cilindros dos carros
# Cada número de cilindros é mapeado para uma cor específica
my_palette = dict(zip(df.cyl.unique(), ["orange","yellow","brown"]))
row_colors = df.cyl.map(my_palette)

# Criar o mapa de calor
sns.clustermap(df, metric="correlation", method="single", cmap="Blues", standard_scale=1, row_colors=row_colors)
plt.show()
