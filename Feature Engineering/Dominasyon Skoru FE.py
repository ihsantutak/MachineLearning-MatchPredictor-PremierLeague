import pandas as pd

# Veriyi yükle
data_path = 'data/processed/train_with_form.csv'  # Son form durumu eklenmiş veri seti
df = pd.read_csv(data_path)

# Dominasyon Skoru hesaplama formülü
df['HomeDominance'] = (df['HS'] - df['AS']) + (df['HST'] - df['AST']) + (df['HC'] - df['AC']) \
                      - (df['HF'] - df['AF']) - (df['HY'] - df['AY']) - 5 * (df['HR'] - df['AR'])

# Güncellenmiş veri setini kaydet
df.to_csv('data/processed/train_with_dominance_score.csv', index=False)

print("Dominasyon Skoru basariyla hesaplandi ve veri setine eklendi.")
