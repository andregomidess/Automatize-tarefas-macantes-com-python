import os
import shelve

p = os.path.join('usr', 'bin', 'spam')  #mostra o caminho
print(p)

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']    # caso queira guardar o diretorio de varios arquivos
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
    
p = os.getcwd() # epgar o diretorio de trabalho atual
print(p)
os.chdir('/home/andre') # muda o diretorio
p = os.getcwd()

g = os.makedirs('/home/andre/delicious/walnut/waffles')   # cria pastas

p = os.path.abspath('..')
print(p)
p = os.path.isabs('.') # esse diretorio é absoluto?
print(p)
p = os.path.isabs(os.path.abspath('.'))
print(p)
p = os.path.relpath('/.', '/home/andre')
print(p)
p = os.path.relpath('/home', '/home/delicious/walnuts/waffles') #mostra o diretorio relativo
print(p)

path = 'home/andre/documentos/calc.exe'
print(os.path.basename(path))   # mostra o basename, que é a ultima string
print(os.path.dirname(path))    # mostra o dirname, que é tudo antes da ultima string

print(os.path.split(path))  # o split retona o dirname e o dirname em uma tupla

p = path.split(os.path.sep) # usando o split ele vai separar exatamente tudo e colocar em uma lista
print(p)

p = os.path.getsize(os.getcwd()) # mostra o tamanho do diretorio em bytes
print(p)
p = os.listdir(os.getcwd()) # vai botar em uma lista o nome de todos os srquivos dentro desse diretorio
print(p)

totalSize = 0
for filename in os.listdir('/./home/andre'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/andre', filename))    # vai pegar o tamanho total de tds os arquivos dentro desse diretorio
print(totalSize)

helloFile = open('/home/andre/hello', 'r')  # leitura de arquivos
helloContent = helloFile.read()
print(helloContent)

sonetoFile = open('/home/andre/soneto29')
sonetoContent = sonetoFile.readlines()
print(sonetoContent)

# escrita e adição de escrita em arquivo
galoFile = open('galo.txt', 'w')    # 'w' vai zerar oq existe e criar um novo arquivo
galoFile.write('Galão é gigante\n')

galoFile.close()
galoFile = open('galo.txt', 'a')    # 'a' vai editar oq ja existe
galoFile.write('Hulk esmaga!!')

galoFile.close()
galoFile = open('galo.txt')
texto = galoFile.read()
galoFile.close()

print(texto)

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
shelfFile = shelve.open('mydata')
l = list(shelfFile.keys())
v = list(shelfFile.values())
print(l)
print(v)
shelfFile.close()