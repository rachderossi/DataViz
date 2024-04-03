import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", 
    delim_whitespace=True
)

data["date"] = pd.to_datetime(data["date"])

date = data["date"]
value = data["value"]

plt.figure(figsize=(10, 6))
plt.plot(date, value, color="#69b3a2", alpha=0.5, zorder=1)
plt.title("Evolução do preço do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Preço Bitcoin ($)")
plt.grid(True)
plt.show()
