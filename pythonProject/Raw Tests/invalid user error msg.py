from selenium import webdriver
import time

class InvalidUserLoginError:
    expected_msg = 'Unknown email address. Check again or try your username.'
    url = 'http://demostore.supersqa.com/my-account/'
    invalid_email = 'abc@hotmail.com'
    invalid_pass = '123asd'
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        time.sleep(3)

    def website(self):
        self.driver.get(self.url)
    def input_email(self):
        field = self.driver.find_element('id', 'username')
        field.send_keys(self.invalid_email)


    def input_password(self):
        field = self.driver.find_element('id', 'password')
        field.send_keys(self.invalid_pass)


    def click_login(self):
        field = self.driver.find_element('css selector', '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
        field.click()


    def error_message(self):
        error_element = self.driver.find_element('xpath', '//*[@id="content"]/div/div[1]/ul/li')
        displayed_error = error_element.text
        assert displayed_error == self.expected_msg, 'Login successful. No error was displayed'


    def main(self):
        self.website()
        self.input_email()
        self.input_password()
        time.sleep(2)
        self.click_login()
        self.error_message()
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()