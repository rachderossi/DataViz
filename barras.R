library(dplyr)
library(ggplot2)
library(hrbrthemes)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# mpg <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de barras
 mpg %>%
    count(class) %>%
    mutate(class = reorder(class, n)) %>%
    ggplot(aes(x = class, y = n)) + 
    geom_bar(fill = "#6E9AF8", stat = "identity") + 
    ggtitle("Distribuição das classes de veículo") +
    xlab("classe") +
    ylab("frequência") +
    theme_ipsum()
