library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de barras agrupadas
  diamonds %>%
    # fill é a variável que agrupa os dados
    ggplot(aes(x = cut, fill = color)) +
    geom_bar(position = "dodge") +
    ggtitle("Qualidade do corte de diamante de acordo com a cor") +
    xlab("corte") +
    ylab("frequência") +
    labs(fill = "cor") +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.title = element_text(size = 14),
          legend.text = element_text(size = 14))
