from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://demostore.supersqa.com/my-account/')

# generate random email
import string
import random
letters = string.ascii_lowercase
random_str = ''.join(random.choice(letters) for i in range(15)) # generate 15 random characters
random_email = random_str + '@supersqa.com'

# register field
reg_email = driver.find_element(By.ID, 'reg_email')
reg_email.send_keys(random_email)

reg_password = driver.find_element(By.ID, 'reg_password')
reg_password.send_keys('12345')

reg_button = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button').click()
time.sleep(2)
try:
    logout_button = driver.find_element(By.CSS_SELECTOR, '#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a')
    print('logout button is displayed')
except:
    raise Exception('user not logged in after registered')
