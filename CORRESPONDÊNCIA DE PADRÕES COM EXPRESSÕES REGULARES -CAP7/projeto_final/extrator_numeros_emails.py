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
                (\d{2}|\(\d{2}\))?   # ddd da área
                (\s)?    # espaço ddd e numero
                (\d?\d+)  # primeiros 4 dígitos
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


