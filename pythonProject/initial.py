from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

### CHROME
serv = Service(r"C:\Users\luiza\Downloads\chromedriver_win32\chromedriver.exe")

driverC = webdriver.Chrome(service=serv)

driverC.get("http://demostore.supersqa.com/")

### FIREFOX
driverM = webdriver.Firefox()

driverM.get("http://demostore.supersqa.com/")

### FINDING ELEMENTS using By class

from selenium.webdriver.common.by import By
# find_element(By.ID, "<id>")
# find_element(By.CSS_SELECTOR, "<css>")
# find_element(By.XPATH, "<xpath>")

### FINDING ELEMENTS without By

#find_element("id", "<id>)"
#find_element("css selector", "<css>)"
#find_element("xpath", "<xpath>)"