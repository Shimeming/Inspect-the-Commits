import os
import platform
import time


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cbc_print(string: str, interval: float = 0.1):
    '''
    Print the string char by char.
    '''
    for c in string:
        print(c, end='', flush=True)
        time.sleep(interval)


def wbw_print(string: str, interval: float = 0.3):
    '''
    Print the string word by word.
    The string should not contain '\n'
    '''
    for s in string.split():
        print(s, end=' ', flush=True)
        time.sleep(interval)
