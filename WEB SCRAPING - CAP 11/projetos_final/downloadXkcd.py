import os, requests, bs4


url = 'http://xkcd.com'
os.makedirs('tirinhas', exist_ok=True)
while not url.endswith('#'):    # se tem um # no final da url chegou na primeira tirinha do site
    print(f'Baixando a pagina {url}')
    res = requests.get(url) # baixando o conteudo da url
    res.raise_for_status()  # checando se tem algum erro no download da página
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    conteudo_tirinha = soup.select('#comic img')    # o '#' vai pegar tudo q tem a id="comic" no html, apos isso vai acessar a tag img
    if conteudo_tirinha == []:
        print('Não foi encontrado nenhuma tirinha!')
    else:
       link_tirinha = 'http:' + conteudo_tirinha[0].get('src')  # montando o site da img que está apos o src="link"
       print(f'Baixando a imagem {link_tirinha}')
       res = requests.get(link_tirinha) # baixando o conteudo da pagina da foto
       res.raise_for_status()   # vrificando se há erro
       imagem = open(os.path.join('tirinhas', os.path.basename(link_tirinha)), 'wb')
       for chunk in res.iter_content(100000):
           imagem.write(chunk)
       imagem.close()
    prev_link = soup.select('a[rel="prev"]')[0] # vai pegar o link do botão prev que no caso é outra img
    url = 'http://xkcd.com' + prev_link.get('href')  
            
    