import requests

API_URL = "http://127.0.0.1:8000/query"
query = {"query": "What is Dinakars Education, where he studied, whats his CGPA?"}

response = requests.post(API_URL, json=query)
print(response.json())