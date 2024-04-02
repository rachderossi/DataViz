library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(gapminder)
library(viridis)

data <- gapminder %>% filter(year=="2007") %>% dplyr::select(-year)

data %>%
  mutate(pop=pop/1000000) %>%
  arrange(desc(pop)) %>%
  mutate(country = factor(country, country)) %>%
  ggplot( aes(x=gdpPercap, y=lifeExp, size = pop, color = continent)) +
  geom_point(alpha=0.7) +
  scale_size(range = c(1.4, 19), name="Population (M)") +
  scale_color_viridis(discrete=TRUE, guide=FALSE) +
  ggtitle("Relação entre PIB per capita e expectativa de vida no ano de 2007") +
  xlab("PIB per capita") +
  ylab("Expectativa de vida") +
  theme(legend.position = "right") + 
  theme_ipsum() 
