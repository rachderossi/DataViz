library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(babynames)

data <- babynames %>% 
    filter(name %in% c("Anna", "Mary")) %>%
    filter(sex=="F")
  
  data  %>% 
    filter(year %in% c(1950, 1960, 1970, 1980, 1990, 2000)) %>%
    mutate(year=as.factor(year)) %>%
    ggplot( aes(x=year, y=n, fill=name)) +
    geom_bar(stat="identity", position="dodge") +
    scale_fill_manual(values = c("Anna" = "#6E9AF8", "Mary" = "#69b3a2")) + 
    theme_ipsum() +
    ylab("número de bebês") +
    xlab("anos") +
    ggtitle("Número de bebês chamados Anna e Mary ao longo dos anos") +
    guides(fill = guide_legend(title = NULL))