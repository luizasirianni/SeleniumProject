import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pdb

driverM = webdriver.Firefox()

driverM.get("http://demostore.supersqa.com/")

#cart = driverM.find_element(By.CSS_SELECTOR, "#site-header-cart")
account = driverM.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a")

account.click()
time.sleep(3)
driverM.quit()

