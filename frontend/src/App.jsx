import { useState } from 'react'
import './App.css'

function App() {
 
  const [problemText, setProblemText] = useState("");
  const [score, setScore] = useState(null);
  const [status, setStatus] = useState(null);

  const handlePredict = async () => {
    try {
   
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: problemText }),
      });

      const data = await response.json();
      
    
      setScore(data.difficulty_score);
      setStatus(data.difficulty_status);

    } catch (error) {
      console.error("Error connecting to server:", error);
      alert("Failed to connect to the AI. Is the backend running on Port 5000?");
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

      {/* The Result Area */}
      {score !== null && (
        <div className="result" style={{marginTop: '20px'}}>
          <h2>Difficulty: <span style={{color: '#61dafb'}}>{status}</span></h2>
          <h3>Predicted Rating: {score}</h3>
        </div>
      )}
    </div>
  )
}

export default App