from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from boto3 import client

app = FastAPI()


@app.get("/list/")
async def root():
    s3 = client('s3')
    bucketName = 'hneves-api'
    response = s3.generate_presigned_post(
        Bucket=bucketName,
        Key='Screenshot 2025-01-06 at 17.55.51.png',
        Conditions=None,
        ExpiresIn=3600
    )
    return {"url": response['url'], 'fields': response['fields']}

@app.get("/download/{file_id}")
async def root():
    image_path = Path('images/foto de teste.jpg')

    if not image_path.is_file:
        return {'error':'Image not found on server'}
    return FileResponse(image_path)

@app.post("/upload/")
async def root():
    return {"message": "This is my post root"}

@app.delete("/delete/{file_id}")
async def root():
    return {"message": "This is my delete root"}