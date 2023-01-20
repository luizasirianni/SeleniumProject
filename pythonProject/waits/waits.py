from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# implicit wait
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/waitsExample.html")
image = driver.find_element(By.ID, 'the_slow_image')
image.click()
time.sleep(2)
print("found image")

# explicit wait --> most recommended
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/waitsExample.html")

imagem = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))
                      # waits 10 sec until the EXPECTED CONDITION be visible on the defined ID
time.sleep(5)
print("Found image")