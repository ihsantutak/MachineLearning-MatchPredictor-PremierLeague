from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Confusion matrix hesapla
cm = confusion_matrix(y_test_real, y_pred, labels=model.classes_)
cmd = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

# Confusion matrix'i görselleştir
cmd.plot(cmap='Blues')
plt.title('Random Forest Confusion Matrix')
plt.show()