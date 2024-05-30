library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# mpg <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de boxplot
  mpg %>%
    ggplot(aes(x = class, y = hwy)) + 
    geom_boxplot(fill = "#69b3a2", alpha = 0.5) +  
    ggtitle("Consumo de combustível por tipo de veículo") +
    xlab("categorias") +
    ylab("milhas por galão") +
    theme(legend.position = "left") + 
    guides(fill = guide_legend(title = NULL)) +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14))
