import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('file1.csv')

# Group by continent and sum Nobel prizes
nobel_prizes_by_continent = df.groupby('Continent')['Nobel Prices'].sum()

# Count number of continents
no_of_continents = nobel_prizes_by_continent.count()
print(no_of_continents)

# Colors for pie chart
colors = ['gold', 'lightcoral', 'yellow', 'thistle', 'orange',
          'lightskyblue', 'aquamarine', 'burlywood']

# Create figure
plt.figure(figsize=(10, 10))

# Plot pie chart (FIXED autopct)
nobel_prizes_by_continent.plot(
    kind='pie',
    colors=colors,
    autopct='%1.1f%%'
)

# Title and formatting
plt.title('Distribution of Prizes by Continent')
plt.axis('equal')   # Makes circle perfect
plt.ylabel('')      # Removes y-label
plt.tight_layout()

# Show plot
plt.show()