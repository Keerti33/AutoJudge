import requests
import pandas as pd 

url = "https://codeforces.com/api/problemset.problems"
print("Fetching data from Codeforces...")

response = requests.get(url)
data = response.json()

if data["status"] == "OK":
    problems = data["result"]["problems"]
    

    df = pd.DataFrame(problems)
    

    df = df[['name', 'tags', 'rating']]
    

    print(f"Total problems found: {len(df)}")
    df = df.dropna(subset=['rating'])
    print(f"Problems with valid ratings: {len(df)}")
    

    csv_filename = "codeforces_data.csv"
    df.to_csv(csv_filename, index=False)
    
    print(f"Success! Data saved to {csv_filename}")
    
    print(df.head())

else:
    print("Failed to fetch data.")