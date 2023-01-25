from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
def add_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item')
    )

def click_cart():
    driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()


def insert_coupon(coupon_code):
    coupon_field = wait.until(EC.visibility_of_element_located((By.ID, 'coupon_code')))
    coupon_field.send_keys(coupon_code)
    coupon_field.send_keys(Keys.ENTER)
    #driver.find_element(By.NAME, 'apply_coupon').click()

def select_shipping():
    driver.find_element(By.CSS_SELECTOR, '#shipping_method_0_local_pickup3').click()

def verify_total():
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[4]/td/strong/span/bdi'), '$0.00'))



if __name__ == '__main__':

    coupon_code = 'SSQA100'

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get('http://demostore.supersqa.com/')

    add_item_to_cart()
    click_cart()
    insert_coupon(coupon_code)
    time.sleep(3)
    select_shipping()
    verify_total()
    driver.quit()
