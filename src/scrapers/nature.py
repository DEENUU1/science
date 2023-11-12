import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from dataclasses import dataclass
from src.repository.type import types
from src.repository.data import data
from src.repository.author import author
from src.database import get_db
from sqlalchemy.orm import Session


@dataclass
class Article:
    type: str
    title: str
    short_desc: str
    authors: List[str]
    url: str
    date: str
    is_free: bool = False
    content: Optional[str] = None


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
    short_desc = None

    type = article_obj.find("span", {"data-test": "article.type"})
    is_free = article_obj.find("span", class_="text-orange")
    date = article_obj.find('time', {"itemprop": "datePublished"})
    title_url = article_obj.find("a", class_="text-gray")
    desc_container = article_obj.find("div", {"itemprop": "description"})
    if desc_container:
        short_desc = desc_container.find("p")
    authors_container = article_obj.find("ul", {"data-test": "author-list"})

    authors = []
    if authors_container:
        author_objects = authors_container.find_all("li")
        for author in author_objects:
            authors.append(author.text.replace("\xa0&", "").replace("\xa0", ""))

    if not type or not date or not title_url or not short_desc or not authors:
        return None

    free = False
    if is_free:
        free = True

    return Article(
        type=type.text,
        title=title_url.text.strip(),
        short_desc=short_desc.text.replace("\xa0", " "),
        authors=authors,
        url=f"https://www.nature.com{title_url['href']}",
        is_free=free,
        date=date["datetime"],
    )


def get_article_details(url: str):
    content = get_page_content(url)
    res = None

    selectors = ["main-content", "c-article-body main-content", "c-article-body"]
    for selector in selectors:
        article_content = content.find("div", class_=selector)
        if article_content:
            res = article_content.text.strip()
            break

    return res


def run_nature_scraper(db: Session):
    # SUBJECTS = ["physical-sciences", "earth-and-environmental-sciences", "biological-sciences", "health-sciences",
    #             "scientific-community-and-society"]
    SUBJECTS = ["physical-sciences"]
    for subject in SUBJECTS:
        url = f"https://www.nature.com/subjects/{subject}/nature?searchType=journalSearch&sort=PubDate&page=1"
        max_page_content = get_page_content(url)
        # max_page = get_max_page(max_page_content)
        max_page = 5
        for i in range(1, max_page + 1):
            url = f"https://www.nature.com/subjects/{subject}/nature?searchType=journalSearch&sort=PubDate&page={i}"
            content = get_page_content(url)
            all_articles = get_all_articles(content)
            for article in all_articles:
                article_data = get_article_data(article)
                if article_data:
                    if data.exists(db, article_data.url):
                        # This should skip to the next category and do not go to next page
                        pass

                    if not types.exists(db, article_data.type):
                        types.create_by_fields(db, article_data.type)
                    type_obj = types.get_by_name(db, article_data.type)

                    authors_objects = []
                    for a in article_data.authors:
                        if not author.exists(db, a):
                            author.create_by_fields(db, a)
                        authors_objects.append(author.get_by_full_name(db, a))

                    if article_data.is_free:
                        article_data.content = get_article_details(article_data.url)

                    data.create_by_fields(
                        db,
                        title=article_data.title,
                        url=article_data.url,
                        content=article_data.content,
                        short_desc=article_data.short_desc,
                        is_free=article_data.is_free,
                        published_date=article_data.date,
                        type=type_obj,
                        authors=authors_objects
                    )
