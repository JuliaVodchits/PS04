from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("screenshots/dom.png")
time.sleep(3)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("screenshots/selenium.png")
time.sleep(3)
browser.refresh()