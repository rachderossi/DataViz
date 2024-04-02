import matplotlib.pyplot as plt
import seaborn as sns
from gapminder import gapminder 

data = gapminder.loc[gapminder.year == 2007]

sns.scatterplot(data=data, x="gdpPercap", y="lifeExp", size="pop", sizes=(20, 2000))
plt.title("Relação entre PIB per capita e expectativa de vida no ano de 2007")
plt.xlabel("PIB per capita")
plt.ylabel("Expectativa de vida")
plt.legend(title=None, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
