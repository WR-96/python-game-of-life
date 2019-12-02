#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:

    def __init__(self, board = []):
        self.board = board

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
