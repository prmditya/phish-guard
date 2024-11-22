import numpy as np
import pickle
from flask import request, jsonify
from app.utils.features_extraction import extract_features

with open('phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict(features):
  prediction = model.predict(features)[0]
  
  result = 'Phishing' if prediction == 1 else 'Safe'
  return result