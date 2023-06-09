import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#download geckodriver.exe and add to system path
# Firefox Webdriver documentation: https://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/firefox.html
# https://github.com/mozilla/geckodriver
# https://seleniumhq.github.io/selenium/docs/api/py/api.html#webdriver-firefox


driver = webdriver.Firefox()
driver.get("http://192.168.2.12/lohit/")
elemEmail = driver.find_element_by_id('email')
elemEmail.send_keys('vinay@website.com')
elemPwd = driver.find_element_by_id('pwd')
elemPwd.send_keys('123456' + Keys.RETURN)

driver.implicitly_wait(5) 
driver.find_element_by_css_selector('.socialinsights_tab.influencerInsights_tab').click()

driver.implicitly_wait(5)
search = driver.find_element_by_css_selector('.search_dataQuery')
# slowly enter text for search
text = 'shilpa'
for character in text:
    search.send_keys(character)
    driver.implicitly_wait(0.3)

driver.get('http://192.168.2.12/lohit/influencerInsights?id=0tmWAd-NpE1z0IMN14z5BL9AM5xJgmmwg5Te1JfLDdo&user_type=agency&platform=facebook&tab=facebook_overview&subtitle=Shilpa%20Shetty%20Kundra')

#driver.close()
