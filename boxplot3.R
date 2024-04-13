library(dplyr)
library(ggplot2)
library(hrbrthemes)

mtcars %>%
  ggplot(aes(x = as.factor(cyl), y = mpg, fill = factor(am, labels = c("Automático", "Manual")))) +
    geom_boxplot() +
    xlab("número de cilindros") +
    ylab("milhas por galão") +
    ggtitle("Consumo de combustível por cilindros e tipo de transmissão") +
    scale_fill_manual(values = c("#009E73", "#6E9AF8")) +
    theme_ipsum() +
    guides(fill = guide_legend(title = NULL))
