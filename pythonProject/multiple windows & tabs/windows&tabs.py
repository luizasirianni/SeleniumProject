from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('file:///D:/python/aaaaaaaaaaaaaaaaa/pythonProject/multiple%20windows%20&%20tabs/windows-and_tabs_example.html')

driver.find_element(By.XPATH, '//*[@id="windows"]/a[1]').click()

# driver.find_element(By.XPATH, '/html/body/h1')

# original_window = driver.current_window_handle

all_windows = driver.window_handles
new_window = all_windows[1]

print(f"Title before switching focus: {driver.title}")
driver.switch_to.window(new_window) # switch focus to the new tab/window
print(f"Title after switching focus: {driver.title}")
driver.switch_to.window(all_windows[0]) # switch back the focus to the default tab/window
print(f"Title after switching back focus: {driver.title}")
import pdb; pdb.set_trace()