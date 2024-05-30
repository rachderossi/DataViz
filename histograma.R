library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Lendo os dados de um arquivo CSV hospedado em um repositório do GitHub
  data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv", header=TRUE)

# Criar o gráfico de histograma
  data %>%
    filter(price<300 ) %>% # Necessário apenas se quiser filtrar valores específicos
    ggplot(aes(x=price)) +
    ggtitle("Preço por diária de apartamentos Airbnb na Riviera Francesa") +
    xlab("preço (euro)") +
    ylab("frequência") +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14))
