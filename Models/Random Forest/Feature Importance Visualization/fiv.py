import seaborn as sns

# Özellik önemlerini hesapla
feature_importances = model.feature_importances_
features = X_train.columns

# Özellik önemlerini görselleştir
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=features)
plt.title('Random Forest Feature Importance')
plt.xlabel('Ozellik Onemi')
plt.ylabel('Ozellikler')
plt.show()
