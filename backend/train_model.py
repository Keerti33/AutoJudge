import pandas as pd
import joblib 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


print("Loading data...")
data = pd.read_csv("codeforces_data.csv")


data['tags'] = data['tags'].str.replace(r"[\[\]']", "", regex=True)
data['tags'] = data['tags'].str.replace(",", " ")
data['combined_text'] = data['name'] + " " + data['tags']

X_text = data['combined_text']
y = data['rating']


X_train_text, X_test_text, y_train, y_test = train_test_split(X_text, y, test_size=0.2, random_state=42)


print("Vectorizing text...")
vectorizer = TfidfVectorizer(max_features=1000)
X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

print("Training the Random Forest model... (This might take a minute)")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print(f"\nModel Training Complete!")
print(f"Mean Absolute Error: {mae:.2f}")
print("Interpretation: On average, the AI's guess is off by about this many points.")


joblib.dump(model, "rating_predictor_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("Files saved: 'rating_predictor_model.pkl' and 'tfidf_vectorizer.pkl'")