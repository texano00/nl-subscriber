from devilConfig import *

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# iPhone
# Driver = webdriver.Remote(browser_name="iphone", command_executor='http://172.24.101.36:3001/hub')

# Firefox
driver = webdriver.Firefox()

# ------------------------------

mail = sys.argv[1]

for form in devilConfig:
	print "devil is processing form at -> " + form['url']

	driver.get(form['url'])

	try:
	    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, form['waitUntilThisElement'])))

	finally:
		if form['isInsideIframe']:
			frame = driver.find_element_by_css_selector(form['iframeElement'])			
			driver.switch_to.frame(frame)

		emailElement = driver.find_element_by_css_selector(form['emailElement'])
		emailElement.send_keys(mail)

		for checkbox in form['checkboxes']:
			driver.find_element_by_css_selector(checkbox).click()

		driver.find_element_by_css_selector(form['submitElement']).click()
		
		time.sleep(2)
		