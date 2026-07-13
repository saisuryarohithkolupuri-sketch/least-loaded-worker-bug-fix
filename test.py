import requests

url = "http://127.0.0.1:5000/assign"

for i in range(8):

    response = requests.get(url)

    print(response.json())