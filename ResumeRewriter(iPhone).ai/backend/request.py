import requests 


def makeResumeReq(resText):
    url = "http://localhost:8000/provideResume"

    with open("tests/temp.tex", "r") as file:
            aiResume = file.read()

    #with open("backend/partialTemplate.tex", "r") as file:
        #resumeText = file.read()
    response = requests.post(url, data= aiResume)

    print(response)

makeResumeReq(" ")
#print(response.text)
