# Main executable file
from const import GREET, MENU, PROMPT
import to_x10_number as x10


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


if __name__ == '__main__':
    main()
