import pandas as pd

# Veriyi yükle
data_path = 'data/processed/train_with_form.csv'  # Son form durumu eklenmiş veri seti
df = pd.read_csv(data_path)

# Şut farkını hesapla
df['HomeShotDifference'] = df['HS'] - df['AS']  # Ev sahibi şut farkı (attığı şutlar - yediği şutlar)
df['AwayShotDifference'] = df['AS'] - df['HS']  # Deplasman şut farkı (attığı şutlar - yediği şutlar)

# Güncellenmiş veri setini kaydet
df.to_csv('data/processed/train_with_shot_difference.csv', index=False)

print("Sut farki basariyla hesaplandi ve veri setine eklendi.")
