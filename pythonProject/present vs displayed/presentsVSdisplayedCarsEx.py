from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/presentsVSdisplayedCarsExample.html')

# first option

# bmw = driver.find_element(By.CSS_SELECTOR, '#bmw')
# bmw.click()
#
# series_6 = driver.find_element(By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')
# series_6.click()

# second option

# series_6 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))

# third option

driver.find_element(By.CSS_SELECTOR, '#bmw').click()
series_6 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))