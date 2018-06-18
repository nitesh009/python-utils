# controlling the browser with the selenium module
# pip install selenium
# import selenium is little different

from selenium import webdriver
#browser = webdriver.Firefox()

browser = webdriver.Chrome()

browser.get('http://www.knitesh.com')

# single selection selection
elem = browser.find_element_by_css_selector('')

print(elem)

elem.click()

# multiple selection selection
elems = browser.find_elements_by_css_selector('p')
len(elems)


# type in elements

searchElem = browser.find_elements_by_css_selector('.search-field')
searchElem.send_keys('nitesh')
searchElem.submit()   # automatically it finds that form associated with that field

browser.back()


browser.forward()

browser.refresh()

browser.quit()

# to check entire content
elems = browser.find_element_by_css_selector('html')
elems.text