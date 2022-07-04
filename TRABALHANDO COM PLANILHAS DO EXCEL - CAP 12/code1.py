import openpyxl


wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.sheetnames)    # printando tds os nomes
sheet = wb['Sheet3'] #pegando a sheet3
print(sheet.title)
anotherSheet = wb.active    # pegando a sheet ativa (a primeira que abrir no excel)
print(anotherSheet)