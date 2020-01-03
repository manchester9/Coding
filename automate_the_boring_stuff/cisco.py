# automate the boring stuff
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')
# browser.forward()
# browser.back()

elm = browser.find_element_by_tag_name('h1')
print(elm)
print(type(elm))
# print(elm.get_attribute('href'))

# elm = browser.find_element_by_css_selector(
# '.entry-content>ol:nth-child(15)>li:nth-child(1)>a:nth-child(1)')

# print(elm.text)
# print(elm.click())
# print(browser.quit())
