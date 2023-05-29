from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time 
import pandas as pd

service = Service(r"chrome_driver/chromedrvier.exe")
driver = webdriver.Chrome(service = service)
driver.get('https://www.indeed.com/career/salaries/technology?from=whatwhere&b=technology')

time.sleep(7)
Button_element = driver.find_element(By.XPATH,"//h2[normalize-space()='Software Engineer']").click()
time.sleep(5)
Position = Button_element.text

time.sleep(2)
element = driver.find_element(By.XPATH, "//div[@class='css-15psvrv eu4oa1w0']")

Pay = element.text

time.sleep(2)
data = {
    Position : Pay
}

df = ps.DataFrame(data)

file_path = 'data.csv'

df.to_csv(file_path, index=False
)
time.sleep(10)

