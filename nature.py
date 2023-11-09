import requests
from bs4 import BeautifulSoup
from typing import List, Optional

SUBJECTS = ["physical-sciences", "earth-and-environmental-sciences", "biological-sciences", "health-sciences",
            "scientific-community-and-society"]


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



if __name__ == "__main__":
    url = f"https://www.nature.com/subjects/physical-sciences/nature?searchType=journalSearch&sort=PubDate&page=1"
    content = get_page_content(url)
    max_page = get_max_page(content)
    print(max_page)