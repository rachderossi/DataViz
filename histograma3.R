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
      ggtitle("Distribuição do comprimento da pétala por espécie de flor") +
      xlab("comprimento da pétala (cm)") +
      ylab("frequência") +
      labs(fill = "espécies") +
      theme_ipsum() +
      theme(axis.text.x = element_text(size = 14),
            axis.text.y = element_text(size = 14),
            axis.title.x = element_text(size = 14),
            axis.title.y = element_text(size = 14),
            legend.title = element_text(size = 14),
            legend.text = element_text(size = 14))
