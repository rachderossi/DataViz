library(dplyr)
library(ggplot2)
library(hrbrthemes)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# mtcars <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Criar o gráfico de boxplot
  mtcars %>%
    ggplot(aes(x = as.factor(cyl), y = mpg, fill = factor(am, labels = c("Automático", "Manual")))) +
    geom_boxplot() +
    ggtitle("Consumo de combustível por cilindros e tipo de transmissão") +
    xlab("número de cilindros") +
    ylab("milhas por galão") +
    scale_fill_manual(values = c("#009E73", "#6E9AF8")) +
    guides(fill = guide_legend(title = NULL)) +
    theme_ipsum() 
