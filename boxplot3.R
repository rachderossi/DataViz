library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# mtcars <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de boxplot
  mtcars %>%
    # A variável x está sendo convertida para fator, pois "cyl" é uma variável numérica
    # fill é a variável que agrupa os dados
    # labels define o nome de cada grupo, é possível ser customizado pela quantidade de grupos 
    ggplot(aes(x = as.factor(cyl), y = mpg, fill = factor(am, labels = c("Automático", "Manual")))) +
    geom_boxplot() +
    ggtitle("Consumo de combustível por cilindros e tipo de transmissão") +
    xlab("número de cilindros") +
    ylab("milhas por galão") +
    scale_fill_manual(values = c("#009E73", "#6E9AF8")) + # É possível definir cores para cada grupo
    guides(fill = guide_legend(title = NULL)) +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.text = element_text(size = 14))
