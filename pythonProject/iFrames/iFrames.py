import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/iFrames/iFrames_example.html')

'''Button outside an iFrame'''
# driver.find_element(By.ID, 'btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alerttxt = my_alert.text
# assert my_alerttxt == 'Just Clicked Outside iFrame', 'Text does not match the pop up alert'
# my_alert.dismiss()

'''Button inside an iFrame - example using WebElement'''
'''before clicking the button, we need to change focus:'''
# my_frame = driver.find_element(By.ID, 'myFrame1')
# driver.switch_to.frame(my_frame)
# driver.find_element(By.ID, 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

'''considering the situation where we switched the focus right above and we want to click a button outside iFrame'''
# driver.switch_to.default_content() # switching the focus to default content. Now we can click the button outside
# driver.find_element(By.ID, 'btnOutFrame').click()
# driver.switch_to.alert.dismiss()

'''Button inside an iFrame - using ID '''
# driver.switch_to.frame('myFrame1')
# driver.find_element(By.ID, 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# time.sleep(2)
# driver.switch_to.alert.dismiss()

'''Button inside an iFrame - using index '''

driver.switch_to.frame(0)#switch to the first frame. The html example has 2 iFrames
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.dismiss()