library(dplyr)
library(ggplot2)
library(hrbrthemes)

iris %>%
  ggplot(aes(x = Sepal.Length, fill = Species)) +
    geom_density(alpha = 0.5) + 
    xlab("comprimento da sépala") +
    ylab("densidade") +
    labs(fill = "espécies") +
    ggtitle("Distribuição do comprimento da sépala por espécie de flor") +
    theme_ipsum()
