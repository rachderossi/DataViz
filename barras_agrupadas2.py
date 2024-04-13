import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/hadley/data-baby-names/raw/master/baby-names.csv"
babynames = pd.read_csv(url)

names = ['Anna', 'Mary']
filtered_data = babynames[babynames['name'].isin(names)]

selected_years = [1950, 1960, 1970, 1980]
filtered_data = filtered_data[filtered_data['year'].isin(selected_years)]

data = filtered_data.pivot_table(index='year', columns='name', values='percent', aggfunc='sum', fill_value=0)

data.plot(kind='bar', stacked=False, figsize=(12, 6))
plt.xlabel('Anos')
plt.ylabel('Percentual de bebês')
plt.title('Percentual de bebês chamados Anna e Mary ao longo dos anos')
plt.legend(title=None)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
