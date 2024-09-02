from pprint import pprint as p
from src.get_sheet_data import get_sheet_data
from src.get_db_data import fetch_net_records
from utils.text import err_msg, ok_msg
from utils.date_and_time import seconds_between_dates


def main():
    list_from_db = fetch_net_records()
    list_from_sheet = get_sheet_data()
    not_same = []
    for sheet_rec in list_from_sheet:
        for db_rec in list_from_db:
            if db_rec['mac_address'].upper() == sheet_rec['mac'].upper():
                continue
            else:
                if (db_rec['name'] == sheet_rec['name'] 
                    and db_rec['device'] == sheet_rec['device'] 
                    and db_rec['mac_address'].upper() != sheet_rec['mac'].upper()):
                    not_same.append(db_rec)
    if (len(not_same)) >= 1:
        print(err_msg('These record(s) are not the same between datasets:'))
        print(f'{"Nome":<20} | {"Tipo Disp.":<20} | {"MAC":<20}')
        print('-' * 66)
        for rec in not_same:
            if 'mac' in rec:
                print(f'{rec["name"]:<20} | {rec["device"]:<20} | {rec["mac"]:<20}')
            else:
                print(f'{rec["name"]:<20} | {rec["device"]:<20} | {rec["mac_address"]:<20}')
                
    else:
        print(ok_msg('The records are in sync.'))
    input('\nPress enter to exit...')


if __name__ == "__main__":
    main()
