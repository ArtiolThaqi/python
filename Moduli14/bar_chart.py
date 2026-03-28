import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('file1.csv')

# Filter rows where 'Average IQ' >= 100
filtered_df = df[df["Average IQ"] >= 100]

# Sort by 'Average IQ' descending
filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

# Print to verify
print(filtered_df)

# Create figure
plt.figure(figsize=(14, 8))

# Bar chart
bars = plt.bar(filtered_df["Country"], filtered_df["Average IQ"], color="skyblue")

# Title and labels
plt.title("Average IQ by Country (IQ >= 100)", fontsize=16)
plt.xlabel("Country", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

# Rotate x labels
plt.xticks(rotation=45, ha='right')

# Grid
plt.grid(axis='y')

# Adjust layout so labels don’t get cut
plt.tight_layout()

# Show plot
plt.show()