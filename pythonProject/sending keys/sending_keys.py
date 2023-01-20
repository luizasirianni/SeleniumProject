
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/my-account/')

'''example of sending texts keys'''

username = driver.find_element('id', 'username')
username.send_keys('abcde')

password = driver.find_element('id', 'password')
password.send_keys('mypasscode')

submit = driver.find_element('css selector', '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
submit.click()

'''example using enter key '''
driver.get('http://demostore.supersqa.com/')

search = driver.find_element('id', 'woocommerce-product-search-field-0')
from selenium.webdriver.common.keys import Keys
search.send_keys('search example')
time.sleep(5)
search.send_keys(Keys.ENTER)


'''example using tabkey after typing the username'''

driver.get('http://demostore.supersqa.com/my-account/')

username = driver.find_element('id', 'username')
from selenium.webdriver.common.keys import Keys
username.send_keys('abcde')
time.sleep(3)
username.send_keys(Keys.TAB)

import pdb; pdb.set_trace()