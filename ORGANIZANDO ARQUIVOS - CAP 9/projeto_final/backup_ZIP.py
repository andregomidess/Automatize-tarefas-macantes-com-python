import os, shutil, zipfile

# função para criar o nome da pasta zip
def backup_zip(pasta):
    pasta = os.path.abspath(pasta)  # garante que o dir pasta é absoluto
    num = 1
    while True:
        nome_zip = os.path.basename(pasta) + '_' + str(num) + '.zip'
        if not os.path.exists(nome_zip):    # se existe um nome1.zip, acrescenta mais 1 no num, se existe da break
            break
        num += 1
    
    print (f'Criando {nome_zip}...')
    backup = zipfile.ZipFile(nome_zip, 'w')
    
    for foldername, subfolders, filenames in os.walk(pasta):
        print(f'adicionando arquivos em {foldername}...')
        backup.write(foldername)
        for filename in filenames:
            nova_base = os.path.basename(pasta) + '_'
            if filename.startswith(nova_base) and filename.endswith('.zip'):
                continue    # n faz o backup
            backup.write(os.path.join(foldername, filename))
    backup.close()
    print('Concluido')
    
if __name__ == '__main__':
    backup_zip('/home/andre/delicious')            