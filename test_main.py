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


    def test_board_sets_neighbours(self):
        cell = self.board[5][5]
        self.assertEqual(len(cell.neighbours), 8)


    def test_neighbour_change_state(self):
        self.board[0][1].state = 'alive'
        self.assertEqual(self.board[0][0].live_neighbours, 1)


    def test_set_neighours_return_a_cell(self):
        cell = main.set_neighbours(self.board, [0,0])

        self.assertEqual(isinstance(cell, Cell), True)


    def test_set_right_amount_of_neighours(self):
        cell = main.set_neighbours(self.board, [0,0])
        self.assertEqual(len(cell.neighbours), 3)

        cell = main.set_neighbours(self.board, [0,5])
        self.assertEqual(len(cell.neighbours), 5)

        cell = main.set_neighbours(self.board, [0,9])
        self.assertEqual(len(cell.neighbours), 3)

        cell = main.set_neighbours(self.board, [5,0])
        self.assertEqual(len(cell.neighbours), 5)

        cell = main.set_neighbours(self.board, [5,5])
        self.assertEqual(len(cell.neighbours), 8)

        cell = main.set_neighbours(self.board, [5,9])
        self.assertEqual(len(cell.neighbours), 5)

        cell = main.set_neighbours(self.board, [5,9])
        self.assertEqual(len(cell.neighbours), 5)

        cell = main.set_neighbours(self.board, [9,0])
        self.assertEqual(len(cell.neighbours), 3)

        cell = main.set_neighbours(self.board, [9,5])
        self.assertEqual(len(cell.neighbours), 5)

        cell = main.set_neighbours(self.board, [9,9])
        self.assertEqual(len(cell.neighbours), 3)


    def test_duplicate_set_neighbours(self):
        cell = main.set_neighbours(self.board, [0,0])
        cell = main.set_neighbours(self.board, [0,0])
        self.assertEqual(len(cell.neighbours), 3)

        c1 = main.set_neighbours(self.board, [5,5])
        c2 = main.set_neighbours(self.board, [5,6])
        self.assertEqual(len(c1.neighbours), 8)

    def test_linked_negihbours(self):
        cell = main.set_neighbours(self.board, [5,5])
        neighbour = cell.neighbours[0]
        self.assertEqual(cell in neighbour.neighbours, True)
        self.assertEqual(neighbour in cell.neighbours, True)


    def test_delimit_number(self):
        number = main.delimit_number(-1, 28)
        self.assertEqual(number, 0)

        number = main.delimit_number(7, 5)
        self.assertEqual(number, 5)

        number = main.delimit_number(3, 5)
        self.assertEqual(number, 3)


    def list_elements_instance_of(self, list, type):
        return all(isinstance(x, type) for x in list)

if __name__ == '__main__':
    unittest.main()
