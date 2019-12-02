#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from game import Game
from cell import Cell

class TestGame(unittest.TestCase):

    def setUp(self):
        self.cell = Cell()
        self.game = Game()

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

if __name__ == '__main__':
    unittest.main()

