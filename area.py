import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv"
data = pd.read_csv(url)

data[['date', 'value']] = data['date value'].str.split(expand=True)
data.drop(columns=['date value'], inplace=True)
data['date'] = pd.to_datetime(data['date'])

plt.figure(figsize=(10, 6))
plt.fill_between(data['date'], data['value'], color="#69b3a2", alpha=0.5, zorder=1)
plt.title("Evolução do preço do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Preço Bitcoin ($)")
plt.show()
