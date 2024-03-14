import const
import util
import time
import copy


class Maze():
    def __init__(self):
        self.player_position = const.MAZE_START_POINT
        self.goal_position = const.MAZE_GOAL_POINT
        self.state = 'running'

    def render_run(self):
        def change_char(s: str, ind: int, new_char: str):
            return s[:ind] + new_char + s[ind+1:]
        graph = copy.deepcopy(const.MAZE_MAP)
        graph[self.player_position[0]] = change_char(
            graph[self.player_position[0]], self.player_position[1], 'O')
        graph[self.goal_position[0]] = change_char(
            graph[self.goal_position[0]], self.goal_position[1], 'G')
        for line in graph:
            print(line)
        print()

    def run(self):
        while self.state == 'running':
            util.clear()
            self.render_run()
            print('''
Credit:
The maze map is copied from the homework 1 of Foundations of Artificial Intelligence (CSIE obligatory course).

Goal:
Move the player ('O') to obtain the goal ('G').

Options:
* W/A/S/D or w/a/s/d:
    move up/left/down/right
    invalid move will be ignored
* 0:
    stop the game and return to the home screen
* other:
    the option will be ignored
Please enter a sequence of operations: ''', end='')
            options = input()
            for opt in list(options):
                if opt == '0':
                    self.state = 'stop'
                    break
                if opt == 'W' or opt == 'w':
                    new_position = tuple(
                        map(lambda i, j: i + j, self.player_position, (-1, 0)))
                if opt == 'A' or opt == 'a':
                    new_position = tuple(
                        map(lambda i, j: i + j, self.player_position, (0, -1)))
                if opt == 'S' or opt == 's':
                    new_position = tuple(
                        map(lambda i, j: i + j, self.player_position, (1, 0)))
                if opt == 'D' or opt == 'd':
                    new_position = tuple(
                        map(lambda i, j: i + j, self.player_position, (0, 1)))
                if const.MAZE_MAP[new_position[0]][new_position[1]] == ' ':
                    self.player_position = new_position
                util.clear()
                self.render_run()
                print(f'option: {opt}')
                time.sleep(0.15)
                if self.player_position == self.goal_position:
                    self.state = 'complete'
                    break
        if self.state == 'complete':
            print('Congratulation!')
            print(f'The secret key is "{const.MAZE_REWARD}".')
