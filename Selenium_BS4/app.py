from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



input = input("Enter Seatchabe item : ")
# find page using serch and get item page 
driver=webdriver.Chrome()
url = "https://www.flipkart.com/"
driver.get(url)
element = driver.find_element(By.CLASS_NAME,'_3704LK')
element.clear()
element.send_keys(input)
element.submit()
url = driver.current_url
print(url)
sleep(2)

file = open('Projects/data.csv','w')
file.write(f"your last searchs  : {input}")
file.close()

# scwaping data using bs4  
from bs4 import BeautifulSoup
import requests

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
sleep(2)

for product in soup.find_all('div',{'class':'_13oc-S'}):
    # print(product)
    # break
    title = product.find('div',{'class':'_4rR01T'}).text
    price = product.find('div',{'class':'_30jeq3'}).text
    data = product.find('ul',{'class':'_1xgFaf'}).text

    print("-------------*****------------")
    print(" Product Name :",title)
    print(" Price :",str(price))
    print("** Details **")
    print(data)
    




