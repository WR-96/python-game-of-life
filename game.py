#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:

    def __init__(self, board = []):
        self.board = board

    def print_board(self):
        for row in self.board:
            for cell in row:
                cell.draw()
            print('')
