# Change your own console colors using colorama
from colorama import Fore, Back, Style

def color(text: str, fg, bg=None) -> str:
    colored_text = f'{fg}{text}{Style.RESET_ALL}'
    return colored_text if bg is None  else bg + colored_text

if __name__ == '__main__':
    print(f'This is {color("Hello, World!", Fore.LIGHTYELLOW_EX)}!')
    print(f'This is {color("Hello, World!", Fore.LIGHTWHITE_EX, Back.RED)}! This is some more 'f'{color("Hello, World!", Fore.LIGHTRED_EX)}')

create_new_color = f'This is {color("Hello, World!", Fore.LIGHTGREEN_EX)}!'
print(create_new_color)
