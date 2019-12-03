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

    for i in range(size):
        for j in range(size):
            cell = set_neighbours(board, [i,j])
            board[i][j] = cell

    return board;

def set_neighbours(board, position):
    limit_x = len(board) - 1
    limit_y = len(board[0]) - 1

    cell = board[position[0]][position[1]]

    start_x = delimit_number(position[0] - 1, limit_x)
    start_y = delimit_number(position[1] - 1, limit_y)

    end_x = delimit_number(position[0] + 1, limit_x)
    end_y = delimit_number(position[1] + 1, limit_y)

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            neighbour = board[i][j]
            if not cell == neighbour:
                if not cell in neighbour.neighbours:
                    neighbour.neighbours.append(cell)
                    cell.neighbours.append(neighbour)

    return cell

def delimit_number(number, limit):
    if number < 0: return 0;
    if number > limit: return limit;
    return number

if __name__ == '__main__':
    main()
