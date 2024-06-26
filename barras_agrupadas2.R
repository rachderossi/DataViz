library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(babynames)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Filtrando o conjunto de dados babynames pelo nome e sexo de interesse
# Caso não seja necessário filtrar seus dados pule para a linha 17
  data <- babynames %>% 
    filter(name %in% c("Anna", "Mary")) %>%
    filter(sex=="F")

# Criar o gráfico de barras agrupadas
  data  %>% 
    filter(year %in% c(1950, 1960, 1970, 1980, 1990, 2000)) %>% # Necessário apenas se quiser filtrar valores específicos
    mutate(year=as.factor(year)) %>% # Transformando o ano para uma variável categórica
    # Caso exista, substitua n pela sua variável de frequência, fill é a variável que agrupa os dados
    ggplot( aes(x=year, y=n, fill=name)) +  
    geom_bar(stat="identity", position="dodge") +
    scale_fill_manual(values = c("Anna" = "#6E9AF8", "Mary" = "#69b3a2")) + # É possível definir cores para cada grupo
    ggtitle("Número de bebês chamados Anna e Mary 
            nos EUA ao longo dos anos") +
    ylab("número de bebês") +
    xlab("anos") +
    guides(fill = guide_legend(title = NULL)) +
    theme_ipsum() +
    theme(axis.text.x = element_text(size = 14),
          axis.text.y = element_text(size = 14),
          axis.title.x = element_text(size = 14),
          axis.title.y = element_text(size = 14),
          legend.text = element_text(size = 14))
