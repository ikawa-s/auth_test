from google.oauth2 import service_account
from googleapiclient.discovery import build

SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=SCOPES
)

service = build('sheets', 'v4', credentials=creds)
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range='A1'
).execute()

print(result.get('values', [['']])[0][0])
