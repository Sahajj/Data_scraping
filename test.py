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

Roles = ['Front End Developer', 'IT Support', 'Product Owner', 'It Security Specialist', 'Full Stack Developer']
Place = ['New-York--NY', 'Los-Angeles--CA', 'NJ', 'Detroit--MI', 'Chicago--IL', 'Houston--TX']

# Create an empty dataframe to store the data
data = pd.DataFrame(columns=['Role', 'Place', 'High Salary', 'Average Salary'])

for i in Roles:
    for j in Place:
        link = f'https://www.indeed.com/career/{i}/salaries/{j}'
        time.sleep(5)
        driver.get(link)
        time.sleep(7)
        High_element = driver.find_element(By.XPATH,"//div[@class='css-noncsw e37uo190']//div[2]")
        H = High_element.text
        hig = H.split()
        High = hig[1] 
        print(High)
        time.sleep(2)
        avg_element = driver.find_element(By.XPATH,"//div[@class='css-15b2pfd eu4oa1w0']")
        avg = avg_element.text
        Avg2 = avg.split()
        Avrage = Avg2[1] 
        print(Avrage)
        time.sleep(2)
        data.loc[len(data)] = [i, j, High, Avrage]
        data.to_csv('data.csv', index=False)
        time.sleep(7)
