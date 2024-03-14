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


def xor_two_str(str1: str, str2: str):
    assert(len(str1) == len(str2))
    str3 = ''
    for i in range(len(str1)):
        str3 += chr(ord(str1[i]) ^ ord(str2[i]))
    return str3
