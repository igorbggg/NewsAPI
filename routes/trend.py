from fastapi import APIRouter

from models.document import Document

router = APIRouter()


@router.get("/trends")
async def get_trends(limit: int = 50):

    return await Document.find_all(Document.insight == True).limit(n=limit).to_list()

