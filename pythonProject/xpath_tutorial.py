
"""
// relative xpath -- most used
/ absolute xpath -- very easy to break

//tag[@attribute='value'] --> the attribute can be a class, an id, a html tag or any cand of attribute
//*[@attribute='value'] --> used when we want any tag that contains that attribute

cart example:
copy xpath:          //*[@id="site-header-cart"] or  //ul('[@id="site-header-cart"]')  --> most used
copy full xpath:    /html/body/div[2]/header/div[2]/div/ul --> very easy to break... things and tags are most likely to change and the path stops working

searching the console using contains:   $x('//ul[contains(@id, "site")]') --> this is searching for any id containing the word 'site'
searching for a tag that has no attributes,
    for example <a href="http://demostore.supersqa.com/my-account/lost-password/">Lost your password?</a>
        we're going to search like this  -->     $x('//a[text()="Lost your password"]')
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

### CHROME
serv = Service(r"C:\Users\luiza\Downloads\chromedriver_win32\chromedriver.exe")

driverC = webdriver.Chrome(service=serv)

driverC.get("http://demostore.supersqa.com/")
