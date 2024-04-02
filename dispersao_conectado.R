library(dplyr)
library(ggplot2)
library(hrbrthemes)

df <- tibble(
  Date = c(
    "23-Abr", "22-Abr", "21-Abr", "20-Abr", "19-Abr", 
    "18-Abr", "17-Abr", "16-Abr", "15-Abr", "14-Abr"
  ),
  Value = c(
    8958.55, 9001.64, 8997.57, 8880.23, 8298.69, 8197.80, 8285.96, 8371.15, 8338.42, 
    8140.71
  ))


df %>%
  ggplot(aes(x=Date, y=Value)) +
  geom_point(shape=21, color="black", fill="#69b3a2", size=6) +
  geom_line(color="grey", aes(group=1)) +
  ggtitle("Evolução do preço do Bitcoin") +
  xlab("Data") +
  ylab("Preço Bitcoin ($)") +
  theme_ipsum() 
