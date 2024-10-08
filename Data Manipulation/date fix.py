import pandas as pd


data_path = 'data/processed/train_set.csv'
df = pd.read_csv(data_path)

# Tarih formatını datetime formatına dönüştür
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')


df = df.sort_values('Date')


df.to_csv('data/processed/train_with_datetime.csv', index=False)

