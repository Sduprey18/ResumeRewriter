from fastapi import FastAPI, File, HTTPException, UploadFile, Body
from fastapi.responses import StreamingResponse
from pdf2image import convert_from_bytes
from pytesseract import image_to_string
from io import BytesIO
from PIL import Image
import subprocess
from pdflatex import PDFLaTeX
from pathlib import Path


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

@app.post("/provideResume")
async def provideResume(file: UploadFile = File(..., description="LaTeX file")): 

    latex_content = (await file.read()).decode("utf-8")

    pdfBytes = createResume(latex_content)
    
    return StreamingResponse(
        BytesIO(pdfBytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=firstTest.pdf"}
    )

    #return("hey")


def image_to_text(imageObjects):
    #lets get OCR now. 
    arr = []
    for image in imageObjects:
        arr.append(image_to_string(image))

    return arr

#add deepseek latex to template 
def createResume(aiResume):
    #base_dir = Path(__file__).resolve().parent
    #template_path = base_dir / "beginnerTemplate.tex"
    #tex_path = base_dir / "generatedResume.tex"

    with open("backend/beginnerTemplate.tex", "r") as file:
        starterCode = file.read()
    
    #with open("tests/temp.tex", "r") as file:
        #aiResume = file.read()
    
    starterCode += aiResume

    with open("generatedResume.tex", "w") as file:
        file.write(starterCode)

    pdfl = PDFLaTeX.from_texfile("generatedResume.tex")
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)
    return pdf

'''
def main():
    with open("tests/temp.tex", "r") as file:
            aiResume = file.read()
    createResume(aiResume)
    pass

main()
'''
