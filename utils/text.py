import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def trim(docstring: str) -> str:
    """
    Removes whitespace from both ends of a string.

    This function removes all leading and trailing whitespace characters
    (space, tab, no-break space, etc.) from the given string and returns
    the resulting trimmed string.

    Args:
        s (str): The string to trim.

    Returns:
        docstring (str): The trimmed string without leading or trailing whitespace.

    Examples:
        >>> trim('   Hello, World!   ')
        'Hello, World!'

        >>> trim('\\t\\n  Python  \\n\\t')
        'Python'
    """
    if not docstring:
        return ''
    lines = docstring.expandtabs().splitlines()
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    return '\n'.join(trimmed)


def ok_msg(message: str) -> str:
    """
    Turns the message green.
    
    Args:
        message (str): The string to trim.

    Returns:
        message (str): Returns it ascii colored.
    """
    return str(f'{bcolors.OKGREEN}{trim(message)}{bcolors.ENDC}')


def err_msg(message: str) -> str:
    """
    Turns the message red.
    
    Args:
        message (str): The string to trim.

    Returns:
        message (str): Returns it ascii colored.
    """
    return str(f'{bcolors.FAIL}{trim(message)}{bcolors.ENDC}')

