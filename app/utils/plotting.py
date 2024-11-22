import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, title="Test"):
  plt.title(f"Confusion Matrix for {title}")
  sns.heatmap(cm, annot=True, fmt='d', cmap='crest', xticklabels=['Not Phising', 'Phising'], yticklabels=['Not Phising', 'Phising'])
  plt.xlabel('Predicted Labels')
  plt.ylabel('True Labels')
  plt.yticks(rotation=0)
  plt.show()