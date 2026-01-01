import { useState } from 'react'
import './App.css'

function App() {
 
  const [problemText, setProblemText] = useState("");


  const [prediction, setPrediction] = useState(null);


  const handlePredict = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: problemText }),
      });

      const data = await response.json();
      setPrediction(data.predicted_rating);
    } catch (error) {
      console.error("Error connecting to server:", error);
      alert("Failed to connect to the AI. Is the backend running?");
    }
  };

  return (
    <div className="container">
      <h1>AutoJudge AI 🤖</h1>
      <p>Paste your problem Name & Tags below:</p>

      {/* The Input Box */}
      <textarea 
        placeholder="Example: watermelon math brute_force"
        value={problemText}
        onChange={(e) => setProblemText(e.target.value)}
      />

      {/* The Button */}
      <button onClick={handlePredict}>
        Predict Difficulty
      </button>

      {/* The Result Area (Only shows if we have a prediction) */}
      {prediction && (
        <div className="result">
          <h2>Predicted Rating: {prediction}</h2>
        </div>
      )}
    </div>
  )
}

export default App