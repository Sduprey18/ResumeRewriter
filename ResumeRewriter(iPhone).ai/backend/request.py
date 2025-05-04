import requests 

url = "http://127.0.0.1:8000/something"
uploadURL = "http://127.0.0.1:8000/uploadPDF"


_file = {
    'file': ('tests/OldResume.pdf', open('tests/OldResume.pdf', 'rb'), 'application/pdf')
}

with open("tests/temp.tex", "r") as file:
    aiTextThing = file.read()

try:
    response = requests.post(url, data= aiTextThing)
except Exception as e:
    print(f"You got a {e} error")


#print(response.text)
