from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.find_element_by_name("q").send_keys("pycon" + Keys.RETURN)
driver.find_element_by_css_selector(".blog-item-title a").click()
driver.switch_to.window(driver.window_handles[-1])
