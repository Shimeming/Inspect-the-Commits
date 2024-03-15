import util
import const
import time
import challenge1
from hashlib import sha256


def home():
    action = '0'
    while True:
        action = input('''
If you find your screen cannot display all output, you can reduce the font size by <Ctrl> + <->.

Please select an action you want to do.
  * 1)  Challenge 1
  * 2)  Challenge 2
  * 3)  Merge the two keys and obtain the flag
  * 4)  Play games for fun. (NOT relevant to solving this problem)
  * Q)  Quit
Enter your option: ''')
        util.clear()
        
        if action == '1':
            maze = challenge1.Maze()
            maze.run()
        if action == '2':
            util.cbc_print('Please refer to README.\n')
            util.cbc_print('Hint: read README again whenever you switch between branches or commits.\n')
            # time.sleep(1)
            # util.cbc_print('Press "Enter" to continue...\n')
            # input()
            # util.clear()
        if action == '3':
            util.clear()
            print('Please insert the first key obtained from Challenge 1: ', end='')
            key1 = input()
            print('Please insert the first key obtained from Challenge 2: ', end='')
            key2 = input()
            for i in range(6):
                print('Casting the flag' + (i%3+1)*'.' + '   ', end='\r')
                time.sleep(1)
            flag1 = util.unlock(key1, const.SLOT1)
            flag2 = util.unlock(key2, const.SLOT2)
            print()
            flag = f'CSIE{{{flag1}{flag2}}}'
            if sha256(flag.encode('utf-8')).hexdigest() != const.FLAG_SHA:
                util.twinkle_print('WRONG_KEY!!!')
            else:
                print('The flag is: ')
                util.cbc_print(f'CSIE{{{flag1}{flag2}}}\n', 0.2)
        if action == '4':
            print(f'Please insert map number(0 ~ {len(const.MAZE_FUN_MAPS)-1})')
            print('An invalid input will result in automatic selection of a random map.')
            map_num = input('Map number: ')
            maze = challenge1.Maze(True, map_num)
            maze.run()
        if action == 'Q':
            break
