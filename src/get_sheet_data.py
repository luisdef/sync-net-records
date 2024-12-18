import os.path
import os
from os import getenv
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.exceptions import RefreshError
from config import validate
from utils.text import err_msg

SHEET_SCOPE_ACCESS = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

load_dotenv()
SAMPLE_SPREADSHEET_ID = getenv('SHEET_ID')
SHEET_FOLDER = getenv('SHEET_FOLDER')


def establish_connection_get_credentials() -> str:
    creds = None
    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file(
            "secrets/token.json", SHEET_SCOPE_ACCESS
        )
    if not creds or not creds.valid:
        flow = False
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                os.remove('secrets/token.json')
                print(err_msg('Token expired.'))
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "secrets/credentials.json", SHEET_SCOPE_ACCESS
            )
        if flow:
            creds = flow.run_local_server(port=0)
    with open("secrets/token.json", "w") as token:
        token.write(creds.to_json())
    
    return creds


def get_sheet_data() -> list:
    validate()
    credentials = establish_connection_get_credentials()
    
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SHEET_FOLDER)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print(err_msg('No data found.'))
            return

        keys = None
        list_of_records = []
        for i in range(len(values)):
            if i == 0:
                keys = values[i]
            else:
                record = {}
                idx = 0
                for key in keys:
                    record[key] = values[i][idx]
                    idx += 1
                list_of_records.append(record)
        return list_of_records
    except HttpError as err:
        print(err)
