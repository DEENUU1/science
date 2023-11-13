from dataclasses import dataclass
from typing import Optional
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from src.repository.data import data
from sqlalchemy.orm import Session


@dataclass
class Data:
    url: str
    title: str
    content: Optional[str] = None


MAX_ITEM = 45


def get_page_content(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    return soup


def get_article_content(url: str):
    driver = webdriver.Chrome()
    driver.get(url)
    content = driver.page_source
    return content


def parse_xml(data):
    urls = []
    url_objects = data.find_all("url")
    for url_obj in url_objects:
        url = url_obj.find("loc")

        if url:
            urls.append(url.text)
    return urls


def get_article_details(url: str) -> Data:
    data = get_article_content(url)
    soup = BeautifulSoup(data, "html.parser")

    title = soup.find("h1", class_="Article__Headline__Title")
    content = soup.find("section", class_="Article__Content")

    if title and content:
        return Data(url, title.text, content.text)


def run_ng(db: Session):
    for i in range(1, MAX_ITEM + 1):
        URL = f"https://www.nationalgeographic.com/sitemaps/items.{i}.xml"
        content = get_page_content(URL)
        urls = parse_xml(content)
        for url in urls:
            article_details = get_article_details(url)

            if article_details:
                if data.exists(db, article_details.url):
                    pass
                data.create_by_fields(
                    db,
                    title=article_details.title,
                    url=article_details.url,
                    content=article_details.content
                )
