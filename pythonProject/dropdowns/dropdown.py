from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/dropdowns/dropdownsExample.html')
'''Option 1 - using Select class'''
# drpdwn = driver.find_element('id', 'age-range-select')
# drpdwn_obj = Select(drpdwn)
# drpdwn_obj.select_by_index(3)
# time.sleep(3)
# drpdwn_obj.select_by_value('61-80')

'''Option 2 - finding the element without the select class'''
time.sleep(3)
button = driver.find_element('id', 'dropdownMenuButton')
button.click()
time.sleep(3)
option = driver.find_element('xpath', '//*[@id="dropdowns"]/div[2]/div/ul/li[1]/a')
option.click()

import pdb; pdb.set_trace()
# (Pdb) drpdwn_obj = Select(drpdwn)
# (Pdb) dir(drpdwn_obj)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_el', '_escape_string', '_get_longest_token', '_set_selected', '_unset_selected', 'all_selected_options', 'deselect_all', 'deselect_by_index', 'deselect_by_value', 'deselect_by_visible_text', 'first_selected_option', 'is_multiple', 'options', 'select_by_index', 'select_by_value', 'select_by_visible_text']
# (Pdb) drpdwn_obj.all_selected_options
# [<selenium.webdriver.remote.webelement.WebElement (session="3665b342edccd308145ffb1bdc29651d", element="e8464917-f53a-407a-8a4a-a92ba5ae2a74")>]
# (Pdb) drpdwn_obj.all_selected_options[0].text
# '--Please choose an option--'
# (Pdb) drpdwn_obj.select_by_index(2)
# (Pdb) len(drpdwn_obj.options)
# 5
# (Pdb) drpdwn_obj.select_by_index(4)
# (Pdb) for option in drpdwn_obj.options: print(option.text)
# --Please choose an option--
# 81+
# 61-80
# 41-60
# 21-40
# (Pdb)