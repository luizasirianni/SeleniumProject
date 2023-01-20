from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/')

search_field = driver.find_element('id','woocommerce-product-search-field-0')
place_holder = search_field.get_attribute('placeholder')

if place_holder != "Search products…":
    raise Exception("Placeholder for search field is not as expected. Actual: {}".format(place_holder))
else:
    print("PLACE HOLDER OK")


# Example to verify which tab is selected
# first click on My Account
my_acct = driver.find_element('css selector', 'li.page-item-9')
my_acct.click()
#
 # find all the LI elements in the nav menu
nav_items = driver.find_elements('css selector', 'ul.nav-menu li')

for item in nav_items:
    item_class = item.get_attribute('class')
    if 'current_page_item' in item_class:
        print('The selected tab is {}'.format(item.text))

#Example to get a link url

prod_link = driver.find_element('css selector', 'li.product a')
prod_url = prod_link.get_attribute('href')
print('The url for product is {}'.format(prod_url))


import pdb; pdb.set_trace()