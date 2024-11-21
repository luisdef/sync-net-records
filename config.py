import os.path
from os import getenv
from dotenv import load_dotenv
from utils.text import err_msg


def validate() -> bool | Exception:
    """
    Checking if requirements are satisfied.
    
    Returns:
        bool: true if everything is ok.
    
    Raises:
        Exception: If something was not found.
    """
    if not (os.path.exists('secrets/') and (
        os.path.exists('secrets/token.json') or
        os.path.exists('secrets/credentials.json')
    )):
        raise Exception(err_msg('Secrets auth directory not found.'))
    
    if not (os.path.exists('.env')):
        raise Exception(err_msg('\'.env\' file not found.'))
    
    load_dotenv()
    if (not (bool(getenv('SHEET_ID')))
        ) or (not (bool(getenv('SHEET_FOLDER')))
        ) or (not (bool(getenv('HOST_DB')))
        ) or (not (bool(getenv('DATABASE')))
        ) or (not (bool(getenv('USER_DB')))
        ) or (not (bool(getenv('PASSWD_DB')))
        ):
        raise Exception(err_msg('Environment variables missing.'))
    return True


if __name__ == '__main__':
    validate()
