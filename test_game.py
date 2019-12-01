#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from game import Game
from cell import Cell

class TestGame(unittest.TestCase):

    def setUp(self):
        self.cell = Cell()
        self.game = Game()

    def test_underpopulation(self):
        self.cell.state = 'alive'
        self.cell.live_neighbours = 1
        self.cell = self.game.underpopulation(self.cell)

        self.assertEqual(self.cell.next_state, 'dead')

        self.cell.live_neighbours = 0
        self.cell = self.game.underpopulation(self.cell)

        self.assertEqual(self.cell.next_state, 'dead')

if __name__ == '__main__':
    unittest.main()

