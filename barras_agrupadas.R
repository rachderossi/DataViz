library(dplyr)
library(ggplot2)
library(hrbrthemes)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# diamonds <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de barras agrupadas
  diamonds %>%
    ggplot(aes(x = cut, fill = color)) +
    geom_bar(position = "dodge") +
    ggtitle("Qualidade do corte de diamante de acordo com a cor") +
    xlab("corte") +
    ylab("frequência") +
    labs(fill = "cor") +
    theme_ipsum() 
