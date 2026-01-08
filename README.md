# AutoJudge: AI-Powered Coding Problem Difficulty Estimator

## 📌 Project Overview
AutoJudge is an intelligent full-stack application designed to predict the difficulty of competitive programming problems. By analyzing the textual content of a problem statement (such as its title and tags), the system predicts a continuous difficulty rating (e.g., 800, 1500, 2100) and classifies the problem into difficulty tiers (**Easy**, **Medium**, **Hard**).

This project integrates a **Flask (Python)** backend for Machine Learning inference with a modern **React + Vite** frontend for a seamless user experience.

---

## 🎥 Demo Video
> https://drive.google.com/file/d/1RlYNK3uWOnZNKlXfipn_OgCAeMujomRM/view?usp=sharing > *(Please click the link above to watch the 2-minute demonstration of the project)*

---

## 📂 Dataset
The dataset was constructed dynamically using the **Codeforces API**.
* **Source:** `https://codeforces.com/api/problemset.problems`
* **Data Size:** ~1,000+ problem statements.
* **Features Used:**
  * `name`: The title of the problem.
  * `tags`: Contextual tags (e.g., "dp", "graphs", "greedy").
  * **Target:** `rating` (The official Codeforces difficulty rating).

---

## 🧠 Approach & Models

### 1. Data Preprocessing
* **Cleaning:** Removed special characters from tags and handled missing rating values.
* **Feature Engineering:** Combined `Problem Name` and `Tags` into a single text feature to capture both context and domain.
* **Vectorization:** Used **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text data into numerical vectors (`max_features=1000`).

### 2. Machine Learning Models
* **Regression Model:** A **Random Forest Regressor** (100 estimators) was trained to predict the specific difficulty score (0-3500).
* **Classification Logic:** Instead of a separate classifier, the difficulty status is derived from the predicted score to ensure consistency:
  * **Easy:** Score < 1350
  * **Medium:** 1350 ≤ Score < 1700
  * **Hard:** Score ≥ 1700

---

## 📊 Evaluation Metrics
The model was evaluated on a 20% held-out test set.
* **Metric:** Mean Absolute Error (MAE)
* **Performance:** The model achieved an MAE of approximately **192.5** (varies slightly per training run), meaning predictions are generally within a standard deviation of the actual Codeforces rating tiers.

---

## 🚀 Steps to Run Locally

### Prerequisites
* Python 3.x
* Node.js & npm

### Step 1: Clone the Repository
```bash
git clone [https://github.com/Keerti33/AutoJudge.git](https://github.com/Keerti33/AutoJudge.git)
cd AutoJudge

### Step 2: Setup the Backend (The Brain)

cd backend

pip install -r requirements.txt

python train_model.py

python main.py
The backend will start at http://127.0.0.1:5000

### Step 3: Setup the Frontend (The Interface)
Open a new terminal window:

Bash

cd frontend

npm install

npm run dev
The frontend will start at http://localhost:5173

💻 Web Interface Explanation
The user interface is built with React and styled with CSS.

Input Area: A text box where users enter the problem title and tags (e.g., "Shortest path in weighted graph").

Predict Button: Sends a POST request to the Flask API.

Result Display: Shows:

Difficulty Status: Color-coded (Green for Easy, Blue for Medium, Red for Hard).

Predicted Rating: The precise numerical score predicted by the Random Forest model.