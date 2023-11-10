# Converts x36 number to x10 number
PROMPT = 'Enter x36 number: '
BASE = 36
x36_DICT = {
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18,
    'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27,
    's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
}


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
