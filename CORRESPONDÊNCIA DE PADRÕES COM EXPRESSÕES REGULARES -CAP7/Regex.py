import re


def regex():
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search('My number is 415-555-4242')
    print(f'Phone number found: {mo.group()}')
    

def regex_groups():
    phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
    mo = phoneNumRegex.search('My number is (415)-555-4242.')

    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(0))
    print(mo.group())
    print(mo.groups())

    areaCode, mainNumber = mo.groups()
    print(areaCode)
    print(mainNumber)
    

def regex_pipe():
    heroRegex = re.compile(r'Batman|Tina Fey') # |(pipe), vai retornar o primeiro que achar na string
    mo1 = heroRegex.search('Batman and Tina Fey')
    print(mo1.group())
    
    mo2 = heroRegex.search('Tina Fey and Batman')   
    print(mo2.group())     
  
  
def regex_pipe_prefixo():
    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = batRegex.search('Batcopter lost a wheel')
    print(mo.group())
    print(mo.group(1))
    
    
def regex_opcional():
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())
    
    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    mo1 = phoneRegex.search('My number is 415-555-4242')
    print(mo1.group())
    
    mo2 = phoneRegex.search('My number is 555-4242')
    print(mo2.group())
    
    
def regex_asterisco():
    batRegex = re.compile(r'Bat(wo)*man')   # se tiver 0 ou mais (wo) ele imprime -> corresponda a 0 ou mais
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())
    
    mo3 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo3.group())


def regex_adicao():
    batRegex = re.compile(r'Bat(wo)+man') # corresponde a 1 ou mais (wo)
    mo1 = batRegex.search('The Adventures of Batwoman')
    print(mo1.group())
    
    mo2 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo2.group())
    
    mo3 = batRegex.search('The Adventures of Batman')
    print(mo3 == None)
    

def regex_freq():
    haRegex = re.compile(r'(Ha){3}')    # frequencia exata de quantos Ha devem aparecer {3, 5}, min e max
    mo1 = haRegex.search('HaHaHa')
    print(mo1.group())
    
    mo2 = haRegex.search('Ha')  # se aparecer apena um já não é valido, tem q ser 3 exato
    print(mo2 == None)       


def regex_findall():
    #metodo search so retorna o primeiro valor encontrado na string, já o findall retorna todos em uma lista
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # não tem nenhum grupo
    mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(mo)
    
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # com grupos, retorna um lista de tuplas
    mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(mo)
    
    
def regex_propria_classe():
    vowelRegex = re.compile(r'[aeiouAEIOU]') #vai pegar apenas as vogais
    mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(mo)
    
    consonantRegex = re.compile(r'[^aeiouAEIOU]') # o ^ serve para fazer a negação de td que está dentro do colchetes, ou seja vai pegar tds as consoantes
    mo1 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(mo1)        


def caractere_curinga():
    atRegex = re.compile(r'.at')    #vai pegar todos .at, no qual o . é substituido por qualquer letra ou numero
    mo = atRegex.findall('The cat in the hat sat on the flat mat.')
    print(mo)
    
    nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    mo = nameRegex.search('First Name: Al Last Name: Sweigart')
    print(mo.group(1))
    print(mo.group(2))
    
    nongreedyRegex = re.compile(r'<.*?>')
    mo = nongreedyRegex.search('<To serve man> for dinner.>')
    print(mo.group())   #nongreedy, menor string possivel
    
    greedyRegex = re.compile(r'<.*>')
    mo = greedyRegex.search('<To serve man> for dinner.>')
    print(mo.group()) #greedy, maior string possível
    
    
def caractere_curinga_quebra_linha():
    newlineRegex = re.compile('.*') # sem o re.DOTALL ele para no primeiro \n
    mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
    print(mo)  
    
    newlineRegex = re.compile('.*', re.DOTALL)  #com re.DOTALL ele imprime certo
    mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
    print(mo)   

def substitui_string():
    namesRegex = re.compile(r'Agent \w+')
    mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
    print(mo)
    
    agentNamesRegex = re.compile(r'Agent (\w)\w*')  #string Agent seguido pela primeira char e depois o resto tae o espaço
    mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
    print(mo) # substitui 

    
if __name__ == '__main__':
    regex()
    print()
    print('='*20)
    
    regex_groups()
    print()
    print('='*20)
    
    regex_pipe()
    print()
    print('='*20)
    
    regex_pipe_prefixo()
    print()
    print('='*20)
    
    regex_opcional()
    print()
    print('='*20)
    
    regex_asterisco()  
    print()
    print('='*20)
    
    regex_adicao()
    print()
    print('='*20)
    
    regex_freq()
    print()
    print('='*20)
    
    regex_findall()
    print()
    print('='*20)
    
    xmasRegex = re.compile(r'\d+\s\w+') 
    #(\d+) um ou mais digito, (\s) seguido por um espaço, (\w+) um ou mais caracteres
    mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
    print(mo)
    
    regex_propria_classe()
    print()
    print('='*20)
    
    beginsWithHello = re.compile(r'^Hello') 
    # o ^ pode ser usado no início de uma regex para indicar que uma correspondência deve ocorrer no início de um texto pesquisado
    mo = beginsWithHello.search('Hello world!')
    print(mo)
    
    endsWithNumber = re.compile(r'\d$')
    #A string r'\d$' de expressão regular corresponde a strings que terminem com um caractere numérico de 0 a 9
    mo = endsWithNumber.search('Your number is 42')
    print(mo)
    
    wholeStringIsNum = re.compile(r'^\d+$')
    #A string r'^\d+$' de expressão regular corresponde a strings que comecem e terminem com um ou mais caracteres numéricos.
    mo = wholeStringIsNum.search('1234567890')
    print(mo)
    mo = wholeStringIsNum.search('12345xyz67890') == None
    print(mo)
    
    
    print()
    print('='*20)
    
    caractere_curinga() #todos caracteres menos o quebra linha (\n)
    print()
    print('='*20)
    
    caractere_curinga_quebra_linha()
    print()
    print('='*20)
    
    # para não ter problemas em caçar palavras com letras maiusculas ou minusculas use o re.I 
    robocop = re.compile(r'robocop', re.I)
    mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
    print(mo)
    mo = robocop.search('ROBOCOP is part man, part machine, all cop.').group()
    print(mo)
    mo = robocop.search('Al, why does your programming book talk about robocop somuch?').group()
    print(mo)
    print()
    print('='*20)
    
    substitui_string()
    
    phoneRegex = re.compile(r'''((\d{3}|\(\d{3}\))?
                            (\s|-|\.)?
                            \d{3}
                            (\s|-|\.)
                            \d{4}
                            (\s*(ext|x|ext.)\s*\d{2,5})?
                            )''', re.VERBOSE)
    
    
      