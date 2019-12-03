#!/usr/bin/python
# -*- coding: utf-8 -*-

class Cell:

    def __init__(self,state = 'dead', neighbours = [], live_neighbours = 0, next_state = 'dead'):
        self.state = state
        self.next_state = next_state
        self.neighbours = neighbours
        self.live_neighbours = live_neighbours

    @property
    def live_neighbours(self):
        live_neighbours = 0
        for neighbour in self.neighbours:
            if neighbour.state == 'alive':
                live_neighbours += 1

        return live_neighbours

    @live_neighbours.setter
    def live_neighbours(self, n):
        self.neighbours = []
        for i in range(n):
            self.neighbours.append(Cell(state = 'alive'))

    def draw(self):
        if self.state == 'alive':
            print('■', end = ' ')
        else:
            print('□', end = ' ')

