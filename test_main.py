#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import main
from cell import Cell

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.board = main.set_board([], 10)

    def test_board_is_a_square_matrix(self):
        self.assertEqual(len(self.board), 10)
        self.assertEqual(len(self.board[0]), 10)

        self.board = main.set_board([], 5)

        self.assertEqual(len(self.board), 5)
        self.assertEqual(len(self.board[0]), 5)

    def test_board_is_a_matrix_of_cells(self):
        self.assertEqual(self.list_elements_instance_of(self.board, list), True)

        for row in self.board:
            self.assertEqual(self.list_elements_instance_of(row, Cell), True)

    def list_elements_instance_of(self, list, type):
        return all(isinstance(x, type) for x in list)

if __name__ == '__main__':
    unittest.main()
