import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv"
data = pd.read_csv(url)

data_filtered = data[data['price'] < 300]

plt.figure(figsize=(10, 6))
plt.hist(data_filtered['price'], bins=20, color='#69b3a2', edgecolor='#e9ecef', alpha=0.8)
plt.title("Distribuição de preços de aluguel")
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()
