# Converts x36 number to x10 number
from const import x36_DICT, BASE

PROMPT = 'Enter x36 number: '


def convert_x36_to_x10() -> None:
    """Converts x36 number to x10"""
    result = 0
    prompt = get_x36_number()
    data_list = [ch for ch in prompt]
    power = len(data_list) - 1                          # Initial power for calculation
    for n in data_list:
        if n in x36_DICT.keys():                        # Letter
            result += x36_DICT.get(n) * BASE ** power
        else:                                           # Digit
            result += int(n) * BASE ** power
        power -= 1
    print(f'x10 number: {result}')


def get_x36_number() -> str:
    """Gets x36 number from user's input"""
    return input(PROMPT)
