#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import Game
from cell import Cell

def main():
    board = [
            [Cell(), Cell()],
            [Cell(), Cell()]
            ]
    game = Game(board)
    print('Board')
    game.print_board()


if __name__ == '__main__':
    main()
