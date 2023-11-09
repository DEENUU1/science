import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

import time

SUBJECTS = ["physical-sciences", "earth-and-environmental-sciences", "biological-sciences", "health-sciences",
            "scientific-community-and-society"]


@dataclass
class Article:
    type: Optional[str]
    title: Optional[str]
    short_desc: Optional[str]
    authors: List[Optional[str]]
    url: Optional[str]
    date: Optional[str]
    is_free: bool = False


def get_page_content(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_max_page(soup) -> int:
    result = []

    pagination_items = soup.find_all("a", class_="c-pagination__link")

    for element in pagination_items:
        text = element.text.replace("page", "").replace("Next", "").replace("\n", "")
        try:
            result.append(int(text))
        except Exception as e:
            continue

    return max(result)


def get_all_articles(soup) -> Optional[List]:
    articles = None
    container = soup.find("ul", class_="ma0 mb-negative-2 clean-list")
    if container:
        articles = container.find_all("li")

    return articles


def get_article_data(article_obj) -> Optional[Article]:
    type = article_obj.find("span", {"data-test": "article.type"})
    is_free = article_obj.find("span", class_="text-orange")
    date = article_obj.find('time', {"itemprop": "datePublished"})
    title_url = article_obj.find("a", class_="text-gray")
    short_desc = article_obj.find("p")
    authors_container = article_obj.find("ul", {"data-test": "author-list"})
    authors = []
    if authors_container:
        author_objects = authors_container.find_all("li")
        for author in author_objects:
            authors.append(author.text)

    if not type or not date or not title_url or not short_desc or not authors:
        return None

    free = False
    if is_free:
        free = True

    return Article(
        type=type.text,
        title=title_url.text,
        short_desc=short_desc.text,
        authors=authors,
        url=f"https://www.nature.com{title_url['href']}",
        is_free=free,
        date=date["datetime"]
    )


if __name__ == "__main__":
    url = f"https://www.nature.com/subjects/physical-sciences/nature?searchType=journalSearch&sort=PubDate&page=1"
    content = get_page_content(url)
    # max_page = get_max_page(content)
    # print(max_page)

    all_articles = get_all_articles(content)
    for article in all_articles:
        article_data = get_article_data(article)
        if article_data:
            print(article_data)
            print("=======================")
