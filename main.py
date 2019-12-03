#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import Game
from cell import Cell

def main():
    board = set_board([], 10)
    game = Game(board)
    print('Board')
    game.print_board()

def set_board(board, size):
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(Cell())

    return board;


def delimit_number(number, limit):
    if number < 0: return 0;
    if number > limit: return limit;
    return number

if __name__ == '__main__':
    main()
