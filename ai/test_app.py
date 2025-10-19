import requests

url = "http://127.0.0.1:5000/api/recommend"

data = {
    "name": "Sabrina",
    "age": 15,
    "answers": "Gosto muito de computação e programação"
}

response = requests.post(url, json=data)
print(response.json())