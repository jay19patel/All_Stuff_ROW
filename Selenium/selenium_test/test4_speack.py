



# ++++++++ Speack system +++++++++++++++++++++++




from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver_path = 'driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, options=options)


driver.maximize_window()
url ="https://ttsmp3.com/" 
driver.get(url)
btnselect = driver.find_element(By.ID,"sprachwahl")
btnselect.send_keys("British English / Brian")
sleep(2)
print("setup done... ")


def mywatherapp(text):
    strlen = len(text)
    print(f"your text: {text}")
    data =driver.find_element(By.ID,"voicetext")
    data.send_keys(text)
    driver.find_element(By.ID,"vorlesenbutton").click()
    sleep(3)






def app():
    print(" welcome to Speking test ")
    # text = input("enter text here : ")
    mywatherapp("hi jay")

app()




