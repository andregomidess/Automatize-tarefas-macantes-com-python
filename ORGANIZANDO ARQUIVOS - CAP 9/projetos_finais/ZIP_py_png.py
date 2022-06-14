import zipfile, os


def zip_py_png(pasta):
    nome = 'zip_py_png.zip'
    print(f'Criando {nome}')
    pasta_zip = zipfile.ZipFile(nome, 'w')
    
    for foldername, subfolders, filenames in os.walk(pasta):
        print(f'inserindo arquivo em {foldername}...')
        pasta_zip.write(foldername)
        for filename in filenames:
            if filename.endswith('.py') or filename.endswith('.png'):
                pasta_zip.write(os.path.join(foldername, filename))
    pasta_zip.close()            
    print('Concluido!')
    
    
if __name__ == '__main__':
    zip_py_png('/home/andre/teste')        