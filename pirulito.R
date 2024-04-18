library(dplyr)
library(ggplot2)
library(hrbrthemes)

# Contar a frequência de cada classe de veículo
freq_class <- table(mpg$class)

# Criar um data frame com os dados da frequência
data_freq <- data.frame(class = names(freq_class), freq = as.numeric(freq_class))

# Ordenar o data frame pela frequência em ordem ascendente
data_freq <- arrange(data_freq, freq)

data_freq %>%
  ggplot(aes(x = reorder(class, freq), y = freq)) +
  geom_segment(aes(xend = reorder(class, freq), yend = 0), color = "black") +
  geom_point(size = 4, color = "#6E9AF8") +
  coord_flip() +
  xlab("classe") +
  ylab("frequência") +
  ggtitle("Distribuição das classes de veículo") +
  theme_ipsum()
