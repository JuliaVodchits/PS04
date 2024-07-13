from email import header

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

action_dict = {"1": "Листать параграфы текущей статьи",
               "2": "Перейти на одну из связанных страниц",
               "3": "Выйти из программы"}


def find_in_wiki():
    query = input("Введите запрос к Википедии: ")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def get_action():
    global action_dict
    while True:
        print("Выберите действие:")
        for key, value in action_dict.items():
            print(f"{key}: {value}")
        choosed_action = input()
        if choosed_action not in action_dict.keys():
            print(f"Неверное значение: {choosed_action}")
        else:
            break
    return choosed_action

def scroll_paragraphs():
# <h1 id="firstHeading" class="firstHeading mw-first-heading">Результаты поиска</h1>
    header = browser.find_element(By.ID, "firstHeading").text
    print(header)
    if header == "Результаты поиска":
# <div class="searchResultImage-text"><div class="mw-search-result-heading"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце" data-serp-pos="0"
# data-prefixedtext="Солнце"><span class="searchmatch">Солнце</span></a>    </div><div class="searchresult"><span class="searchmatch">Со́лнце</span> (астр. ☉)&nbsp;—
# одна из звёзд нашей Галактики (Млечный Путь) и единственная звезда Солнечной системы. Вокруг <span class="searchmatch">Солнца</span> обращаются другие объекты этой...</div>
# <div class="mw-search-result-data">214 КБ (13&nbsp;050 слов) - 20:25, 22 июня 2024</div><button type="button" class="quickView-aria-button"
# aria-label="Открыть предпросмотр этой статьи."></button></div>
        paragraphs = browser.find_elements(By.CLASS_NAME , "searchResultImage-text")
        for paragraph in paragraphs:
            text = paragraph.find_element(By.CLASS_NAME, "searchresult").text.strip()
            link = paragraph.find_element(By.CLASS_NAME, "mw-search-result-heading").find_element(By.TAG_NAME, "a").get_attribute("href")
            print(text)
            print(link)
            next_input = input()
            if next_input == 'n':
                return
    else:
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph)
            next_input = input()
            if next_input == 'n':
                return

def get_random_link():
    links = []
    header = browser.find_element(By.ID, "firstHeading").text
    print(header, "->")
    if header == "Результаты поиска":
        elements = browser.find_elements(By.CLASS_NAME, "searchResultImage-text")
        for element in elements:
            current_link = element.find_element(By.CLASS_NAME, "mw-search-result-heading").find_element(By.TAG_NAME, "a").get_attribute("href")
            links.append(current_link)
    else:
        elements = browser.find_elements(By.TAG_NAME, "a")
        for element in elements:
            current_link = element.get_attribute("href")
            cl = element.get_attribute("class")
            if  cl!= "new" and cl != "external text":
                links.append(current_link)
    link = random.choice(links)
    print(link)
    browser.get(link)


if __name__ == "__main__":
    browser = webdriver.Chrome()

    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    assert "Википедия" in browser.title

    find_in_wiki()

    while True:
        choosed_action = get_action()
        match choosed_action:
            case '1':
                scroll_paragraphs()
            case '2':
                get_random_link()
            case '3':
                browser.quit()
                break


    time.sleep(200)
