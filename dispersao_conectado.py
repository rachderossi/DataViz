import pandas as pd
import matplotlib.pyplot as plt

# Substitua "caminho/para/seu/arquivo.csv" pelo caminho do arquivo CSV em sua máquina
# df = pd.read_csv("caminho/para/seu/arquivo.csv")

# Cria um DataFrame com as datas e os valores correspondentes
df = pd.DataFrame({
    'Date': ["23-Abr", "22-Abr", "21-Abr", "20-Abr", "19-Abr", 
             "18-Abr", "17-Abr", "16-Abr", "15-Abr", "14-Abr"],
    'Value': [8958.55, 9001.64, 8997.57, 8880.23, 8298.69, 
              8197.80, 8285.96, 8371.15, 8338.42, 8140.71]
})

# Cria o gráfico de dispersão conectado
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='grey', markersize=6, label='_nolegend_')
plt.scatter(df['Date'], df['Value'], color='#69b3a2', edgecolor='black', s=150)
plt.title("Evolução do preço do Bitcoin")
plt.xlabel("Data")
plt.ylabel("Preço Bitcoin ($)")
plt.gca().invert_xaxis()  # Inverter o eixo x
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
