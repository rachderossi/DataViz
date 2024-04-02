library(dplyr)
library(ggplot2)
library(hrbrthemes)

data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv", header=TRUE)

data %>%
  filter( price<300 ) %>%
  ggplot( aes(x=price)) +
  geom_histogram(fill="#69b3a2", color="#e9ecef", alpha=0.8) +
  ggtitle("Distribuição de preços de aluguel") +
  xlab("preço") +
  ylab("frequência") +
  theme_ipsum()
