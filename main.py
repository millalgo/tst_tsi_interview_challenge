import pandas as pd

# 1.1 Ingest the data into Python
df = pd.read_csv('data/2024-04-18_Ancient_Tree_Inventory.csv')

# 1.2 Output number of rows
# https://www.geeksforgeeks.org/python/count-the-number-of-rows-and-columns-of-a-pandas-dataframe/
rows, columns = df.shape

print(f'Count/size:       {rows}')
print(f'Number of fields: {columns}')
