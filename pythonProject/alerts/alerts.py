
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/alerts/alerts_example.html'

driver.get(url)

alert1 = driver.find_element('css selector', 'div#jsAlertExample button')
alert1.click()
time.sleep(2)

my_alert = driver.switch_to.alert #becomes an object
assert my_alert.text =='I am a JavaScript Alert', "Unexpected text on alert"
my_alert.accept() #click to 'accept' and returns to the original page. dismiss() can also be used

import pdb; pdb.set_trace()