from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

service = build('sheets', 'v4', credentials=creds)
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range='A1'
).execute()

print(result.get('values', [['']])[0][0])
