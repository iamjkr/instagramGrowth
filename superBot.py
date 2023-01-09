from instapy import InstaPy
from config import password
from selenium import webdriver
diver = webdriver.Chrome()


session = InstaPy(username="sid_roy7x", password=password,headless_browser=True)
session.login()
session.like_by_tags(["iphone", "mercedes"], amount=5)