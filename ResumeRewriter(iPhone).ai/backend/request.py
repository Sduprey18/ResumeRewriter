import requests 

url = "http://127.0.0.1:8000/something"
x = requests.get(url)

print(x.text)
