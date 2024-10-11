# Doğruluk skorunun farklı iterasyonlarda nasıl geliştiğini izlemek
accuracy_scores = []

for i in range(1, 100, 10):  # n_estimators ile oynayarak
    model = RandomForestClassifier(n_estimators=i, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy_scores.append(accuracy_score(y_test_real, y_pred))

# Doğruluğu zamana göre çiz
plt.figure(figsize=(10, 6))
plt.plot(range(1, 100, 10), accuracy_scores, marker='o')
plt.title('Accuracy Over Iterations')
plt.xlabel('n_estimators')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()
