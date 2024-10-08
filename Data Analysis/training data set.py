import pandas as pd
data_path = 'Data/Raw/soccer18-19.csv'
df = pd.read_csv(data_path);


# Ligin ilk 370 maçı eğitim, son 10 maçı test seti olacak
train_df = df.iloc[:370]  # İlk 370 maç eğitim seti
test_df = df.iloc[370:]   # Son 10 maç test seti

train_data_path = 'Data/Processed/train_set.csv'
test_data_path = 'Data/Processed/test_set.csv'

train_df.to_csv(train_data_path, index=False)
test_df.to_csv(test_data_path, index=False)

print("Egitim ve test setleri basariyla ayrildi ve kaydedildi.")