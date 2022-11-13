from os.path import exists

from fastapi import FastAPI, File, UploadFile, HTTPException
from file_handler import get_synopsis

app = FastAPI()

DATA_DIR = "data/"

@app.post("/upload")
async def upload_file(file: UploadFile):
    if file.filename.endswith('.csv') or file.filename.endswith('.xlsx'):
        # TODO: need to validate is legitimate csv or xlsx 
        # - could try pandas.read_csv/excel and raise HTTP exceptions

        # this is going to write over a same name file
        file_location = f"{DATA_DIR}{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        return {"filename": file.filename}
    else:
        raise HTTPException(422, detail="Invalid file type")

@app.get("/{identifier}/synopsis")
def synopsis(identifier: str):
    path = f"{DATA_DIR}{identifier}"
    if exists(path):
        # Fastapi converts dictionary to json
        return get_synopsis(path)
    else:
        raise HTTPException(404, detail="File not found")
