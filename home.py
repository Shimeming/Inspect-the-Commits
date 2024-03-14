import util


def home():
    action = '0'
    while action not in ['1', '2', '3']:
        action = input('''
Please select an action you want to do.
  * 1)  Challenge 1
  * 2)  Challenge 2
  * 3)  Merge the two keys
Enter a number: ''')
        util.clear()

    action = int(action)
    if action == 1:
        pass
    if action == 2:
        pass
    if action == 3:
        pass
