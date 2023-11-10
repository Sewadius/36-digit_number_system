# Main executable file
from const import GREET, MENU, PROMPT
import to_x10_num as x10
import to_x36_num as x36


def print_greet() -> None:
    """Prints the greeting and the menu"""
    print(GREET, MENU, sep='\n')


def get_choice_menu() -> str:
    """Get user's choice for menu items"""
    return input(PROMPT)


def main():
    """Main function"""
    print_greet()
    match get_choice_menu():
        case '1':                           # Convert x36 to x10 number
            x10.convert_x36_to_x10()
        case '2':                           # Convert x10 to x36 number
            x36.convert_x10_to_x36()


if __name__ == '__main__':
    main()
