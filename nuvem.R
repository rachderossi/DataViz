library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(wordcloud)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# paises <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Cria um vetor chamado 'paises' contendo os nomes dos países
paises <- c("Brasil", "Estados Unidos", "Canadá", "Reino Unido", "França", "Alemanha", "Austrália", "Japão", "China", "Índia")

# Cria um vetor chamado 'frequencias' contendo as frequências associadas a cada país
frequencias <- c(50, 30, 40, 35, 25, 20, 45, 15, 10, 5)

# Cria um dataframe chamado 'df_paises' com duas colunas: 'Pais', contendo os nomes dos países, e 'Frequencia', 
# contendo as frequências associadas a cada país
df_paises <- data.frame(Pais = paises, Frequencia = frequencias)

# Cria o gráfico de nuvem de palavras
wordcloud(words = df_paises$Pais, freq = df_paises$Frequencia, scale = c(5, 0.5), 
          max.words = 10, min.freq = 1, random.order = FALSE, 
          colors=brewer.pal(8, "Dark2"))
