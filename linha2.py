import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided URL
url = "https://github.com/hadley/data-baby-names/raw/master/baby-names.csv"
baby_names = pd.read_csv(url)

# Filter the data for the specified names and sex
names = ['Ashley', 'Patricia', 'Helen']
sex = 'girl'
filtered_data = baby_names[(baby_names['name'].isin(names)) & (baby_names['sex'] == sex)]

# Plotting
plt.figure(figsize=(10, 6))
for name, color in zip(names, ['#6E9AF8', '#009E73', '#FFA07A']):
    data = filtered_data[filtered_data['name'] == name]
    plt.plot(data['year'], data['percent'], label=name, color=color)
plt.title('Popularity of American Names Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Babies')
plt.legend(title='Name', loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
