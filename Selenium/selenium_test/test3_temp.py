# https://www.timeanddate.com/weather/india/valsad

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




def mywatherapp(location):
    print(f"finding {location} weather ")
    driver=webdriver.Chrome()
    url = f"https://www.timeanddate.com/weather/india/{location}"
    print(url)
    driver.get(url)
    element = driver.find_element(By.CLASS_NAME,"h2")
    tem = element.text
    print(f"{location} : {tem} ")






def app():
    print(" welcome to my weather app ")
    location = input("enter Location here : ")
    mywatherapp(location)

app()