import aiofiles
from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_pic

router = APIRouter(
    prefix='/images',
    tags=['Uploading an image']
)


@router.post("/hotels")
async def add_hotel_img(
    name: int,
    file: UploadFile
):
    img_path = f"app/static/images/{name}.webp"
    async with aiofiles.open(img_path, 'wb+') as file_object:
        file_content = await file.read()
        await file_object.write(file_content) # Save in local storage
    
    process_pic.delay(img_path) # Celery task
