library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(readr)

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# data <- read.csv("caminho/para/seu/arquivo.csv", header = TRUE)

# Convertendo o conjunto de dados 'mtcars' para um formato de matriz
data <- as.matrix(mtcars)

# Criar o mapa de calor
heatmap(data, Colv = NA, Rowv = NA, scale="column", main = "Mapa de calor")
