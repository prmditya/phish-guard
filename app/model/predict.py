import pandas as pd
import json
from joblib import load
from app.utils.features_extraction import extract_features

model = load('app/model/url_classification_rf.joblib')

def predict(url):
  features = extract_features(url['url'])

  features_df = pd.DataFrame([features])  # Wrap in a list to ensure it's a row
  flat_data = {key: value[0] if isinstance(value, list) else value for key, value in features.items()}
  print(json.dumps(flat_data, indent=2))

  # Ensure column names match the model's expected features (if trained with names)
  # Convert the DataFrame to a numpy array to drop feature names if needed
  prediction = model.predict(features_df.values)[0]  # sklearn handles DataFrame if names match
  print(f'Prediction: {prediction}')

  result = 'Phishing' if prediction == 1 else 'Safe'
  return result
