library(dplyr)
library(ggplot2)
library(hrbrthemes)
library(wordcloud)

paises <- c("Brasil", "Estados Unidos", "Canadá", "Reino Unido", "França", "Alemanha", "Austrália", "Japão", "China", "Índia")
frequencias <- c(50, 30, 40, 35, 25, 20, 45, 15, 10, 5)
df_paises <- data.frame(Pais = paises, Frequencia = frequencias)

wordcloud(words = df_paises$Pais, freq = df_paises$Frequencia, scale = c(5, 0.5), 
          max.words = 10, min.freq = 1, random.order = FALSE, 
          colors=brewer.pal(8, "Dark2"))
