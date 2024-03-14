import util
import const
import home


def main():
    util.clear()
    print()
    print(const.WELCOME_MESSAGE)
    util.cbc_print('Press enter to continue...')
    input()
    util.clear()
    home.home()


if __name__ == '__main__':
    main()
