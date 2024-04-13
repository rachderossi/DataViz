library(dplyr)
library(ggplot2)
library(hrbrthemes)

ggplot(diamonds, aes(x = cut, fill = color)) +
    geom_bar(position = "dodge") +
    xlab("corte") +
    ylab("frequência") +
    labs(fill = "cor") +
    ggtitle("Qualidade do corte de diamante de acordo com a cor") +
    theme_ipsum() 
