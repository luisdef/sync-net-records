import os.path
from os import getenv
from dotenv import load_dotenv

from utils.text import ok_msg
from utils.text import err_msg


def validate() -> bool | Exception: 
    """Checking if requirements are satisfied.
    - secrets/ directory;
    - `.env` file and sheet id."""
    if not (os.path.exists('secrets/') and (
        os.path.exists('secrets/token.json') or
        os.path.exists('secrets/credentials.json')
    )):
        raise Exception(err_msg('Secrets auth directory not found.'))
    
    if not (os.path.exists('.env')):
        raise Exception(err_msg('\'.env\' file not found.'))
    
    load_dotenv()
    if not (bool(getenv('SHEET_ID'))):
        raise Exception(err_msg('Sheet ID not found in .env file.'))
    
    print(ok_msg('Validation OK.'))
    return True


if __name__ == '__main__':
    validate()
