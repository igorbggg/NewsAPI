from typing import Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Response
from beanie.odm.operators.find.comparison import NotIn, GTE
from beanie.odm.operators.find.logical import And

from models.document import Document


router = APIRouter()


@router.get("/documents")
async def get_documents(
        response: Response,
        trend: Optional[str] = None,
        insight: Optional[bool] = False,
        period: Optional[int] = 1,
        limit: Optional[int] = 100,
        offset: Optional[int] = 0
):
    """
    Получение документов из коллекции rssFeeds

    :param response:
    :param trend: тренд
    :param insight: флаг "инсайтовости" новости
    :param period: период в часах, за который необходимо получить документы
    :param limit: кол-во записей, которое необходимо получить
    :param offset: сдвиг по выборке
    :return:
    """
    response.headers['Access-Control-Allow-Origin'] = '*'

    documents = await Document.find_many(
        And(
            Document.trend == trend if trend else {},
            NotIn(Document.ds_insight.insight, [None, '']) if insight else {},
            GTE(Document.created_at, datetime.utcnow() - timedelta(hours=period))
        ),
        limit=limit,
        skip=offset
    ).sort("-created_at").to_list()

    return documents
