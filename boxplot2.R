  ggplot(diamonds, aes(x = cut, y = price, fill = cut)) +
    geom_boxplot() +
    xlab("corte") +
    ylab("preço") +
    labs(fill = "cor") +
    ggtitle("Distribuição do preço dos diamantes por corte e cor") +
    theme_ipsum()
