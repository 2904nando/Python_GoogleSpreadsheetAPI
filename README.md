# Python_GoogleSpreadsheetAPI

Neste programa de teste eu estou conectando meu programa em Python à um arquivo no Google Drive (Spreadsheet) para extrair, modificar, inserir e excluir dados dele.

**Para conseguir isso, eu precisei criar um projeto na Google Developer Cloud Console, ativar as API do Google Drive e do Spreadsheets, criar minhas credenciais (Papel "Projeto" > "Editor") e exportá-las como JSON, para serem utilizadas no meu programa com a biblioteca _oauth2client_. Acessei esse arquivo e copiei o email _client_email_, acessei minha planilha do drive e compartilhei com esse mesmo email copiado para que ele possa visualizar e editar tudo.**

Exportei a planilha para um _.xlsx_ para que qualquer um possa testar e ter os mesmos resultados!

_Obviamente, por motivos de segurança, não estou disponibilizando o arquivo com as minhas credenciais._

As operações feitas no programa **spreadsheet.py** são as seguintes:

## Extração de todas as linhas como uma lista de dicionários

Utilizando a função _get_all_records()_.

