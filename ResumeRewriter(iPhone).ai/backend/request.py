import requests 

url = "http://127.0.0.1:8000/something"
uploadURL = "http://127.0.0.1:8000/uploadPDF"
x = requests.get(url)

_file = {
    'file': ('backend/sherkeemDupreyCurrentResume.pdf', open('backend/sherkeemDupreyCurrentResume.pdf', 'rb'), 'application/pdf')
}

response = requests.post(uploadURL, files=_file)

print(response.text)
