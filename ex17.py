# obtain headlines from https://www.nytimes.com/

import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(data.text, 'html.parser')

print('The homepage is...\n' + soup.title.text + '\n')

print('These are the the titles on the webpage...\n')
for title in soup.find_all('h2'):
    print(title.string)
