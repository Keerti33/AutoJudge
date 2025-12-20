from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- NEW IMPORT
from pydantic import BaseModel
import joblib

app = FastAPI()

# --- NEW SECTION: ALLOW FRONTEND CONNECTION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------------------------

# Load the Brain
model = joblib.load("rating_predictor_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

class ProblemInput(BaseModel):
    text: str

@app.post("/predict")
def predict_difficulty(input_data: ProblemInput):
    # Same logic as before
    user_text = [input_data.text]
    text_vectorized = vectorizer.transform(user_text)
    prediction = model.predict(text_vectorized)
    return {"predicted_rating": int(prediction[0])}