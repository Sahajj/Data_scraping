from selenium import webdriver

driver = webdriver.Chrome('/chrome_driver/chromedriver.exe')
driver.get("https://www.google.com/")
print(driver.title)