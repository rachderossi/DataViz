library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de dispersão
  iris %>%
    ggplot(aes(x = Sepal.Length, y = Sepal.Width, color = Species)) + 
    geom_point(size = 3) +
    ggtitle("Relação entre comprimento e largura das sépalas por espécie") +
    xlab("comprimento") +
    ylab("largura") +
    labs(color = "espécies") +
    theme(legend.position = "left") + 
    guides(color = guide_legend(title = NULL)) +
    theme_ipsum() 
