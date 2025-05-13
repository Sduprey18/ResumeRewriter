import requests 


def makeResumeReq(resText):
    url = "http://localhost:8000/provideResume"

    #with open("tests/temp.tex", "r") as file:
            #aiResume = file.read()

    #with open("backend/partialTemplate.tex", "r") as file:
        #resumeText = file.read()
    
    with open("tests/temp.tex", "rb") as f:
        response = requests.post(
            url,
            files={"file": ("tests/temp.tex", f, "text/x-tex")}
        )
    #response = requests.post(url, data= aiResume)

    with open("out.pdf", "wb") as f:
        f.write(response.content)

    print(response)

makeResumeReq(" ")
#print(response.text)
