from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/checkbox/checkboxEX.html')

'''example 1'''
# to_select_value = '61-80'
# value_locator = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
# my_choice = driver.find_element('css selector', value_locator)
# time.sleep(3)
# my_choice.click()
# time.sleep(3)
# assert my_choice.is_selected(), f"After clicking value {to_select_value} it's not selected"


'''example 2 - verify number of checkboxes and if they're selected'''

expected = 4
all_check = driver.find_elements('name', 'age-group-checkbox')
assert len(all_check) == expected, "Incorrect number of checkboxes"

for checkboxes in all_check:
    checkboxes.click()
    time.sleep(3)
    value = checkboxes.get_attribute('value')
    if checkboxes.is_selected():
        print(f"Checkbox with value {value} is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")