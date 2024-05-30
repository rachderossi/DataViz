library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(ISLR)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# A linha 8 substitui essa, pois aqui estou utilizando dados de uma base de dados do R
# Lendo o conjunto de dados Carseats do pacote ISLR
  data <- ISLR::Carseats

# Criar o gráfico de dispersão
  data %>%
    ggplot(aes(x = CompPrice, y = Price)) + 
    geom_point(size = 3, color = "#009E73") +
    ggtitle("Relação entre o preço da mercadoria na empresa e concorrente") +
    xlab("preço no concorrente (dólar)") +
    ylab("preço na empresa (dólar)") +
    theme(legend.position = "left") + 
    guides(color = guide_legend(title = NULL)) +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14))
