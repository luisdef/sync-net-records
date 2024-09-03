from pprint import pprint as p
from src.get_sheet_data import get_sheet_data
from src.get_db_data import fetch_net_records
from utils.text import err_msg, ok_msg
from utils.date_and_time import seconds_between_dates


def main():
    list_from_db = fetch_net_records()
    list_from_sheet = get_sheet_data()
    # Order to sync the records.
    
    # NEW RECORDS
    # A new record is some record that is in the sheets but is not in
    # database, so if a name+device+os does not match any record that
    # is in the database it will insert the new record.
    
    # UPDATE RECORDS
    # Example: a record that is newer and equal to other by name+device+os.
    # Then update the database.
    # Need to see the authorization to update the google sheet form.
    
    # See the records that are in the sheet and are not in database
    # Ask if wants to save the record in the database

if __name__ == "__main__":
    main()
 