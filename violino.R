library(dplyr)
library(ggplot2)
library(hrbrthemes)

mpg %>%
  mutate(Tipo = ifelse(class == "subcompact", "Destacado", "Normal")) %>%
  ggplot(aes(x = class, y = hwy, fill = Tipo)) + 
  geom_violin() +
  scale_fill_manual(values = c("#69b3a2", "#e9ecef")) +
  scale_alpha_manual(values = c(1, 0.1)) +
  ggtitle("Consumo de combustível por tipo de veículo") +
  xlab("Categorias") +
  ylab("Milhas por Galão") +
  theme(legend.position = "right") + 
  theme_ipsum() +
  guides(fill = guide_legend(title = NULL))
