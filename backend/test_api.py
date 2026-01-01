import requests
import json

# 1. The URL of your API
url = "http://127.0.0.1:5000/predict"

# 2. Define test cases (Just text, no hours needed now)
test_cases = [
    {
        "text": "Calculate the eigen value of the matrix and find the integration limits." 
    },
    {
        "text": "Print the sum of two integers A and B." 
    },
    {
        "text": "Given a graph with N nodes, find the shortest path using Dijkstra's algorithm."
    }
]

print("--- AutoJudge API Tester ---")
print(f"Target URL: {url}\n")

# 3. Loop through test cases and send them
for i, data in enumerate(test_cases):
    print(f"Test Case #{i+1}: Sending data...")
    print(f"Input: {data['text']}")
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success! Server Response:")
            print(json.dumps(result, indent=2))
        else:
            print(f"❌ Error: {response.status_code}")
            # Print the error message from the server if available
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect. Is the server running?")
    
    print("-" * 30)