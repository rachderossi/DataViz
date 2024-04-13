library(dplyr)
library(ggplot2)
library(hrbrthemes)

  data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", header = TRUE)
  data$date <- as.Date(data$date)
  
  data_filtrado <- data %>%
    filter(format(date, "%Y-%m") == "2018-04")
  
  ggplot(data_filtrado, aes(x = date, y = value)) +
    geom_point(shape=21, color="black", fill="#69b3a2", size=2) +
    geom_line(color = "#69b3a2") +
    ggtitle("Evolução do preço do Bitcoin em abril de 2018") +
    xlab("data") +
    ylab("preço do Bitcoin ($)") +
    theme_ipsum()
