import numpy as np
import matplotlib.pyplot as plt  # Matplotlib eklenmeli
import seaborn as sns  # Seaborn eklenmeli

# Gerçek ve tahmin edilen sonuçları karşılaştır
comparison['Correct'] = np.where(comparison['FTR'] == comparison['Predicted_FTR'], 'Correct', 'Incorrect')

# Doğru ve yanlış tahminlerin oranlarını görselleştir
plt.figure(figsize=(6, 4))
sns.countplot(x='Correct', data=comparison)
plt.title('Correct vs Incorrect Predictions')
plt.show()
