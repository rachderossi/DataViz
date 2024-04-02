library(dplyr)
library(ggplot2)
library(hrbrthemes)

data <- as.matrix(mtcars)

heatmap(data, Colv = NA, Rowv = NA, scale="column", main = "Mapa de calor")
