import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Veriyi yükle
df = pd.read_csv('data/processed/train_with_form.csv')

# Özellikler (features) ve hedef değişken (target)
features = ['HomePPG', 'AwayPPG', 'HomeFormPoints', 'AwayFormPoints', 'HomeFormGoals', 'AwayFormGoals']
target = 'FTR'

# İlk 360 maçı eğitim seti olarak kullanacağız
train_data = df.iloc[:360]

# Son 10 maçı test seti olarak kullanacağız (FTR tahmin edilecek)
test_data = df.iloc[360:]

# Eğitim setinde özellikler ve hedef değişkeni ayıralım
X_train = train_data[features]
y_train = train_data[target]

# Test setinde sadece özellikleri alıyoruz (FTR gizlenecek)
X_test = test_data[features]
y_test_real = test_data[target]  # Gerçek FTR sonuçlarını karşılaştırmak için tutalım

# Modeli oluştur
model = RandomForestClassifier(random_state=42)

# Modeli eğit
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

# Test setine tahmin edilen FTR'yi ekle
test_data['Predicted_FTR'] = y_pred

# Modelin doğruluğunu hesapla
accuracy = accuracy_score(y_test_real, y_pred)
print(f'Model Dogrulugu: {accuracy * 100:.2f}%')

# Tahmin edilen sonuçları ve gerçek sonuçları kaydet
test_data.to_csv('data/processed/test_data_with_predictions.csv', index=False)

# Tahmin edilen FTR ile gerçek FTR'yi karşılaştır
comparison = test_data[['HomeTeam', 'AwayTeam', 'FTR', 'Predicted_FTR']]
print(comparison)




