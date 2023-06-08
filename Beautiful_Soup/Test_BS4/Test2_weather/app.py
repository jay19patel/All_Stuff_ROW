
import requests
from bs4 import BeautifulSoup

url ="https://weather.com/en-DM/weather/tenday/l/28d595bc7ffad1010c416552a79bd576c69a3443d730c27784a0911b2e078f98"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

location = soup.find('span',{'class':'LocationPageTitle--PresentationName--1AMA6'}).text
# print(location)

info = soup.find('p',{'class':'DailyContent--narrative--3Ti6_'}).text
# print(info)

temp = soup.find('span',{'class':'DailyContent--temp--1s3a7'}).text
# print(temp)

# data-testid="PercentageValue"
humidiy = soup.find('span',{'class':'DetailsTable--value--2YD0-'}).text
# print(humidiy)

# data-testid="MoonriseTime"
Moonrise = soup.find(attrs={'data-testid':'MoonriseTime'}).text
# print(Moonrise)


for wed in soup.find_all('details',{'class':'DaypartDetails--DayPartDetail--2XOOV Disclosure--themeList--1Dz21'}):
    day = wed.find('h3',{'class':'DetailsSummary--daypartName--kbngc'})
    temp = wed.find('span',{'class':'DetailsSummary--highTempValue--3PjlX'})
    print(f' Day : {day.text}  | Temps : {temp.text}')