#!/usr/bin/python
# -*- coding: utf-8 -*-

from cell import Cell

class Game:

    def __init__(self, board_size):
        self.board = self.set_board([], board_size)


    def set_board(self, board, size):
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(Cell())

        for i in range(size):
            for j in range(size):
                cell = self.set_neighbours(board, [i,j])
                board[i][j] = cell

        return board;


    def set_neighbours(self, board, position):
        limit_x = len(board) - 1
        limit_y = len(board[0]) - 1

        cell = board[position[0]][position[1]]

        start_x = self.delimit_number(position[0] - 1, limit_x)
        start_y = self.delimit_number(position[1] - 1, limit_y)

        end_x = self.delimit_number(position[0] + 1, limit_x)
        end_y = self.delimit_number(position[1] + 1, limit_y)

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                neighbour = board[i][j]
                if not cell == neighbour:
                    if not cell in neighbour.neighbours:
                        neighbour.neighbours.append(cell)
                        cell.neighbours.append(neighbour)

        return cell


    def delimit_number(self, number, limit):
        if number < 0: return 0;
        if number > limit: return limit;
        return number


    def next_step(self):
        for row in self.board:
            row = list(map(self.check_rules, row))

        for row in self.board:
            for cell in row:
                cell.state = cell.next_state

        return self.board


    def check_rules(self, cell):
        if cell.state == 'alive':
            if cell.live_neighbours < 2 or cell.live_neighbours > 3:
                cell.next_state = 'dead'
            else:
                cell.next_state = 'alive'
        elif cell.live_neighbours == 3:
            cell.next_state = 'alive'

        return cell


    def print_board(self):
        for row in self.board:
            for cell in row:
                cell.draw()
            print('')

