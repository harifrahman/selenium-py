import requests
import json

# Define the API endpoint URL
# url = 'https://pokeapi.co/api/v2/pokemon/charizard'
url = 'https://pokeapi.co/api/v2/pokemon/1/encounters'

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Save the JSON response to a new file
    with open('response_result_area.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    print("Data saved to response_result.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")