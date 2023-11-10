import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict
from dataclasses import dataclass, asdict
import json


@dataclass
class Article:
    type: str
    title: str
    short_desc: str
    authors: List[str]
    url: str
    date: str
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


def write_to_json(data: Dict) -> None:
    """ This function should save and update data to a json file.
    It should also create the file if it does not exist.
    """
    with open("nature.json", "a", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write(",")
        file.write("\n")


def get_article_details(url: str) -> Optional[str]:
    content = get_page_content(url)
    res = None

    selectors = ["div.main-content", "div.c-article-body main-content"]
    for selector in selectors:
        article_content = content.find("div", class_=selector)
        if article_content:
            res = article_content.text.strip()
            break

    return res


def main():
    SUBJECTS = ["physical-sciences", "earth-and-environmental-sciences", "biological-sciences", "health-sciences",
                "scientific-community-and-society"]

    for subject in SUBJECTS:
        url = f"https://www.nature.com/subjects/{subject}/nature?searchType=journalSearch&sort=PubDate&page=1"
        max_page_content = get_page_content(url)
        max_page = get_max_page(max_page_content)
        for i in range(1, max_page + 1):
            url = f"https://www.nature.com/subjects/{subject}/nature?searchType=journalSearch&sort=PubDate&page={i}"
            content = get_page_content(url)
            all_articles = get_all_articles(content)
            for article in all_articles:
                article_data = get_article_data(article)
                if article_data:
                    write_to_json(asdict(article_data))


if __name__ == "__main__":
    main()
