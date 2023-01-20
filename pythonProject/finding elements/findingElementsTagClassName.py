from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/')


# example finding by class name

product = driver.find_element(By.CLASS_NAME, 'product')
print(product)

# example finding by name

ob = driver.find_element(By.NAME, 'orderby')
print(ob.text)

# example finding by tag

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"found number of 'a' tag: {len(all_links)}")
all_lists = driver.find_elements(By.TAG_NAME, 'li')
print(f'found a total of {len(all_lists)} of "li" tags ')