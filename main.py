
# Gerekli kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn tema ayarı
sns.set(style="whitegrid")


#
file_path = './Data/soccer18-19.csv'  
df = pd.read_csv(file_path)

#
print(df.head())

# Veri hakkında genel bilgi
print(df.info())

# Eksik değerler kontrolü
print(df.isnull().sum())

# Verinin özet istatistikleri
print(df.describe())

# Maç sonuçlarının dağılımı
sns.countplot(df['FTR'])
plt.title('Mac Sonuclarinin Dagilimi (Ev sahibi - Beraberlik - Deplasman)')
plt.show()

# 1. FTR (Full Time Result) ve HTR (Half Time Result) için sayısal dönüşüm
df['FTR'] = df['FTR'].map({'H': 1, 'D': 0, 'A': 2})  # H: Ev sahibi, D: Beraberlik, A: Deplasman
df['HTR'] = df['HTR'].map({'H': 1, 'D': 0, 'A': 2})  # H: Ev sahibi, D: Beraberlik, A: Deplasman

# 2. One-hot encoding uygulanacak kategorik değişkenler
# HomeTeam, AwayTeam ve Referee gibi kategorik değişkenleri one-hot encoding ile sayısal hale getirelim
df = pd.get_dummies(df, columns=['HomeTeam', 'AwayTeam', 'Referee'], drop_first=True)

# Kategorik değişken dönüşümü sonrası veri setinin yapısı
print(df.head())

# Ev sahibi avantajı özelliği
df['HomeAdvantage'] = df['FTHG'] - df['FTAG']  # Ev sahibi takımın attığı goller - deplasman takımının attığı goller

# Veri çerçevesindeki mevcut kolonlar
print(df.columns)

import pandas as pd

# Özellik mühendisliği işlemleri (one-hot encoding yapılmadan önce)

# Ev sahibi avantajı özelliği
df['HomeAdvantage'] = df['FTHG'] - df['FTAG']

# Veriyi tarihe göre sıralamak
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Takım formunu takip eden bir kolon
df['HomeTeamForm'] = 0
df['AwayTeamForm'] = 0

# Tarih sırasına göre veriyi ayıralım
df['Date'] = pd.to_datetime(df['Date'])  # Tarihleri datetime formatına dönüştürelim
df = df.sort_values('Date')  # Tarihe göre sıralayalım

# İlk 304 maç (%80) eğitim seti, son 76 maç (%20) test seti olacak şekilde veriyi ayıralım
train_size = int(len(df) * 0.8)  # Toplam veri sayısının %80'i eğitim seti olacak
df_train = df.iloc[:train_size]  # İlk 304 maç
df_test = df.iloc[train_size:]   # Son 76 maç

# Hedef değişken (FTR) ve özellikler (X) için ayırma işlemi
X_train = df_train.drop(['FTR', 'Date', 'Div'], axis=1)  # FTR hedef olduğu için çıkarıyoruz
y_train = df_train['FTR']  # Hedef değişken

X_test = df_test.drop(['FTR', 'Date', 'Div'], axis=1)
y_test = df_test['FTR']

# Eğitim ve test setlerinin boyutlarını kontrol edelim
print(f"Egitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")
