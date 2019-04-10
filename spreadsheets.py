import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('secret_keys.json', scope)
client = gspread.authorize(credentials)

sheet = client.open('Carros').sheet1

#Puxando todas as linhas com nomes de colunas:

carros = sheet.get_all_records()

for carro in carros:
    print(carro)

#Conseguindo dados de uma linha específica:

row4 = sheet.row_values(4) #No caso do teste, o Volkswagen Jetta

print(f"\nRow 4: {row4}")

#Conseguindo dados de uma coluna específica:

col2 = sheet.col_values(2) #No caso do teste, os modelos dos carros

print(f"\nCol 1: {col2}")

#Conseguindo algum dado de uma célula específica:

cell4_9 = sheet.cell(4,9).value #No caso do teste, o preço do Volkswagen Jetta

print(f"\nCell 4,9: {cell4_9}")

#Atualizando algum dado da planilha:

sheet.update_cell(4,9,63000) #No caso do teste, aumentando o preço do Jetta

preco_atualizado = sheet.cell(4,9).value

print(f"\nNovo preço do Jetta: {cell4_9}")

#Adicionando uma row no fim do arquivo:

row_audi = ['Audi', 'A3', '2001/2001', 'Manual', 'Esportivo', 'Prata', '60000', '3', '30000']
index_final = len(carros) + 2 #Essa adição de 2 é para contar também a linha de cabeçalho!

#sheet.insert_row(row_audi,index_final)

#Deletando a última row:

index_final = len(carros) + 1

#sheet.delete_row(index_final)