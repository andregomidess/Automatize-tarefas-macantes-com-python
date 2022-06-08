import re, pyperclip


url = re.compile(r'''(
    (\w{4}://|\w{5}://)? #   http:// ou https://
    ([w]{3}\.)?    # www.
    ([a-zA-Z0-9]{2,4}\.)?   #.pt, .en, etc...
    ([a-z0-9]+)   #   corpo do site
    (\.[a-z]{2,4})    #   .com, .org, etc...
    (\.[a-z]{2})?   # extensão de cada pais, .br, .uk, etc...
    )''', re.VERBOSE|re.IGNORECASE)

texto = str(pyperclip.paste())
urls = []
for groups in url.findall(texto):
    urls.append(groups[0])
if len(urls) > 0:
    pyperclip.copy('\n'.join(urls))
    print('Links copiado!')
    print('\n'.join(urls))
else:
    print('Não foi encontrado nenhum link!')        