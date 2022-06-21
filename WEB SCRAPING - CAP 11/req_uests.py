import requests, bs4


#res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # metodo requests.get() pega tudo oq ta na pagina
#print(type(res))

#print(res.status_code == requests.codes.ok)
#print(len(res.text))
#print(res.text[:250])


#res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status()  # este metodo interrompe o download caso a exista algum erro


#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#res.raise_for_status()
#playFile = open('RomeoAndJuliet.txt', 'wb') # para gravar o conteudo de uma pagina em um aqr txt deve abrir no modo escrita binaria (wb) para preservar o seu unicode
#for chunk in res.iter_content(100000): # o metodo inter_content() está acesando tudo que o res pegou do site
#    b = playFile.write(chunk)
#print(b)

#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#noStarchSoup = bs4.BeautifulSoup(res.text)
#print(type(noStarchSoup))

arq_ex = open('exemplo.html')
#soup_ex = bs4.BeautifulSoup(arq_ex)
#print(type(soup_ex))

exampleSoup = bs4.BeautifulSoup(arq_ex.read())
elems = exampleSoup.select('#author')
print(elems[0].get_text())
print(str(elems[0]))
print(elems[0].attrs)   # retorna um dicionario com as tags id