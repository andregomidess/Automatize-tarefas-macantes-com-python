import openpyxl, pprint, os


planilha = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = planilha['Population by Census Tract']
dados_condado = {}

for linhas in range(2, sheet.max_row + 1):
    estado = sheet['B' + str(linhas)].value
    condado = sheet['C' + str(linhas)].value
    pop = sheet['D' + str(linhas)].value
    dados_condado.setdefault(estado, {})
    dados_condado[estado].setdefault(condado, {'tracts': 0, 'pop': 0})
    dados_condado[estado][condado]['tracts'] += 1 
    dados_condado[estado][condado]['pop'] =+ int(pop)
    
resultado = open('census2010.py', 'w')
resultado.write('allData = ' + pprint.pformat(dados_condado))
resultado.close()
    
