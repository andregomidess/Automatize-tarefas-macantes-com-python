#!/usr/bin/python3
import os, bs4, requests, sys

url = 'https://www.bigboygames.com.br/loja/busca.php?loja=906426&palavra_busca=' + ' '.join(sys.argv[1:])
os.makedirs('jogos_BigBoyGames', exist_ok=True)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elementos_site = soup.select('.image img')  # pegando os elementos img q contenham a class product box image
if elementos_site == []:
    print('Não foi encontrado nenhum produto com essa pesquisa!')
else:
    for i in range(len(elementos_site)):
        link_produtos = elementos_site[i].get('data-src')
        if link_produtos == '':
            break
        print(f'Baixando a imagem {link_produtos}')
        res = requests.get(link_produtos)
        res.raise_for_status()
        imagem = open(os.path.join('jogos_BigBoyGames', os.path.basename(link_produtos)), 'wb')
        for chunk in res.iter_content(100000):
            imagem.write(chunk)
    imagem.close()
print('Concluido!')            
       
