from selenium import webdriver
# Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver import Keys
# Библиотека с поиском элементов на сайте
from selenium.webdriver.common.by import By
import time
import random

# Если работаем в Chrome
browser = webdriver.Chrome()
# Сразу заходим на страницу солнечной системы
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

paragraphs = browser.find_elements(By.TAG_NAME, "p")
# Для перебора пишем цикл
for paragraph in paragraphs:
    print(paragraph.text)
    input()