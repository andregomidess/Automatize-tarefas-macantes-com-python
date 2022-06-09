import os, random

#todas as capitais americanas
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for num_prova in range(35):
    prova_file = open('provaCapitais%s.txt' %(num_prova + 1), 'w')
    gabarito = open('provaCapitais_gabarito%s.txt'%(num_prova + 1), 'w')
    
    # Cabeçalho da prova
    prova_file.write('Nome:\nData:\n\nTurma:\n\n')
    prova_file.write((''*20)+'Prova da capital dos estados americanos(Form %s)' %(num_prova + 1))
    prova_file.write('\n\n')
    
    #embaralha a ordem dos estados
    estados = list(capitals.keys())
    random.shuffle(estados)

#   percorre todos os 50 estados em um loop    
    for num_questao in range(50):
        respostas_correta = capitals[estados[num_questao]]
        respostas_erradas = list(capitals.values())
        del respostas_erradas[respostas_erradas.index(respostas_correta)]
        respostas_erradas = random.sample(respostas_erradas, 3)
        opcao_de_respostas = respostas_erradas + [respostas_correta]
        random.shuffle(opcao_de_respostas)
        
        #grava a pergunta e as opções de resposta no arquivo de prova
        prova_file.write('%s. Qual é a capital do estado de %s?\n' %(num_questao + 1, estados[num_questao]))
        for i in range(4):
            prova_file.write('  %s. %s\n' %('ABCD'[i], opcao_de_respostas[i]))
        prova_file.write('\n')
        #grava o gabarito com as respostas em um arquivo    
        gabarito.write('%s. %s\n' %(num_questao + 1, 'ABCD'[opcao_de_respostas.index(respostas_correta)]))
prova_file.close()
gabarito.close()               
    