from flask import Flask, request, jsonify
import joblib  # or your preferred model loading library
import os

app = Flask(__name__)

# Load your model
model_path = r'/kaggle/working/path_to_save_directory'  # Adjust to your model path
model = joblib.load(model_path)  # or load your model using the appropriate method

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Preprocess the data if necessary
    features = [data['feature1'], data['feature2'], ...]  # Update based on your input features
    prediction = model.predict([features])
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
