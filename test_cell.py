#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from cell import Cell


class TestCell(unittest.TestCase):

    def test_live_neighbours(self):
        cell = Cell(live_neighbours = 2)

        self.assertEqual(cell.live_neighbours, 2)

        cell.live_neighbours = 5

        self.assertEqual(cell.live_neighbours, 5)

if __name__ == '__main__':
    unittest.main()
