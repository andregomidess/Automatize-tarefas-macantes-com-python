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
    
    
      