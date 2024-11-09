from flask import Blueprint, request, jsonify, render_template
import pickle
from .utils import extract_features
import numpy as np

main = Blueprint('main', __name__)

# Load model saat inisialisasi blueprint
with open('app/model/phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url', '')
    
    if not url:
        return jsonify({'result': 'Invalid URL'}), 400
    
    # Ekstraksi fitur
    features = extract_features(url)
    
    # Membuat array fitur
    feature_array = np.array([
        features['url_length'],
        features['num_hyphens'],
        features['num_underscores'],
        features['num_subdomains'],
        features['has_https'],
        features['has_ip'],
        features['num_question_marks'],
        features['num_amps'],
        features['suspicious_tld'],
        features['has_redirect']
    ]).reshape(1, -1)
    
    # Prediksi
    prediction = model.predict(feature_array)[0]
    
    result = 'Phishing' if prediction == 1 else 'Safe'
    
    return jsonify({'result': result})
