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

# Criar o gráfico de histograma
  data %>%
    filter(Price < 300) %>% # Necessário apenas se quiser filtrar valores específicos
    ggplot() +
    geom_histogram(aes(x = Price, fill = "preço"), alpha = 0.8) +  
    geom_histogram(aes(x = CompPrice, fill = "renda"),  alpha = 0.8) +  
    scale_fill_manual(values = c("#6E9AF8", "#009E73"), name= NULL) + # É possível definir cores para cada grupo
    ggtitle("Distribuição de preço e renda") +
    xlab("valor") +
    ylab("frequência") +
    guides(fill = guide_legend(title.position = "left", title.hjust = 1, title = NULL)) +
    theme_ipsum() 
