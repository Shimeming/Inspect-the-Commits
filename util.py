import os
import platform


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cbc_print(string: str, interval: float = 0.25):
    '''
    print the string char by char
    '''
    print(string)
