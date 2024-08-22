from pprint import pprint as p
from src.get_sheet_data import get_sheet_data


def main():
    list_of_devices = get_sheet_data()
    p(list_of_devices)


if __name__ == "__main__":
    main()
