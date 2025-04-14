from fastapi import FastAPI, File, HTTPException, UploadFile
from pdf2image import convert_from_bytes, convert_from_path
from pytesseract import image_to_string
from io import BytesIO
import base64
from PIL import Image

app = FastAPI()

#well use this file to put the finished pdf once its ready. now we need to create endpoint to take in s pdf file

@app.get("/")
def root():
    return{'message':"hello world"}

@app.get("/something")
def otherfunction():
    return("hi")

@app.post("/uploadPDF")
async def uploadPDF(file: UploadFile):
    
    if file.filename[-3:] !="pdf":
        return (file.filename[-3:])
    else:
        print('is pdf')
    
    contents = await file.read()
    try:
       #images = convert_from_bytes(contents, poppler_path="/opt/homebrew/bin")
       images = convert_from_bytes(contents)
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Failed to convert PDF to images, with error being {e}")

    first_page = images[0]
    width, height = first_page.size

    arr = image_to_text(images)
    return arr

def image_to_text(imageObjects):
    #lets get OCR now. 
    arr = []
    for image in imageObjects:
        arr.append(image_to_string(image))

    return arr
'''
@app.post("/uploadPDF")
async def uploadPDF(file: UploadFile):
    pdf_bytes = await file.read()
    imageHolder = []

    with BytesIO(pdf_bytes) as pdf:
        #images = convert_from_path(pdf)
        images = convert_from_bytes(pdf_bytes)
        for i, img in enumerate(images):
            img.save(f"page_{i + 1}.png", "PNG")
            imageHolder.append(img)
    
    returnDict = {}

    for i in range(len(imageHolder)):
        with open(f"page_{i+1}.png", "rb") as image_file:
           encoded_image_string = base64.b64encode(image_file.read()).decode("utf-8")
           returnDict[f'page{i+1}'] = encoded_image_string

    
    return returnDict
'''
