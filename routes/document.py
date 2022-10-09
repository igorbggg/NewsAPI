from fastapi import APIRouter, Response

from models.document import Document

router = APIRouter()


@router.get("/documents")
async def get_documents(response: Response, trend: str = None, insight: bool = None, limit: int = 50):
    response.headers['Access-Control-Allow-Origin'] = '*'

    if trend:
        return await Document.find_many(Document.trend == trend, limit=limit).to_list()

    if insight:
        return await Document.find_many(Document.insight == True, limit=limit).to_list()

    return await Document.find_many(limit=limit).to_list()
