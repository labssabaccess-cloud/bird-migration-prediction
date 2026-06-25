import os
import pandas as pd

df = pd.read_csv('FILE NAME', sep='\t', usecols=useful_columns, dtype=column_types)

needs = ['species', 'eventDate', 'decimalLatitude', 'decimalLongitude']

rename_ease{
  'eventDate': 'date'
  'decimalLatitude': 'lat'
  'decimalLongitude': 'long'
}

df_ease.rename(columns=rename_ease, inplace=True)

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year
df["week"] = df["date"].dt.isocalendar().week
df_clean = df_clean.round({'lat': 2, 'lon': 2})
