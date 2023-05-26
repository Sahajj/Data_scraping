from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time 

Driver_path = 'D:\data scraping\chrome_deriver\chromedriver.exe'
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/css/css_dropdowns.asp")
# identify dropdown with select class 
sel = Select(driver.find_element("x-path",'//*[@id="main"]/div[3]/div[2]/div/button'))
sel.select_by_visible_text("Dropdown Menu")
time.sleep(0.8)
# select ny select string method 
sel.select_by_index(1)
driver.close()