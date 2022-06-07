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
    
    
      