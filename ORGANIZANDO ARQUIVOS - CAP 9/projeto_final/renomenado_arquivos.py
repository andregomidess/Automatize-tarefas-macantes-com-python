import os, re, shutil,send2trash, random

os.makedirs('/home/andre/aquivos_data_americana')   #pasta criada
diretorio_de_trabalho = os.chdir('/home/andre/aquivos_data_americana')
for i in range(10):
    mes = str(random.randint(1, 12))
    dia = str(random.randint(1, 30))
    ano = str(random.randint(2010, 2021))
    data = mes + '-' + dia + '-' + ano
    arqs = open('galo %s.txt'%data, 'w')
    
data_regex = re.compile(r'''
                        ^(.*?)  # todo o texto antes
                        ((0|1)?\d)-  # meses 
                        ((0|1|2|3)?\d)- # dois digitos do dia
                        (20\d\d)    # ano so contadno os anos 2000 pra frente
                        (.*?)$  # todo o resto dps
            ''', re.VERBOSE)

    