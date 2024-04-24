library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# mpg <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de barras
 mpg %>%
    count(class) %>% # substitua class pela sua variável categórica
    # caso exista, substitua n pela sua variável de frequência
    mutate(class = reorder(class, n)) %>% # ordenando a variável pela frequência
    ggplot(aes(x = class, y = n)) + 
    geom_bar(fill = "#6E9AF8", stat = "identity") + 
    ggtitle("Distribuição das classes de veículo") +
    xlab("classe") +
    ylab("frequência") +
    theme_ipsum()
