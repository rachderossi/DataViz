library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Lendo os dados de um arquivo CSV hospedado em um repositório do GitHub
 data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/7_OneCatOneNum.csv", header=TRUE, sep=",")

# Criar o gráfico de pirulito
  data %>%
    filter(!is.na(Value)) %>%
    arrange(Value) %>%
    tail(20) %>%
    mutate(Country=factor(Country, Country)) %>%
    ggplot( aes(x=Country, y=Value) ) +
    geom_segment( aes(x=Country ,xend=Country, y=0, yend=Value), color="grey") +
    geom_point(size=3, color="#69b3a2") +
    theme(
      panel.grid.minor.y = element_blank(),
      panel.grid.major.y = element_blank(),
      legend.position="none",
      plot.title = element_text(hjust = 0.5, size = 15)) +
    ggtitle("Quantidade de armas exportadas pelos 20 maiores exportadores em 2017") +
    xlab("países") +
    ylab("quantidade de armas") +
    coord_flip() +
    theme_ipsum() 
