library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de histograma
    iris %>%
      # fill é a variável que agrupa os dados
      ggplot(aes(x = Petal.Length, fill = Species)) +
      geom_histogram(binwidth = 0.2, alpha = 0.5, position = "identity") +
      ggtitle("Distribuição do comprimento da sépala por espécie de flor") +
      xlab("comprimento da pétala") +
      ylab("frequência") +
      labs(fill = "espécies") +
      theme_ipsum()
