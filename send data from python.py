import requests
import json

# Define the URL provided by the Power Automate trigger
url = "https://prod-04.westeurope.logic.azure.com/workflows/9ebec4b01be741be8a81dc666a776a2e/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=6nrygY6EDhBA9sVq6_fSRypCqqhJL5yXIBErpwNuiNc"

# Define the data to be sent in the request
data = {
    "name": "From python",
    "age": 30,
    "email": "cimar@outlook.com"
}

# Convert the data to JSON
payload = json.dumps(data)

print(data)
# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the HTTP POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response status code
if response.status_code == 202:
    print("Data sent successfully!")
else:
    print("An error occurred while sending data.")
