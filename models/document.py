from typing import Any

from beanie import Document as Doc


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
    insight: Any
    ap_uid: Any

    class Collection:
        name = "rssFeeds"

