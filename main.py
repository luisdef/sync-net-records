from pprint import pprint as p
from src.get_sheet_data import get_sheet_data
from src.get_db_data import fetch_net_records
import datetime

def main():
    list_from_db = fetch_net_records()
    for rec in list_from_db:
        rec['created_at'] = datetime.datetime(
                                year=rec['created_at'].year,
                                month=rec['created_at'].month,
                                day=rec['created_at'].day,
                                hour=rec['created_at'].hour,
                                minute=rec['created_at'].minute,
                                second=rec['created_at'].second
                            ).strftime('%d/%m/%Y %H:%M:%S')
        rec['updated_at'] = datetime.datetime(
                                year=rec['updated_at'].year,
                                month=rec['updated_at'].month,
                                day=rec['updated_at'].day,
                                hour=rec['updated_at'].hour,
                                minute=rec['updated_at'].minute,
                                second=rec['updated_at'].second
                            ).strftime('%d/%m/%Y %H:%M:%S')
    p(list_from_db)
    # list_from_sheet = get_sheet_data()


if __name__ == "__main__":
    main()
