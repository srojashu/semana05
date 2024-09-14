from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1cryh3rXwsnTNSLwTQN5P9pmjJ7SAAr-FKbEU3XjW4bI'

nombre_usuario = input("Introduce el nombre del usuario: ")

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


values = [[nombre_usuario]]

result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='A1',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")