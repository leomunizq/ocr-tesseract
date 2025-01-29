import uvicorn
from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image
import io

app = FastAPI()

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        
        custom_config = "--oem 1 --psm 1 -l ita"
         
        text = pytesseract.image_to_string(image, lang="ita", config=custom_config)
        return {"filename": file.filename, "extracted_text": text.strip()}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8500, reload=True)
