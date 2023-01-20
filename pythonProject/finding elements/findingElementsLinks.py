from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/')

# must be an <a> tag or it will fail

cart = driver.find_element(By.LINK_TEXT, 'Cart')
print(cart.text)

account_element = driver.find_element(By.LINK_TEXT, 'My account')
print(account_element.text)

partial_acct_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print(partial_acct_element.text)

footer = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefront')
print(footer.text)
