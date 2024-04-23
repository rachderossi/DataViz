library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data_freq <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Conta a frequência de cada classe de veículo
freq_class <- table(mpg$class)

# Cria um data frame com os dados da frequência
data_freq <- data.frame(class = names(freq_class), freq = as.numeric(freq_class))

# Ordena o data frame pela frequência em ordem ascendente
data_freq <- arrange(data_freq, freq)

# Cria o gráfico de pirulito
  data_freq %>%
    ggplot(aes(x = reorder(class, freq), y = freq)) +
    geom_segment(aes(xend = reorder(class, freq), yend = 0), color = "black") +
    geom_point(size = 4, color = "#6E9AF8") +
    ggtitle("Distribuição das classes de veículo") +
    xlab("classe") +
    ylab("frequência") +
    coord_flip() +
    theme_ipsum()
