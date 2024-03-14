import os
import platform
import time


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cbc_print(string: str, interval: float = 0.05):
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
    str3 = ''
    for i in range(len(str1)):
        str3 += chr(ord(str1[i]) ^ ord(str2[i]))
    return str3

def unlock(key: str, slot: list[int]):
    if len(key) != len(slot):
        return 'WRONG_KEY'
    str3 = ''
    for i in range(len(key)):
        str3 += chr(ord(key[i]) ^ slot[i])
    return str3
