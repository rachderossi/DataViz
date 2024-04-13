library(dplyr)
library(ggplot2)
library(hrbrthemes)

  data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", header=T)
  data$date <- as.Date(data$date)
  
  data %>%
    ggplot( aes(x=date, y=value)) +
    geom_line(color="#69b3a2") +
    ggtitle("Evolução do preço do Bitcoin") +
    xlab("ano") +
    ylab("preço do Bitcoin ($)") +
    theme_ipsum()
