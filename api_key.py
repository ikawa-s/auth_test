from googleapiclient.discovery import build

API_KEY = 'YOUR_API_KEY'
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'

service = build('sheets', 'v4', developerKey=API_KEY)
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range='A1'
).execute()

print(result.get('values', [['']])[0][0])
