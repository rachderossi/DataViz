library(dplyr)
library(ggplot2)
library(hrbrthemes)

  ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) + 
    geom_point(size = 3) +
    ggtitle("Relação entre comprimento e largura das sépalas por espécie") +
    xlab("comprimento") +
    ylab("largura") +
    labs(color = "espécies") +
    theme(legend.position = "left") + 
    theme_ipsum() +
    guides(color = guide_legend(title = NULL))
