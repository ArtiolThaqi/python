import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('file1.csv')

print(df.info())

# Histogram
plt.figure(figsize=(10,6))
sns.histplot(df['Average IQ'])
plt.title('Histogram of Average IQ')
plt.xlabel('Average IQ')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ❌ E kemi heq këtë pjesë (nuk duhet)

print(df.info())

# Heatmap
numeric_iq_data_loc = df.select_dtypes(include=['number'])

plt.figure(figsize=(10,6))
sns.heatmap(numeric_iq_data_loc.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(12,6))
sns.set_style("darkgrid")
sns.boxplot(data=df, x='Continent', y='Average IQ')
plt.title('Boxplot of Average IQ by Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')
plt.tight_layout()
plt.show()