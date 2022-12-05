from tech_news.database import search_news, find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = search_news({
        "$query": {},
        "$orderby": {"comments_count": -1, "title": 1}
    })

    return [(new["title"], new["url"]) for new in news[:5]]


# Requisito 11
def top_5_categories():
    all_news = find_news()
    count = Counter([new["category"] for new in all_news])
    categories = sorted(
        count.items(), key=lambda x: (-x[1], x[0])
    )

    return [category[0] for category in categories[:5]]
