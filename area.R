library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Lendo os dados de um arquivo CSV hospedado em um repositório do GitHub
data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", header=T)

# Se a sua variável ordenada for uma data no formato "yyyy-mm-dd" é possível converter para um formato de data
# Convertendo a coluna de datas para o formato de data
# Isso é importante para que o gráfico reconheça as datas corretamente
data$date <- as.Date(data$date)

# Criar o gráfico de área
  data %>%
    ggplot(aes(x=date, y=value)) +
    geom_area(fill="#69b3a2", alpha=0.5) +
    geom_line(color="#69b3a2") +
    ggtitle("Evolução do preço do Bitcoin") +
    xlab("ano") +
    ylab("preço (dólar)") +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14))
