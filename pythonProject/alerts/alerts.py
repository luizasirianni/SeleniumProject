
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/alerts/alerts_example.html'
driver.get(url)
#
# # First example - JS alert
# alert1 = driver.find_element('css selector', 'div#jsAlertExample button')
# alert1.click()
# time.sleep(2)
# my_alert = driver.switch_to.alert #becomes an object
# assert my_alert.text =='I am a JavaScript Alert', "Unexpected text on alert"
# my_alert.accept() #click to 'accept' and returns to the original page. dismiss() can also be used


# Second example - Confirm alert
# my_js_confirm = driver.find_element('css selector', 'div#jsConfirmExample button')
# my_js_confirm.click()
# time.sleep(2)
#
# my_confirm = driver.switch_to.alert
# my_confirm.accept() #clicks ok button and closes the alert
# #my_confirm.dismiss() #clicks cancel button and closes the alert
# rs_message = driver.find_element('id', 'userResponse1').text
#
# assert rs_message == 'Great! You will love it!', "Wrong message after accepting "

#Third example - prompt alert

prompt = driver.find_element('css selector', '#jsPromptExample > button')
prompt.click()

prompt_type = driver.switch_to.alert
message = 'teste teste teste'
prompt_type.send_keys(message)
prompt_type.accept()

p_message = driver.find_element('id', 'userResponse2').text
time.sleep(2)
assert p_message == 'You have entered: {}'.format(message), 'Wrong message'
import pdb; pdb.set_trace()