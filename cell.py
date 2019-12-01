#!/usr/bin/python
# -*- coding: utf-8 -*-

class Cell:

    def __init__(self,state = 'dead', neighbours = [], live_neighbours = 0, next_state = ''):
        self.state = state
        self.next_state = next_state
        self.neighbours = neighbours
        self.live_neighbours = live_neighbours

    def draw(self):
        if self.state == 'alive':
            print('■', end = ' ')
        else:
            print('□', end = ' ')

