#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from game import Game
from cell import Cell

class TestGame(unittest.TestCase):

    def setUp(self):
        self.cell = Cell()
        self.game = Game(10)


    def test_next_step(self):
        c1 = Cell(state = 'alive', live_neighbours = 1)

        c2 = Cell(state = 'alive', live_neighbours = 2)

        c3 = Cell(live_neighbours = 3)

        c4 = Cell(state = 'alive', live_neighbours = 4)

        self.game.board = [[c1,c2], [c3, c4]]
        board = self.game.next_step()

        self.assertEqual(board[0][0].state, 'dead')
        self.assertEqual(board[0][1].state, 'alive')
        self.assertEqual(board[1][0].state, 'alive')
        self.assertEqual(board[1][1].state, 'dead')


    def test_underpopulation(self):
        self.cell.state = 'alive'
        self.cell.live_neighbours = 1
        self.cell = self.game.check_rules(self.cell)

        self.assertEqual(self.cell.next_state, 'dead')

        self.cell.live_neighbours = 0
        self.cell = self.game.check_rules(self.cell)

        self.assertEqual(self.cell.next_state, 'dead')


    def test_overpopulation(self):
        self.cell.state = 'alive'
        self.cell.live_neighbours = 4
        self.cell = self.game.check_rules(self.cell)

        self.assertEqual(self.cell.next_state, 'dead')


    def test_survive(self):
        self.cell.state = 'alive'
        self.cell.live_neighbours = 2
        self.cell = self.game.check_rules(self.cell)

        self.assertEqual(self.cell.next_state, 'alive')

        self.cell.live_neighbours = 3
        self.cell = self.game.check_rules(self.cell)

        self.assertEqual(self.cell.next_state, 'alive')


    def test_become_alive(self):
        self.cell.state = 'dead'
        self.cell.live_neighbours = 3
        self.cell = self.game.check_rules(self.cell)

        self.assertEqual(self.cell.next_state, 'alive')


    def test_board_is_a_square_matrix(self):
        self.assertEqual(len(self.game.board), 10)
        self.assertEqual(len(self.game.board[0]), 10)

        self.game.board = self.game.set_board([], 5)

        self.assertEqual(len(self.game.board), 5)
        self.assertEqual(len(self.game.board[0]), 5)


    def test_board_is_a_matrix_of_cells(self):
        self.assertEqual(self.list_elements_instance_of(self.game.board, list), True)

        for row in self.game.board:
            self.assertEqual(self.list_elements_instance_of(row, Cell), True)


    def test_board_sets_neighbours(self):
        cell = self.game.board[5][5]
        self.assertEqual(len(cell.neighbours), 8)


    def test_neighbour_change_state(self):
        self.game.board[0][1].state = 'alive'
        self.assertEqual(self.game.board[0][0].live_neighbours, 1)


    def test_set_neighours_return_a_cell(self):
        cell = self.game.set_neighbours(self.game.board, [0,0])

        self.assertEqual(isinstance(cell, Cell), True)


    def test_set_right_amount_of_neighours(self):
        cell = self.game.set_neighbours(self.game.board, [0,0])
        self.assertEqual(len(cell.neighbours), 3)

        cell = self.game.set_neighbours(self.game.board, [0,5])
        self.assertEqual(len(cell.neighbours), 5)

        cell = self.game.set_neighbours(self.game.board, [0,9])
        self.assertEqual(len(cell.neighbours), 3)

        cell = self.game.set_neighbours(self.game.board, [5,0])
        self.assertEqual(len(cell.neighbours), 5)

        cell = self.game.set_neighbours(self.game.board, [5,5])
        self.assertEqual(len(cell.neighbours), 8)

        cell = self.game.set_neighbours(self.game.board, [5,9])
        self.assertEqual(len(cell.neighbours), 5)

        cell = self.game.set_neighbours(self.game.board, [5,9])
        self.assertEqual(len(cell.neighbours), 5)

        cell = self.game.set_neighbours(self.game.board, [9,0])
        self.assertEqual(len(cell.neighbours), 3)

        cell = self.game.set_neighbours(self.game.board, [9,5])
        self.assertEqual(len(cell.neighbours), 5)

        cell = self.game.set_neighbours(self.game.board, [9,9])
        self.assertEqual(len(cell.neighbours), 3)


    def test_duplicate_set_neighbours(self):
        cell = self.game.set_neighbours(self.game.board, [0,0])
        cell = self.game.set_neighbours(self.game.board, [0,0])
        self.assertEqual(len(cell.neighbours), 3)

        c1 = self.game.set_neighbours(self.game.board, [5,5])
        c2 = self.game.set_neighbours(self.game.board, [5,6])
        self.assertEqual(len(c1.neighbours), 8)

    def test_linked_negihbours(self):
        cell = self.game.set_neighbours(self.game.board, [5,5])
        neighbour = cell.neighbours[0]
        self.assertEqual(cell in neighbour.neighbours, True)
        self.assertEqual(neighbour in cell.neighbours, True)


    def test_delimit_number(self):
        number = self.game.delimit_number(-1, 28)
        self.assertEqual(number, 0)

        number = self.game.delimit_number(7, 5)
        self.assertEqual(number, 5)

        number = self.game.delimit_number(3, 5)
        self.assertEqual(number, 3)


    def list_elements_instance_of(self, list, type):
        return all(isinstance(x, type) for x in list)

if __name__ == '__main__':
    unittest.main()

