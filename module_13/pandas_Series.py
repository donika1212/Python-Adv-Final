import pandas as pd

products = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pineapples']

sales = [150, 200, 180, 90, 60]

sales_series = pd.Series(sales, index=products)

#rint(sales_series)
print(sales_series['Grapes'])

total_sales = sales_series.sum()
print(total_sales)

best_selling_product = sales_series.idxmax()
print(best_selling_product)


