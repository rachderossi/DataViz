library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(babynames)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# name <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Filtrando o conjunto de dados babynames pelo nome e sexo de interesse
# Caso não seja necessário filtrar seus dados pule para a linha 17
  name <- babynames %>%
    filter(name %in% c("Ashley", "Patricia", "Helen")) %>%
    filter(sex == "F")

# Criar o gráfico de linha
  name %>%
    # Caso exista, substitua n pela sua variável de frequência, group é a variável que agrupa os dados
    ggplot(aes(x = year, y = n, group = name, color = name)) +
    geom_line() +
    scale_color_manual(values = c("#6E9AF8", "#009E73", "#FFA07A"), name = NULL) + # É possível definir cores para cada grupo
    ggtitle("Popularidade dos nomes Ashley, Patrícia e Helen
                 nos EUA entre (1880-2020) ") +
    xlab("ano") +
    ylab("número de bebês") +
    guides(color = guide_legend(title.position = "left", title.hjust = 1, title = NULL)) +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.text = element_text(size = 14))
