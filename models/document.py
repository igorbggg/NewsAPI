from typing import Any, Optional

from beanie import Document as Doc
from pydantic import BaseModel


class DsInsight(BaseModel):
    insight: Optional[str]
    insight_proba: Optional[float]
    insight_location: Optional[str]


class Document(Doc):
    guidislink: Any
    id: Any
    link: Any
    links: Any
    published: Any
    published_parsed: Any
    summary: Any
    summary_detail: Any
    tags: Any
    title: Any
    title_detail: Any
    ds_summary: Any
    repost_cnt: Any
    trend: Any
    ds_insight: DsInsight
    ap_uid: Any

    class Collection:
        name = "rssFeeds"

