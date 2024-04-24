library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Lendo os dados de um arquivo CSV hospedado em um repositório do GitHub
  data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv", header=TRUE)

# Criar o gráfico de densidade
  data %>%
    filter(price<300 ) %>% # necessário apenas se quiser filtrar valores específicos
    ggplot(aes(x=price)) +
    geom_density(fill="#69b3a2", color="#e9ecef", alpha=0.8) +
    ggtitle("Distribuição de preços de aluguel") +
    xlab("preço") +
    ylab("densidade") +
    theme_ipsum()
