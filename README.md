# AutoJudge: AI-Powered Coding Problem Difficulty Estimator

## 📌 Project Overview
AutoJudge is an intelligent difficulty estimation tool for coding problems (like those on Codeforces or LeetCode). It uses Natural Language Processing (NLP) and Machine Learning to analyze the text of a problem statement and predict:
1. **Difficulty Status:** A classification label (e.g., "Easy", "Hard").
2. **Complexity Score:** A regression score (0-100) indicating the granular difficulty.

This project includes a fully functional **Flask REST API** that serves the models to a frontend or client.

## 📂 Dataset
* **Source:** Codeforces Problem Set
* **Data File:** `codeforces_data.csv`
* **Features:** Problem Statement (Text), Tags, Difficulty Rating.
* **Size:** ~1000+ problem statements processed for training.

## 🧠 Approach & Models

### 1. Data Preprocessing
* Text cleaning (removing HTML tags, special characters).
* Tokenization and Vectorization using **CountVectorizer** and **TF-IDF**.

### 2. Classification Model (Easy vs. Hard)
* **Algorithm:** Multinomial Naive Bayes.
* **Goal:** Classify problem text into categorical difficulty levels.
* **Metrics:** Achieved high precision in distinguishing basic math problems from complex algorithmic tasks.

### 3. Regression Model (Difficulty Score)
* **Algorithm:** Linear Regression (Hybrid Approach).
* **Goal:** Predict a continuous difficulty score (0-100) based on text length and vocabulary complexity.

## 🚀 Steps to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Keerti33/AutoJudge>
   cd AutoJudge