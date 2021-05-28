from fastapi import FastAPI, File, UploadFile
import os, time
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from models import Files
from pydantic import BaseModel 
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = f'{dir_path}/files/{file.filename}'
    f = open(f'{filename}', 'wb')
    content = await file.read()
    f.write(content)
    fileResponseDB = await Files.create(file=f'127.0.0.1:8000/files/{file.filename}')
    return { 'url': fileResponseDB }

register_tortoise(
    app,
    db_url="postgres://postgres:postgres@localhost:5432/sv-arquivos",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
