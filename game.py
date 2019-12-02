#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:

    def __init__(self, board = []):
        self.board = board

    def underpopulation(self, cell):
        if cell.state == 'alive':
            if cell.live_neighbours < 2:
                cell.next_state = 'dead'
        return cell

    def overpopulation(self, cell):
        if cell.state == 'alive':
            if cell.live_neighbours > 3:
                cell.next_state = 'dead'
        return cell

    def survive(self, cell):
        if cell.state == 'alive':
            if cell.live_neighbours == 2 or cell.live_neighbours == 3:
                cell.next_state = 'alive'
        return cell

    def become_alive(sefl, cell):
        if cell.state == 'dead':
            if cell.live_neighbours == 3:
                cell.next_state = 'alive'
        return cell

    def print_board(self):
        for row in self.board:
            for cell in row:
                cell.draw()
            print('')
