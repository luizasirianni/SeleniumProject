import pytest
from selenium import webdriver
import os
@pytest.fixture(scope="class") #this fixture is going to run in every class
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff']
    # user is going to provide which browser will be used
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'Browser' must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported browsers: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver #setting a class variable
    yield
    driver.quit()