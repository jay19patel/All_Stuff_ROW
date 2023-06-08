from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)
element = driver.find_element(By.NAME,"q")# find name="q" in google inspact function 
element.clear()#clear any past keys
element.send_keys("news ") # sen new keys
element.send_keys(Keys.RETURN)
news = driver.find_element(By.CLASS_NAME,"aUSklf")


print('''
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

''')
print(news.text)