import pandas as pd
from datetime import datetime

def dt_to_iso(dt):
# https://www.geeksforgeeks.org/python/python-pandas-timestamp-isoformat/
# https://www.geeksforgeeks.org/python/python-pandas-to_datetime/
    try:
        return pd.to_datetime(dt).isoformat()
    except:
        return None

# 1.1 Ingest the data into Python
df = pd.read_csv('data/2024-04-18_Ancient_Tree_Inventory.csv')

# 1.2 Output number of rows
# https://www.geeksforgeeks.org/python/count-the-number-of-rows-and-columns-of-a-pandas-dataframe/
rows, columns = df.shape

print(f'Count/size:       {rows}')
print(f'Number of fields: {columns}')

# 1.3.1 Convert any date/time fields to ISO 8601 format (YYYY-MM-DDThh:mm:ss)
# https://www.geeksforgeeks.org/python/apply-a-function-to-each-row-or-column-in-dataframe-using-pandas-apply/
df['SurveyDate'] = df['SurveyDate'].apply(dt_to_iso)
df['VerifiedDate'] = df['VerifiedDate'].apply(dt_to_iso)

print(df)
