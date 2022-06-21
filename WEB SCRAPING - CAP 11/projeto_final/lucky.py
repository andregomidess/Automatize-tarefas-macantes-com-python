#!/usr/bin/python3
from os import link
import requests, sys, webbrowser, bs4


print('Baixando pagina do Google...')
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="lxml")
linkss = soup.select('.yuRUbf a')

num_open = min(5, len(linkss))
for i in range(num_open):
    webbrowser.open('http://google.com' + linkss[i].get('href'))