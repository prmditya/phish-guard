from flask import Blueprint, request, jsonify, render_template
from app.model.predict import predict

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict_url():
    prediction = predict(request.get_json()) 
    return jsonify({'result': prediction})
