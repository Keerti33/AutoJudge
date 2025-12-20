import requests
import pandas as pd # We import pandas as 'pd' to save typing

url = "https://codeforces.com/api/problemset.problems"
print("Fetching data from Codeforces...")

response = requests.get(url)
data = response.json()

if data["status"] == "OK":
    problems = data["result"]["problems"]
    
    # 1. Convert the list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(problems)
    
    # 2. Keep only the columns we need for the AI
    # 'name' = input, 'tags' = input, 'rating' = what we want to predict
    df = df[['name', 'tags', 'rating']]
    
    # 3. Clean the data: Drop rows where 'rating' is missing (NaN)
    print(f"Total problems found: {len(df)}")
    df = df.dropna(subset=['rating'])
    print(f"Problems with valid ratings: {len(df)}")
    
    # 4. Save to CSV
    csv_filename = "codeforces_data.csv"
    df.to_csv(csv_filename, index=False)
    
    print(f"Success! Data saved to {csv_filename}")
    
    # Optional: Show the first few rows to confirm
    print(df.head())

else:
    print("Failed to fetch data.")