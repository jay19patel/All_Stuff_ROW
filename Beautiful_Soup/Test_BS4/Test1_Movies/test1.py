
import requests
from bs4 import BeautifulSoup

response = requests.get('https://timesofindia.indiatimes.com/entertainment/movie-reviews')
alltitle = []
allstars = []

soup = BeautifulSoup(response.text, 'html.parser')

for i in soup.find_all('div',{"class":"sli_title"}):
    alltitle.append(i.text)

for j in soup.find_all('div',{"class":"sli_starRating lgttxt"}):
    allstars.append(j.text)

file = open('Test_BS4/Test1/movies.txt','w')
for i in range(len(alltitle)):
    print(f"MOVIE : {alltitle[i]} || STARS : {allstars[i]}")
    file.write(f"MOVIE : {alltitle[i]} || STARS : {allstars[i]} \n")
file.close()


