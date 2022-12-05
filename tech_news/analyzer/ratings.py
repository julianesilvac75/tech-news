from tech_news.database import search_news


# Requisito 10
def top_5_news():
    news = search_news({
        "$query": {},
        "$orderby": {"comments_count": -1, "title": 1}
    })

    return [(new["title"], new["url"]) for new in news[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
