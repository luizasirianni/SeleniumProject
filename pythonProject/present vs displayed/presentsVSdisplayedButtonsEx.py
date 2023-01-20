from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/presentsVSdisplayedButtonsExample.html')

my_btn1 = driver.find_element('id', 'btn1')
btn1_txt = my_btn1.text
print('First button text: {}'.format(btn1_txt))

my_btn4 = driver.find_element('id', 'btn4')
btn4_txt = my_btn4.text
print('4th button text: {}'.format(btn4_txt))
    #Not printing anything because it is not displayed. Hidden element


if my_btn4.is_displayed():
    my_btn4.click()
else:
    raise Exception("Button 4 is not displayed")
import pdb; pdb.set_trace()