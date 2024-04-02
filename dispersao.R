library(dplyr)
library(ggplot2)
library(hrbrthemes)

ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) + 
  geom_point(size = 3) +
  ggtitle("Relação entre comprimento e largura das sépalas por espécie") +
  xlab("Comprimento") +
  ylab("Largura") +
  labs(color = "Espécies") +
  theme(legend.position = "right") + 
  theme_ipsum() +
  guides(color = guide_legend(title = NULL))
