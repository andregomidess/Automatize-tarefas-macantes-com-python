import os, shutil


diretorio_de_trabalho = os.chdir('/home/andre/aquivos_data_americana')
for nome_arq in os.listdir(diretorio_de_trabalho):
    novo_nome = 'spam_' + nome_arq
    
    dir_trab_abs = os.path.abspath('.')
    
    path_old = os.path.join(dir_trab_abs, nome_arq)
    path_new = os.path.join(dir_trab_abs, novo_nome)
    
    print(f'Mudando "{path_old}" para "{path_new}"')
    shutil.move(nome_arq, novo_nome)
    
