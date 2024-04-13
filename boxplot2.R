library(dplyr)
library(ggplot2)
library(hrbrthemes)

diamonds %>%
ggplot(aes(x = cut, y = price, fill = color)) +
    geom_boxplot() +
    xlab("corte") +
    ylab("preço") +
    labs(fill = "cor") +
    ggtitle("Distribuição do preço dos diamantes por corte e cor") +
    theme_ipsum()
