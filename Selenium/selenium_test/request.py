import requests


url ="www.youtube.com"

r = requests.get('https://api.github.com/events')
print(r.status_code)