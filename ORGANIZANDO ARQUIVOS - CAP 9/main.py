import shutil, os, send2trash


#u = shutil.copy('/home/andre/hello', '/home/andre/delicious') # copia arquivo de uma path para outra
#print(u)
#shutil.copy('/home/andre/hello', '/home/andre/delicious/hello2') # copia o arquivo e coloca o nome hello2 ou oq o programador quiser


#v = shutil.copytree('/home/andre/delicious', '/home/andre/delicious_backup') # copia a pasta inteira para outro diretorio

shutil.move('/home/andre/bacon.txt', '/home/andre/delicious/new_bacon.txt') # move o arquivo e mudad seu nome

# smp use um comentario e um print para saber oq vc está apagando, a função unlink apaga permanentemente, e apenas um erro pode fazer oq vc n queria
# forma errada
for filename in os.listdir():
    if filename.endswith('.rxt'):
    os.unlink(filename)

# forma certa
for filename in os.listdir():
    if filename.endswith('.rxt'):
    #os.unlink(filename)
    print(filename)
    
        