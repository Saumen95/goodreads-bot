from goodreads import client
from selenium import webdriver
from selenium.webdriver import chrome
import time


class Goodiebot:
    def __init__(self, username):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.goodreads.com/")
        time.sleep(2)

    gc = client.GoodreadsUser()
    user = gc.user(input(user.name))

    book = gc.book(input(book.title))




