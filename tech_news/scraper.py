import requests
import time
from parsel import Selector


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
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
