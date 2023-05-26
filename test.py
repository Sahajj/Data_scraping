from selenium import webdriver
from selenium.webdriver.support.select import Select
Driver_path = 'D:\data scraping\chrome_deriver\chromedriver.exe'
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify dropdown with Select class
sel = Select(driver.find_element("x-path","//select[@name='continents']"))
#select by select_by_visible_text() method
sel.select_by_visible_text("Europe")
time.sleep(0.8)
#select by select_by_index() method
sel.select_by_index(0)
driver.close()