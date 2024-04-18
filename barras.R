library(dplyr)
library(ggplot2)
library(hrbrthemes)

  mpg %>%
    count(class) %>%
    mutate(class = reorder(class, n)) %>%
    ggplot(aes(x = class, y = n)) + 
    geom_bar(fill = "#6E9AF8", stat = "identity") +  
    xlab("Classe") +
    ylab("Frequência") +
    ggtitle("Distribuição das classes de veículo") +
    theme_ipsum()
