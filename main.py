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
    list_from_sheet = get_sheet_data()
    same = []
    not_same = []
    for s_rec in list_from_sheet:
        for db_rec in list_from_sheet:
            if db_rec['mac'] == s_rec['mac']:
                same.append(s_rec)
            else:
                if (db_rec['name'] == s_rec['name'] 
                    and db_rec['device'] == s_rec['device'] 
                    and db_rec['mac'] != s_rec['mac']):
                    not_same.append(s_rec)
    #p(same)
    p(len(same))
    p(len(not_same))
    p(not_same)


if __name__ == "__main__":
    main()
