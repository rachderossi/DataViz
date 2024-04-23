from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# paises = pd.read_csv("caminho/para/seu/arquivo.csv")

# Lista de países e suas frequências
paises = ["Brasil", "Estados Unidos", "Canadá", "Reino Unido", "França", "Alemanha", "Austrália", "Japão", "China", "Índia"]
frequencias = [50, 30, 40, 35, 25, 20, 45, 15, 10, 5]

# Criar um dicionário com as palavras e suas frequências
word_freq = {paises[i]: frequencias[i] for i in range(len(paises))}

# Criar o gráfico de nuvem de palavras
wordcloud = WordCloud(width=800, height=400, colormap='Dark2').generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
