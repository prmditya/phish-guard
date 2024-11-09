import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
from app.utils import extract_features

# 1. Memuat Dataset
data = pd.read_csv('./dataset/dataset_phising.csv')

# 2. Ekstraksi Fitur
# Asumsikan dataset memiliki kolom 'url' dan 'label'
data['features'] = data['url'].apply(extract_features)

# Membagi fitur menjadi beberapa kolom
features_df = pd.json_normalize(data['features'])
X = features_df
y = data['label']

# 3. Membagi Data menjadi Train dan Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Melatih Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluasi Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Akurasi: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# 6. Menyimpan Model
with open('./app/model/phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model berhasil disimpan di './app/model/phishing_model.pkl'")