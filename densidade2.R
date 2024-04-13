library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(ISLR)

  data <- ISLR::Carseats
  
  data %>%
    filter(Price < 300) %>%
    ggplot() +
    geom_density(aes(x = Price, fill = "preço"), alpha = 0.8) +  
    geom_density(aes(x = CompPrice, fill = "renda"), alpha = 0.8) +  
    scale_fill_manual(values = c("#6E9AF8", "#009E73"), name = NULL) +
    ggtitle("Distribuição de preço e renda") +
    xlab("valor") +
    ylab("densidade") +
    theme_ipsum() +
    guides(fill = guide_legend(title.position = "left", title.hjust = 1, title = NULL)) 
