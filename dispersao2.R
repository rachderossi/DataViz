library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# iris <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de dispersão
  iris %>%
    # color é a variável que agrupa os dados
    ggplot(aes(x = Sepal.Length, y = Sepal.Width, color = Species)) + 
    geom_point(size = 3) +
    ggtitle("Relação entre comprimento e largura das sépalas por espécie") +
    xlab("comprimento (cm)") +
    ylab("largura (cm)") +
    labs(color = "espécies") +
    theme(legend.position = "left") + 
    guides(color = guide_legend(title = NULL)) +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.title = element_text(size = 14),
          legend.text = element_text(size = 14))
