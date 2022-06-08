import pyperclip, re


honeRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # código de área
    (\s|-|\.)?  # separador
    (\d{3}) # primeiros 3 dígitos
    (\s|-|\.) # últimos 4 dígitos
    (\d{4}) # últimos 4 dígitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
)''', re.VERBOSE)


brasil_number = re.compile(r'''(
                (\d{2}|\(\d{2}\))   # ddd da área
                (\s)    # espaço ddd e numero
                (\d?\d{4})  # primeiros 4 dígitos
                (\s|-)   # separador dos digitos
                (\d{4})  # ultimos 4 dígitos
)''', re.VERBOSE)


email = re.compile(r'''(
    [a-zA-z0-9._%+-]+  #    nome do usuário
    @                   # o arroba
    [a-zA-z0-9_.-]+     # dominio
    (\.[a-zA-z]{2,4})?  # .edu, etc...
    (\.[a-zA-z]{2,4})   # .com, .br etc...
    
    )''', re.VERBOSE)


texto = str(pyperclip.paste())
numeros_emails = []
for groups in brasil_number.findall(texto):
    numero_tel = ' '.join([groups[1], groups[3], groups[5]])
    numeros_emails.append(numero_tel)
for groups in email.findall(texto):
    numeros_emails.append(groups[0])
    
if len(numeros_emails) > 0:
    pyperclip.copy('\n'.join(numeros_emails))
    print('texto copiado!')
    print('\n'.join(numeros_emails))
else:
    print('Não foi encontrado nenhum número ou email')            
