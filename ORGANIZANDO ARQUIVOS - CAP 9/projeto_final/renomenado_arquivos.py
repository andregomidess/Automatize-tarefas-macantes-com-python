import os, re, shutil,send2trash, random
##################################################################

#apenas para criar os arquivos

#os.makedirs('/home/andre/aquivos_data_americana')   #pasta criada
diretorio_de_trabalho = os.chdir('./home/andre/aquivos_data_americana')
#for i in range(10):
#    mes = str(random.randint(1, 12))
#    dia = str(random.randint(1, 30))
#    ano = str(random.randint(2010, 2021))
#    data = mes + '-' + dia + '-' + ano
#    arqs = open('galo%s.txt'%data, 'w')
################################################################    
data_regex = re.compile(r'''
                        ^(.*?)  # todo o texto antes
                        ((0|1)?\d)-  # meses 
                        ((0|1|2|3)?\d)- # dois digitos do dia
                        (20\d\d)    # ano so contadno os anos 2000 pra frente
                        (.*?)$  # todo o resto dps
            ''', re.VERBOSE)

for nome_arq_americano in os.listdir(diretorio_de_trabalho):
    
    nomes = data_regex.search(nome_arq_americano)
    if nomes == None:
        continue
    texto_antes = nomes.group(1)
    meses_arq = nomes.group(2)
    dia_arq = nomes.group(4)
    ano_arq = nomes.group(6)
    texto_depois = nomes.group(7)
    
    arq_data_europeia = texto_antes + dia_arq + '-' + meses_arq + '-' + ano_arq + texto_depois
    
    diretorio_de_trabalho_abs = os.path.abspath('.')
    nome_arq_americano = os.path.join(diretorio_de_trabalho_abs, nome_arq_americano)
    arq_data_europeia = os.path.join(diretorio_de_trabalho_abs, arq_data_europeia)
    
    print(f'Mudando "{nome_arq_americano}" para "{arq_data_europeia}"')
    shutil.move(nome_arq_americano, arq_data_europeia)
    