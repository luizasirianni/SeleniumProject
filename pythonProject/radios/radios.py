from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/radios/radios_example.html')

expected_default = '21-40'
locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

# #test case 1 - verify if the default value is selected

default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=expected_default))
assert default_element.is_selected(), f"The default value of {expected_default} is not selected"

#test case 2

expected_values = ['21-40', '41-60', '61-80', '81+', '1']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), \
    "the number of radios does not match the expected number of values. Expected: {}, Actual: {}".format(len(expected_values), len(all_radios))