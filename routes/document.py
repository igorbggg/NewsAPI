from fastapi import APIRouter

from models.document import Document

router = APIRouter()


@router.get("/documents")
async def get_documents(trend: str = None, insight: bool = None, limit: int = 50):
    if trend:
        return await Document.find_many(Document.trend == trend, limit=limit).to_list()

    if insight:
        return await Document.find_many(Document.insight == True, limit=limit).to_list()

    return await Document.find_many(limit=limit).to_list()
