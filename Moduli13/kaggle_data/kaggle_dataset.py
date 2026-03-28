import pandas as pd

df = pd.read_csv('../../Moduli14/file1.csv')
print(df.info())

first_rows = df.head()
print(first_rows)

country_data = df['Country']
print(country_data)

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ'] > 100]
print(filtered_df)

duplicated_count = df.duplicated().sum()
print("\nCount duplicate rows:")
print(duplicated_count)

average_iq_per_continent = df.groupby('Continent')[ 'Average IQ'].mean()
print(average_iq_per_continent)
