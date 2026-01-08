from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  
print("--- Loading Real AI Models... ---")


try:

    model = joblib.load('rating_predictor_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    print("✅ Success: Models loaded correctly.")
except FileNotFoundError:
    print("❌ Error: Model files not found!")
    print("   Run 'python train_model.py' first to generate them.")
    model = None
    vectorizer = None


@app.route('/')
def home():
    return "AutoJudge Real-AI Backend is Running!"

@app.route('/predict', methods=['POST'])
def predict():
 
    if not model or not vectorizer:
        return jsonify({"error": "Models not loaded. Run train_model.py first."}), 500

 
    data = request.get_json()
    user_text = data.get('text', '')

    text_vector = vectorizer.transform([user_text])


    predicted_rating = model.predict(text_vector)[0]


    
    if predicted_rating < 1350:  
        difficulty_status = "Easy"
    elif predicted_rating < 1700: 
        difficulty_status = "Medium"
    else:
        difficulty_status = "Hard"

 
    return jsonify({
        "status": "success",
        "input_text": user_text,
        "difficulty_score": int(predicted_rating), 
        "difficulty_status": difficulty_status      
    })

if __name__ == '__main__':
    app.run(debug=True)