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
    xlab("comprimento da sépala (cm)") +
    ylab("densidade") +
    labs(fill = "espécies") +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.title = element_text(size = 14),
          legend.text = element_text(size = 14))
