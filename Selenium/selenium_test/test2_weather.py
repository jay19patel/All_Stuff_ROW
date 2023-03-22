# class="display-temp"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url = "https://www.accuweather.com/en/in/ahmedabad/202438/current-weather/202438"
driver.get(url)
element = driver.find_element(By.CLASS_NAME,"display-temp")
tem = element.text
print(tem)
print(driver.title)
