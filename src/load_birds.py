import os
import pandas as pd

df = pd.read_csv('FILE NAME', sep='\t', usecols=useful_columns, dtype=column_types)

needs = ['species', 'eventDate', 'decimalLatitude', 'decimalLongitude']

rename_ease = {
  'eventDate': 'date'
  'decimalLatitude': 'lat'
  'decimalLongitude': 'long'
}

df.rename(columns=rename_ease, inplace=True)

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year
df["week"] = df["date"].dt.isocalendar().week

df_clean = df_clear.dropna(subset = ['date', 'lat', 'long'])
#round the values
df_clean['lat_grid'] = df_clean['lat'].round(0).astype(int)
df_clean['long_grid'] = df_clean['long'].round(0).astype(int)
#present them
df_clean['region'] = df_clean['lat_grid'].astype(str) + "_" + df_clean['long_grid'].astype(str)
#drop the temporary columns
df_clean.drop(columns=['lat_grid', 'long_grid'], inplace=True)

print(f"Number of rows: {len(df_clean)}")
print(f"Date range: {df_clean['date'].min()} to {df_clean['date'].max()}")
print(f"Number of distinct weeks: {df_clean['week'].nunique()}")
print(f"Number of distinct regions: {df_clean['region'].nunique()}")

