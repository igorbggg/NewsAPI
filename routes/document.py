from fastapi import APIRouter, Response

from models.document import Document
from beanie.odm.operators.find.comparison import NotIn, GT
from beanie.odm.operators.find.logical import And
router = APIRouter()


@router.get("/documents")
async def get_documents(response: Response, trend: str = None, insight: bool = None, limit: int = 100):
    response.headers['Access-Control-Allow-Origin'] = '*'

    if trend:
        return await Document.find_many(Document.trend == trend, limit=limit).to_list()

    if insight:
        insights = await Document.find_many(
            And(NotIn(Document.ds_insight.insight, [None, ''])), limit=limit).to_list()
        sorted_by_proba = sorted(insights, key=lambda x: x.ds_insight.insight_proba, reverse=True)
        return sorted_by_proba

    return await Document.find_many(limit=limit).to_list()
