import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FacebookAnalytics(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://192.168.2.12/lohit/")
		elemEmail = self.driver.find_element_by_id('email')
		elemEmail.send_keys('vinay@unboxsocial.com')
		elemPwd = self.driver.find_element_by_id('pwd')
		elemPwd.send_keys('123456' + Keys.RETURN)

	def test_overview(self):
		driver = self.driver

		driver.implicitly_wait(5) 
		driver.find_element_by_css_selector('.socialinsights_tab.influencerInsights_tab').click()

		search = driver.find_element_by_css_selector('.search_dataQuery')
		# slowly enter text for search
		text = 'shilpa'
		for character in text:
		    search.send_keys(character)
		    driver.implicitly_wait(0.3)
		
		driver.get('http://192.168.2.12/lohit/influencerInsights?id=0tmWAd-NpE1z0IMN14z5BL9AM5xJgmmwg5Te1JfLDdo&user_type=agency&platform=facebook&tab=facebook_overview&subtitle=Shilpa%20Shetty%20Kundra')
	
	# def tearDown(self):
	# 	self.driver.close()

if __name__ == "__main__":
    unittest.main()