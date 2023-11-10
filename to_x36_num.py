# Converts x10 number to x36 number
from const import BASE, x36_DICT_rev

PROMPT = 'Enter x10 number: '


def convert_x10_to_x36() -> None:
    """Converts x10 number to x36"""
    result = []
    prompt = int(get_x10_number())
    while prompt > 0:
        number = prompt % BASE
        if number in x36_DICT_rev.keys():
            result.append(x36_DICT_rev.get(number))
        else:
            result.append(number)
        prompt //= BASE
    print('x36 number: ', end='')
    print(*result[::-1], sep='')


def get_x10_number() -> str:
    """Gets x36 number from user's input"""
    return input(PROMPT)
