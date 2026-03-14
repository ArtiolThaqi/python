import pandas as pd

products = ['Apples','Bananas','Oranges','Grapes','Pineapples']
sales = [150,200,160,90,60]
sales_series = pd.Series(sales, index=products)
print(sales_series)
print(sales_series['Grapes'])

total_series = sales_series.sum()
print(total_series)

best_selling_products = sales_series.idxmax()
print(f"best selling product: {best_selling_products}")

