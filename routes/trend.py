from fastapi import APIRouter, Response

from models.document import Document

router = APIRouter()


@router.get("/trends")
async def get_trends(response: Response, limit: int = 50):
    response.headers['Access-Control-Allow-Origin'] = '*'

    return await Document.find_all(Document.insight == True).limit(n=limit).to_list()

