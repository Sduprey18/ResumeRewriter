from fastapi import FastAPI

app = FastAPI()

#well use this file to put the finished pdf once its ready. now we need to create endpoint to take in s pdf file

@app.get("/")
def root():
    return{'message':"hello world"}

@app.get("/something")
def otherfunction():
    return("hi")

