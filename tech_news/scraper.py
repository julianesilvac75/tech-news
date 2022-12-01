import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url: str):
    try:
        time.sleep(1)
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=3, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content: str):
    selector = Selector(html_content)
    urls = selector.css("h2.entry-title a::attr(href)").getall()

    return urls


# Requisito 3
def scrape_next_page_link(html_content: str):
    selector = Selector(html_content)
    next_page_link = selector.css("a.next.page-numbers::attr(href)").get()

    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content: str):
    selector = Selector(html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css("h1.entry-title::text").get().rstrip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = len(selector.css("ol.comment-list li").getall())
    summary = selector.xpath("string(//p)").get().rstrip()
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("a.category-style span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount: int):
    news = []
    next_page_url = "https://blog.betrybe.com/"

    while len(news) < amount:
        html_content = fetch(next_page_url)
        news_urls = scrape_novidades(html_content)

        for url in news_urls:
            if len(news) == amount:
                break
            else:
                html = fetch(url)
                news_info = scrape_noticia(html)
                news.append(news_info)

        next_page_url = scrape_next_page_link(html_content)

    create_news(news)

    return news
