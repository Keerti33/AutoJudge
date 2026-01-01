import os
import joblib

print("--- AutoJudge System Health Check ---")


required_files = [
    "main.py",
    "train_model.py",
    "rating_predictor_model.pkl",
    "tfidf_vectorizer.pkl",
    "requirements.txt"
]

all_good = True


for filename in required_files:
    if os.path.exists(filename):
        print(f"✅ Found: {filename}")
    else:
        print(f"❌ MISSING: {filename}")
        all_good = False

print("-" * 30)


if os.path.exists("rating_predictor_model.pkl"):
    try:
        model = joblib.load("rating_predictor_model.pkl")
        print(f"✅ Model Load Test: Success (Type: {type(model).__name__})")
    except Exception as e:
        print(f"❌ Model Load Test: FAILED ({e})")
        all_good = False


print("-" * 30)
if all_good:
    print("🚀 SYSTEM READY! You can run 'python main.py' now.")
else:
    print("⚠️ ISSUES FOUND. Please run 'python train_model.py' to fix missing models.")