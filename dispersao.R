library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(ISLR)

  data <- ISLR::Carseats
  
  data %>%
    ggplot(aes(x = CompPrice, y = Price)) + 
    geom_point(size = 3, color = "#009E73") +
    ggtitle("Relação entre o preço da mercadoria na empresa e no concorrente") +
    xlab("preço no concorrente") +
    ylab("preço na empresa") +
    theme(legend.position = "left") + 
    theme_ipsum() +
    guides(color = guide_legend(title = NULL))
