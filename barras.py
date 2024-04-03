import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/7_OneCatOneNum.csv"
data = pd.read_csv(url)

data = data.dropna(subset=['Value']).sort_values(by='Value')
top_20 = data.tail(20)

plt.figure(figsize=(10, 8))
sns.barplot(x='Value', y='Country', data=top_20)
plt.title("Quantidade de armas exportadas pelos 20 maiores exportadores em 2017", fontsize=15)
plt.xlabel("Quantidade de armas", fontsize=12)
plt.ylabel("Países", fontsize=12)
plt.grid(axis='x')
plt.show()
