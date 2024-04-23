library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(babynames)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# name <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Filtrando o conjunto de dados babynames pelo nome e sexo de interesse
  name <- babynames %>%
    filter(name %in% c("Ashley", "Patricia", "Helen")) %>%
    filter(sex == "F")

# Criar o gráfico de linha
  name %>%
    ggplot(aes(x = year, y = n, group = name, color = name)) +
    geom_line() +
    scale_color_manual(values = c("#6E9AF8", "#009E73", "#FFA07A"), name = NULL) +
    ggtitle("Popularidade de nomes Americanos nos últimos 30 Anos") +
    xlab("ano") +
    ylab("número de bebês") +
    guides(color = guide_legend(title.position = "left", title.hjust = 1, title = NULL)) +
    theme_ipsum() 
