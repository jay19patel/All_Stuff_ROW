from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)
element = driver.find_element(By.NAME,"q")
element.send_keys("Learn Python")
element.submit()
geturls =  driver.find_elements(By.TAG_NAME,'a')
geth3 =  driver.find_elements(By.TAG_NAME,'h3')
n=1

h3=[]
for i in geth3:
    h3.append(i.text)

for links in geturls:
    if len(links.text) >5 and links.text != "Videos":
        print(f" link {n} : {links.text}")
        print(links.get_attribute('href'))
        print("__________________________")
        n=n+1
print("all Done :)")
sleep(5)

