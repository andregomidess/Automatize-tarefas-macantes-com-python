from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('http://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
linkElem.click()