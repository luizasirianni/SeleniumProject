import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pdb

serv = Service(r"C:\Users\luiza\Downloads\chromedriver_win32\chromedriver.exe")

driverC = webdriver.Chrome(service=serv)

driverC.get("http://demostore.supersqa.com/")

cart = driverC.find_element(By.ID, 'site-header-cart')
cart.click()
time.sleep(5)

driverC.get("http://demostore.supersqa.com/my-account/")
u_name = driverC.find_element(By.ID, 'username')
u_name.send_keys("lusirianni") #types inside the field
u_name.clear() #clears inside the field

pdb.set_trace()
# to find the available methods just type dir(variableName)
# Ex: dir(driverC)