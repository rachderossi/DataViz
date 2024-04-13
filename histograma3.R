library(dplyr)
library(ggplot2)
library(hrbrthemes)
  
iris %>%
  ggplot(aes(x = Petal.Length, fill = Species)) +
    geom_histogram(binwidth = 0.2, alpha = 0.5, position = "identity") +  
    xlab("comprimento da pétala") +
    ylab("frequência") +
    labs(fill = "espécies") +
    ggtitle("Distribuição do comprimento da sépala por espécie de flor") +
    theme_ipsum()
