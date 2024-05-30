library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de boxplot
  diamonds %>%
    ggplot(aes(x = cut, y = price, fill = color)) + # fill é a variável que agrupa os dados
    geom_boxplot() +
    ggtitle("Distribuição do preço dos diamantes por corte e cor") +
    xlab("corte") +
    ylab("preço (dólar)") +
    labs(fill = "cor") +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.title = element_text(size = 14),
          legend.text = element_text(size = 14))
