from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import PlainTextResponse
from helper_functions import image2, extract_text_from_docx, run_openai_task

app = FastAPI()

labels = [
    "Agreement Value",
    "Aggrement Start Date",
    "Aggrement End Date",
    "Renewal Notice (Days)",
    "Party One",
    "Party Two"
]


@app.post("/extract_components/")
async def extract_components(file: UploadFile):
    try:
        file_extension = file.filename.split(".")[-1]
        text = ""

        if file_extension in ["png", "jpg"]:
            text = image2(file.file)
        elif file_extension == "docx":
            text = extract_text_from_docx(file.file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")

        extracted_components = run_openai_task(labels=labels, text=text)
        return PlainTextResponse(content=extracted_components)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

