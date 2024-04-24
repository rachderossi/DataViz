library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de densidade
  iris %>%
    ggplot(aes(x = Sepal.Length, fill = Species)) +  # fill é a variável que agrupa os dados
    geom_density(alpha = 0.5) + 
    ggtitle("Distribuição do comprimento da sépala por espécie de flor") +
    xlab("comprimento da sépala") +
    ylab("densidade") +
    labs(fill = "espécies") +
    theme_ipsum()
