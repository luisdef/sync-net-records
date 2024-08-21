from pprint import pprint as p
from src.get_sheet_data import get_sheet_data


def main():
    list_of_devices_from_google_sheets = get_sheet_data()


if __name__ == "__main__":
    main()
