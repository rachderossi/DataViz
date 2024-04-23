library(dplyr)
library(ggplot2)
library(hrbrthemes)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de boxplot
  diamonds %>%
    ggplot(aes(x = cut, y = price, fill = color)) +
    geom_boxplot() +
    ggtitle("Distribuição do preço dos diamantes por corte e cor") +
    xlab("corte") +
    ylab("preço") +
    labs(fill = "cor") +
    theme_ipsum()
