import os.path
from os import getenv
from dotenv import load_dotenv
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import validate

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

load_dotenv()
SAMPLE_SPREADSHEET_ID = getenv('SHEET_ID')
RANGE = 'mac-records'


def main():
    validate()
    
    creds = None
    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file("secrets/token.json", SCOPES)
    if not creds or not creds.valid:
        flow = False
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "secrets/credentials.json", SCOPES
            )
        if flow:
            creds = flow.run_local_server(port=0)
    with open("secrets/token.json", "w") as token:
        token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=RANGE)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
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
                    list_of_records.append(record)
                    idx += 1
        print(json.dumps(list_of_records))
    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
