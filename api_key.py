import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

service = build('sheets', 'v4', developerKey=API_KEY)
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range='A1'
).execute()

print(result.get('values', [['']])[0][0])
