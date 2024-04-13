library(dplyr)
library(ggplot2)
library(hrbrthemes)

mpg %>%
ggplot(aes(x = class)) + 
    geom_bar(fill = "#6E9AF8") +  
    coord_flip() +
    xlab("classe") +
    ylab("frequência") +
    ggtitle("Distribuição das classes de veículo") +
    theme_ipsum() 
