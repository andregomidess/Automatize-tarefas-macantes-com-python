#!/usr/bin/python3
from os import link
import requests, sys, webbrowser, bs4


print('Baixando pagina...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkss = soup.select('.package-snippet')

num_open = min(5, len(linkss))
for i in range(num_open):
    webbrowser.open('https://pypi.org' + linkss[i].get('href'))