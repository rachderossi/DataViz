import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv"
data = pd.read_csv(url)

data_filtered = data[data['price'] < 300]

plt.figure(figsize=(10, 6))
sns.kdeplot(data=data_filtered['price'], fill=True, color='#69b3a2', alpha=0.8)
plt.title("Distribuição de preços de aluguel")
plt.xlabel("Preço")
plt.ylabel("Densidade")
plt.grid(True)
plt.show()
