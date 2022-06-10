import shutil, os, send2trash, zipfile


u = shutil.copy('/home/andre/hello', '/home/andre/delicious') # copia arquivo de uma path para outra
print(u)
shutil.copy('/home/andre/hello', '/home/andre/delicious/hello2') # copia o arquivo e coloca o nome hello2 ou oq o programador quiser


v = shutil.copytree('/home/andre/delicious', '/home/andre/delicious_backup') # copia a pasta inteira para outro diretorio

shutil.move('/home/andre/bacon.txt', '/home/andre/delicious/new_bacon.txt') # move o arquivo e mudad seu nome

# smp use um comentario e um print para saber oq vc está apagando, a função unlink apaga permanentemente, e apenas um erro pode fazer oq vc n queria
# forma errada
for filename in os.listdir():
    if filename.endswith('.rxt'):
    #os.unlink(filename)
        pass

# forma certa
for filename in os.listdir():
    if filename.endswith('.rxt'):
    #os.unlink(filename)
    #print(filename)
        pass
    
# a biblioteca send2trash não apaga o arquivo permanentemente igual os metodos de os e shutil    
baconFile = open('bacon.txt', 'a') # cria o arquivo
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

for folderName, subfolders, filenames in os.walk('/home/andre/delicious'): # função os.wall percorre toda arvore de arquivos e pasta do dir atual,  e retorna 3 valores
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
print('')

os.chdir('/home/andre') # indo ao diretorio atual
exemplo_zip = zipfile.ZipFile('exemplo.zip') # abrindo o zip desse dir
print(exemplo_zip.namelist())   # listando os paths e arquivos desse zip
spamInfo = exemplo_zip.getinfo('hello') # peagdno info so arquivo hello.txt
print(spamInfo.file_size)   #vedno tamanho dele
print(spamInfo.compress_size) # vendo o tamanho dele compactado em formato zip

exemplo_zip.extractall() # vai extrair o zip para o dir atual


# vc pode extrair um unico arquivo para outro diretorio
#exemplo_zip.extract('hello')
exemplo_zip.extract('hello', 'home/andre/delicious')

# criar e add arquivo em zips

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('hello', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


        