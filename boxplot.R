library(dplyr)
library(ggplot2)
library(hrbrthemes)

mpg %>%
    ggplot(aes(x = class, y = hwy)) + 
    geom_boxplot(fill = "#69b3a2", alpha = 0.5) +  
    ggtitle("Consumo de combustível por tipo de veículo") +
    xlab("categorias") +
    ylab("milhas por galão") +
    theme(legend.position = "left") + 
    theme_ipsum() +
    guides(fill = guide_legend(title = NULL))
